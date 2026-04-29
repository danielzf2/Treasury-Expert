"""Unified ASGI app: Streamlit + MCP on the same port.

Uses streamlit.starlette.App to mount MCP endpoint alongside Streamlit.
Routes:
    /mcp   — MCP Streamable HTTP (for Cursor, Claude, etc.)
    /api/* — REST API (calculate, portfolio, chat)
    /*     — Streamlit casada-tool
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "server"))

from starlette.routing import Mount, Route
from starlette.responses import JSONResponse
from streamlit.starlette import App

from treasury_mcp import mcp, get_index
from api.chat import router as chat_router
from api.calculate import router as calculate_router
from api.portfolio import router as portfolio_router
from api.anbima import router as anbima_router

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

api = FastAPI(title="Treasury API", docs_url="/api/docs", openapi_url="/api/openapi.json")
api.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
api.include_router(calculate_router)
api.include_router(portfolio_router)
api.include_router(anbima_router)
api.include_router(chat_router)

mcp_app = mcp.http_app(path="/", stateless_http=True)


async def health(request):
    idx = get_index()
    return JSONResponse({"status": "healthy", "documents": len(idx.documents), "sections": len(idx.sections)})


app = App(
    "casada-tool/app.py",
    routes=[
        Route("/health", health),
        Mount("/api", app=api),
        Mount("/mcp", app=mcp_app),
    ],
)
