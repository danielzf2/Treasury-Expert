#!/bin/bash
set -e

export PYTHONPATH="/app/casada-tool:${PYTHONPATH}"

echo "Starting Treasury Expert (Streamlit + MCP) on :${PORT:-8080}..."
exec streamlit run asgi_app.py \
    --server.port "${PORT:-8080}" \
    --server.headless true \
    --server.address 0.0.0.0 \
    --server.enableCORS false \
    --server.enableXsrfProtection false \
    --browser.gatherUsageStats false
