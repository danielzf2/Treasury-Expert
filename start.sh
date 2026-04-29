#!/bin/bash
set -e

echo "Starting MCP server on :8000..."
python server/app.py &
MCP_PID=$!

echo "Starting Streamlit on :8501..."
streamlit run casada-tool/app.py \
    --server.port 8501 \
    --server.headless true \
    --server.address 127.0.0.1 \
    --server.enableCORS false \
    --server.enableXsrfProtection false \
    --browser.gatherUsageStats false &
STL_PID=$!

sleep 3
echo "Starting proxy on :${PORT:-8080}..."
python proxy.py

wait $MCP_PID $STL_PID
