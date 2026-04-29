"""
Unified ASGI entrypoint.
Combines FastAPI (REST API + static files) with FastMCP (MCP endpoint).

Routes:
    /sim/*  — Simulator API
    /api/*  — Treasury calculations API
    /mcp    — MCP Streamable HTTP endpoint (for Cursor, Claude, etc.)
    /*      — Static frontend (HTML/CSS/JS)
"""

import logging
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

casada_lib = str(Path(__file__).resolve().parent.parent / "casada-tool")
if casada_lib not in sys.path:
    sys.path.insert(0, casada_lib)

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
    title="Treasury Expert API",
    description="REST API for treasury calculations, simulator, portfolio risk, and AI chat.",
    version="2.0.0",
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
from api.simulator import router as sim_router

api.include_router(calculate_router)
api.include_router(portfolio_router)
api.include_router(anbima_router)
api.include_router(chat_router)
api.include_router(sim_router)


@api.get("/health")
async def health():
    idx = get_index()
    return {"status": "healthy", "documents": len(idx.documents), "sections": len(idx.sections)}


# ── MCP ASGI App ─────────────────────────────────────────────────────────────

mcp_app = mcp.http_app(path="/", stateless_http=True)

# ── Combined ASGI App ────────────────────────────────────────────────────────

STATIC_DIR = Path(__file__).resolve().parent.parent / "static"
INDEX_HTML = STATIC_DIR / "index.html"


async def root_health(request):
    idx = get_index()
    return JSONResponse({"status": "healthy", "documents": len(idx.documents), "sections": len(idx.sections)})


async def serve_index(request):
    if INDEX_HTML.exists():
        return FileResponse(str(INDEX_HTML), media_type="text/html")
    return JSONResponse({"error": "Frontend not found"}, status_code=404)


routes = [
    Route("/health", root_health),
    Mount("/api", app=api),
    Mount("/sim", app=api),
    Mount("/mcp", app=mcp_app),
]

if STATIC_DIR.exists():
    routes.append(Mount("/static", app=StaticFiles(directory=str(STATIC_DIR))))
    routes.append(Route("/", serve_index))
    routes.append(Route("/{path:path}", serve_index))
    log.info("Serving frontend from %s", STATIC_DIR)

app = Starlette(routes=routes, lifespan=mcp_app.lifespan)


# ── CLI entrypoint ───────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn

    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", "8000"))

    log.info("Starting Treasury Expert on %s:%d", host, port)
    get_index()

    uvicorn.run(app, host=host, port=port)
