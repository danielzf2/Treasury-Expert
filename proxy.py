"""Reverse proxy — routes requests to Streamlit (main site) or MCP server.

Streamlit runs on :8501, MCP/API on :8000.
This proxy listens on $PORT (Railway) and forwards by path prefix.
Supports HTTP and WebSocket (required by Streamlit).
"""

import os
import asyncio
import logging

import httpx
import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocket

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("proxy")

MCP_UPSTREAM = "http://127.0.0.1:8000"
STL_UPSTREAM = "http://127.0.0.1:8501"

MCP_PREFIXES = ("/mcp", "/api", "/health", "/docs", "/openapi.json")

_http_client: httpx.AsyncClient | None = None


async def _get_client() -> httpx.AsyncClient:
    global _http_client
    if _http_client is None or _http_client.is_closed:
        _http_client = httpx.AsyncClient(timeout=httpx.Timeout(120, connect=10))
    return _http_client


def _pick_upstream(path: str) -> str:
    for prefix in MCP_PREFIXES:
        if path == prefix or path.startswith(prefix + "/"):
            return MCP_UPSTREAM
    return STL_UPSTREAM


async def _proxy_http(request: Request) -> Response:
    upstream = _pick_upstream(request.url.path)
    client = await _get_client()

    url = f"{upstream}{request.url.path}"
    if request.url.query:
        url += f"?{request.url.query}"

    body = await request.body()
    headers = dict(request.headers)
    headers.pop("host", None)

    try:
        resp = await client.request(
            method=request.method,
            url=url,
            headers=headers,
            content=body,
        )
    except httpx.ConnectError:
        return Response(f"Upstream {upstream} not ready", status_code=502)

    excluded = {"transfer-encoding", "content-encoding", "content-length"}
    resp_headers = {k: v for k, v in resp.headers.items() if k.lower() not in excluded}

    return Response(
        content=resp.content,
        status_code=resp.status_code,
        headers=resp_headers,
    )


async def _proxy_ws(websocket: WebSocket) -> None:
    """Proxy WebSocket connections to Streamlit."""
    import websockets

    upstream = _pick_upstream(websocket.url.path)
    ws_url = upstream.replace("http://", "ws://") + websocket.url.path
    if websocket.url.query:
        ws_url += f"?{websocket.url.query}"

    await websocket.accept()

    try:
        async with websockets.connect(ws_url) as ws_upstream:
            async def client_to_upstream():
                try:
                    while True:
                        data = await websocket.receive_text()
                        await ws_upstream.send(data)
                except Exception:
                    pass

            async def upstream_to_client():
                try:
                    async for msg in ws_upstream:
                        if isinstance(msg, str):
                            await websocket.send_text(msg)
                        else:
                            await websocket.send_bytes(msg)
                except Exception:
                    pass

            await asyncio.gather(client_to_upstream(), upstream_to_client())
    except Exception as e:
        log.debug("WS proxy closed: %s", e)
    finally:
        try:
            await websocket.close()
        except Exception:
            pass


app = Starlette(
    routes=[
        WebSocketRoute("/_stm/{path:path}", _proxy_ws),
        WebSocketRoute("/_stm", _proxy_ws),
        WebSocketRoute("/stream", _proxy_ws),
        Route("/{path:path}", _proxy_http, methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"]),
        Route("/", _proxy_http, methods=["GET", "POST"]),
    ],
)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "8080"))
    log.info("Proxy listening on :%d -> MCP(%s) + Streamlit(%s)", port, MCP_UPSTREAM, STL_UPSTREAM)
    uvicorn.run(app, host="0.0.0.0", port=port)
