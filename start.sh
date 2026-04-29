#!/bin/bash
set -e

echo "Starting MCP server on :8000..."
python server/app.py &
MCP_PID=$!

sleep 2
echo "Starting Streamlit on :${PORT:-8080}..."
exec streamlit run casada-tool/app.py \
    --server.port "${PORT:-8080}" \
    --server.headless true \
    --server.address 0.0.0.0 \
    --server.enableCORS false \
    --server.enableXsrfProtection false \
    --browser.gatherUsageStats false
