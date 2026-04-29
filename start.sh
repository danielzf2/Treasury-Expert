#!/bin/bash
set -e

export PYTHONPATH="/app/casada-tool:/app/server:${PYTHONPATH}"

echo "Starting Treasury Expert on :${PORT:-8080}..."
exec uvicorn asgi_app:app \
    --host 0.0.0.0 \
    --port "${PORT:-8080}"
