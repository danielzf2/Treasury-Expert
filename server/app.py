"""
Unified ASGI entrypoint.
Combines FastAPI (REST API + static files) with FastMCP (MCP endpoint)
into a single application served by uvicorn.

Routes:
    /api/*  — REST API for the web frontend (chat, calculate, portfolio)
    /mcp    — MCP Streamable HTTP endpoint (for Cursor, Claude, etc.)
    /*      — React SPA static files (frontend)
"""

import logging
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from starlette.applications import Starlette
from starlette.routing import Mount, Route
from starlette.responses import JSONResponse, FileResponse

logging.basicConfig(level=logging.INFO, stream=sys.stderr)
log = logging.getLogger("treasury-web")

from treasury_mcp import mcp, get_index

# ── FastAPI (REST API) ───────────────────────────────────────────────────────

api = FastAPI(
    title="Treasury API",
    description="REST API for treasury calculations, portfolio risk, and AI chat.",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json",
)

api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

from api.chat import router as chat_router
from api.calculate import router as calculate_router
from api.portfolio import router as portfolio_router
from api.anbima import router as anbima_router

api.include_router(calculate_router)
api.include_router(portfolio_router)
api.include_router(anbima_router)
api.include_router(chat_router)


@api.get("/health")
async def health():
    idx = get_index()
    return {"status": "healthy", "documents": len(idx.documents), "sections": len(idx.sections)}


# ── MCP ASGI App ─────────────────────────────────────────────────────────────

mcp_app = mcp.http_app(path="/", stateless_http=True)

# ── Combined ASGI App ────────────────────────────────────────────────────────

STATIC_DIR = Path(__file__).resolve().parent.parent / "web" / "dist"
INDEX_HTML = STATIC_DIR / "index.html"


async def root_health(request):
    idx = get_index()
    return JSONResponse({"status": "healthy", "documents": len(idx.documents), "sections": len(idx.sections)})


async def spa_fallback(request):
    """Serve index.html for any route not matched by API/MCP/static — SPA client-side routing."""
    if INDEX_HTML.exists():
        return FileResponse(str(INDEX_HTML), media_type="text/html")
    return JSONResponse({"error": "Frontend not found"}, status_code=404)


routes = [
    Route("/health", root_health),
    Mount("/api", app=api),
    Mount("/mcp", app=mcp_app),
]

if STATIC_DIR.exists():
    routes.append(Mount("/assets", app=StaticFiles(directory=str(STATIC_DIR / "assets"))))
    routes.append(Route("/{path:path}", spa_fallback))
    log.info("Serving frontend from %s", STATIC_DIR)
else:
    log.warning("Frontend not found at %s — skipping static files", STATIC_DIR)

app = Starlette(routes=routes, lifespan=mcp_app.lifespan)


# ── CLI entrypoint ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn

    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("MCP_PORT", "8000"))

    log.info("Starting Treasury Web on %s:%d", host, port)
    get_index()

    uvicorn.run(app, host=host, port=port)
