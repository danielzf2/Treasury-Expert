FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server/ server/
COPY docs/ docs/
COPY casada-tool/ casada-tool/
COPY proxy.py .
COPY start.sh .
RUN chmod +x start.sh

ENV TRANSPORT=http
ENV HOST=0.0.0.0
ENV PORT=8000
ENV DOCS_DIR=/app/docs
ENV FASTMCP_STATELESS_HTTP=true

EXPOSE 8000

CMD ["./start.sh"]
