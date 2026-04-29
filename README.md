# TradingCore-MCP — Treasury Knowledge Base

MCP server for Brazilian fixed income, derivatives, and treasury operations.
Powered by BM25 search with synonym expansion across 1,800+ indexed sections from 6 reference documents.

## Connect to the MCP

The server is deployed remotely — no installation needed. Just add the configuration to your MCP client.

### Cursor

Add to your project's `.cursor/mcp.json` (or global settings):

```json
{
  "mcpServers": {
    "treasury-docs": {
      "url": "https://web-production-07294.up.railway.app/mcp"
    }
  }
}
```

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "treasury-docs": {
      "url": "https://web-production-07294.up.railway.app/mcp"
    }
  }
}
```

### Claude Code (CLI)

```bash
claude mcp add treasury-docs https://web-production-07294.up.railway.app/mcp
```

### Any MCP client

The server exposes a standard **MCP Streamable HTTP** endpoint at `/mcp`. Any client that supports this transport can connect.

---

## Available Tools (80 total)

### Documentation & Search (7 tools)

| Tool | Description |
|---|---|
| `search(query, top_k)` | BM25 search with synonym expansion. Returns ranked sections with snippets |
| `read_document(path)` | Read full document content |
| `read_section(path, section)` | Read a specific section |
| `list_documents()` | List all documents with metadata |
| `list_sections(path)` | List table of contents for a document |
| `glossary(term)` | Lookup synonyms, related topics, and documents for a term |
| `list_topics()` | Browse the complete topic taxonomy |

### Government Bonds — `titulos_publicos.py` (6 tools)

| Tool | Description |
|---|---|
| `precificar_ltn` | LTN pricing per ANBIMA methodology (T-14, T-6 truncation) |
| `precificar_ntnf` | NTN-F pricing with semiannual coupon (10% p.a.), discounted cash flows |
| `precificar_ntnb` | NTN-B pricing via quotation% × VNA (6% p.a. coupon) |
| `precificar_lft` | LFT pricing with premium/discount in bps over Selic VNA |
| `fluxo_caixa_titulo` | Cash flow table (LTN, NTN-F or NTN-B) with ANBIMA truncation rules |
| `ref_titulos_publicos` | Reference: ANBIMA methodology per bond type, truncation rules |

### Yield Curve — `curva_juros.py` (4 tools)

| Tool | Description |
|---|---|
| `interpolar_flat_forward` | Interpolate spot rate via constant forward between two vertices |
| `calcular_forward` | Implied forward rate between two vertices (exponential, 252 bd) |
| `taxa_spot_para_pu` | Convert spot rate to PU given face value |
| `ref_curva_juros` | Reference: flat forward, linear interpolation, bootstrapping |

### DI Futures — `futuros_di.py` (6 tools)

| Tool | Description |
|---|---|
| `pu_di` | DI1 PU from annual rate and business days |
| `taxa_di` | Implied annual rate from DI1 PU |
| `ajuste_di` | Daily settlement (D0 or D+n with CDI correction) |
| `carry_di` | Carry simulation over N business days (constant rate and CDI) |
| `hedge_di` | Number of contracts for DV01 hedge |
| `ref_di1` | Reference: DI1 contract specifications |

### Dollar Futures — `futuros_dol.py` (4 tools)

| Tool | Description |
|---|---|
| `ajuste_dol` | Daily settlement for DOL or WDO (mini) |
| `simular_posicao_dol` | Multi-day settlement simulation with PA list |
| `forward_points` | Forward points (futures − spot) and % of spot |
| `ref_dol` | Reference: DOL and WDO (multipliers, quotation, expiry) |

### DAP (IPCA Coupon Futures) — `futuros_dap.py` (4 tools)

| Tool | Description |
|---|---|
| `pu_dap` | DAP PU from IPCA coupon % p.a. (252 bd base) |
| `taxa_dap` | Implied IPCA coupon from PU |
| `ajuste_dap` | Settlement with CDI/IPCA correction |
| `ref_dap` | Reference: DAP contract, relationship with NTN-B |

### FRC (FX Coupon Futures) — `futuros_frc.py` (4 tools)

| Tool | Description |
|---|---|
| `pu_frc` | FRC PU (linear, 360 calendar days base) |
| `taxa_frc` | Implied FX coupon from PU |
| `fra_cupom_cambial` | Forward rate agreement between two tenors (linear 360) |
| `ref_frc` | Reference: FRC vs DDI, conventions |

### Swaps — `swaps.py` (5 tools)

| Tool | Description |
|---|---|
| `swap_pre_di` | Fixed vs CDI swap: compare legs at maturity |
| `swap_cambial` | FX swap vs fixed (PTAX, linear coupon, fixed 252 bd) |
| `swap_ipca` | IPCA+ vs CDI swap: real leg vs floating leg |
| `mtm_swap_pre` | Simplified MtM of fixed swap (principal discounting) |
| `ref_swaps` | Reference: fixed×CDI, FX, IPCA swaps |

### FX — `cambio.py` (5 tools)

| Tool | Description |
|---|---|
| `calcular_ndf` | Theoretical NDF via covered interest rate parity |
| `calcular_cupom_cambial` | Implied FX coupon from spot and futures |
| `calcular_casado` | Forward points and premium/discount % |
| `arbitragem_cambio_juros` | Compare theoretical NDF with market futures (deviation) |
| `ref_cambio` | Reference: PTAX, casado, NDF, FX coupon |

### Risk — `risco.py` (7 tools)

| Tool | Description |
|---|---|
| `duration_macaulay` | Macaulay duration from cash flows and business days |
| `duration_modificada` | Modified duration (simple and 252 bd daily adjustment) |
| `duration_anbima` | ANBIMA duration in business days: Σ(dui × PUi) / Σ(PUi) |
| `convexidade` | Convexity with (1+y)^(du/252) discounting |
| `dv01` | Approximate DV01 (Dmod × PV × 0.0001) |
| `hedge_di_futuro` | Number of DI contracts for DV01 hedge |
| `aproximar_variacao_preco` | 2nd-order Taylor: ΔP/P with duration and convexity |

### Options — `opcoes.py` (4 tools)

| Tool | Description |
|---|---|
| `black_scholes` | Black-Scholes price (T = du/252) with Greeks |
| `gregas` | Delta, Gamma, Theta, Vega, Rho for call and put |
| `vol_implicita` | Implied volatility via Newton-Raphson |
| `ref_opcoes` | Reference: BS, Black-76, Greeks, moneyness, time decay |

### Rate Conversions — `conversoes_taxas.py` (10 tools)

| Tool | Description |
|---|---|
| `pct_cdi_para_cdi_spread_tool` | %CDI → CDI+ spread (daily factor equivalence) |
| `cdi_spread_para_pct_cdi_tool` | CDI+ spread → %CDI (inverse) |
| `pre_para_pct_cdi_tool` | Fixed rate % p.a. → %CDI |
| `pct_cdi_para_pre_tool` | %CDI → fixed rate % p.a. |
| `pre_para_cdi_spread_tool` | Fixed → spread over CDI (compounding) |
| `cdi_spread_para_pre_tool` | CDI + spread → fixed rate % p.a. |
| `nominal_para_real_tool` | Nominal and IPCA → real rate (Fisher) |
| `real_para_nominal_tool` | Real and IPCA → nominal rate (Fisher) |
| `exponencial_para_linear_tool` | Exponential 252 bd → linear 360 cd |
| `linear_para_exponencial_tool` | Linear 360 cd → exponential 252 bd |

### Financial Math — `calculo_financeiro.py` (7 tools)

| Tool | Description |
|---|---|
| `taxa_equivalente_tool` | Equivalent rate between tenors in business days |
| `valor_presente_tool` | PV = FV / (1+rate)^(du/252) |
| `valor_futuro_tool` | FV = PV × (1+rate)^(du/252) |
| `acumular_cdi_tool` | Accumulate daily CDI (product of factors) |
| `taxa_over_para_anual_tool` | Overnight rate % → annual 252 bd and back |
| `amortizacao_tool` | Price or SAC amortization table |
| `ref_calculo_financeiro_tool` | Reference: compound, simple, equivalence, day-count bases |

### Conventions — `convencoes.py` (1 tool)

| Tool | Description |
|---|---|
| `referencia_rapida_tool` | Formula and convention lookup by topic (LTN, DI1, duration, %CDI, etc.) |

### Business Days — `dias_uteis.py` (6 tools)

| Tool | Description |
|---|---|
| `dias_uteis_entre` | Business days between two dates (ANBIMA calendar) |
| `dias_uteis_anbima` | ANBIMA DU for bond pricing (settlement inclusive, maturity exclusive) |
| `proximo_dia_util` | Next business day from a date |
| `verificar_dia_util` | Check if a date is an ANBIMA business day |
| `listar_feriados_ano` | List ANBIMA holidays for a year (2001–2099) |
| `ref_dias_uteis` | Reference: business day conventions, 252/360/365 bases |

### Search Features

- **BM25 (Okapi)** — probabilistic ranking over 1,800+ indexed sections
- **Synonym expansion** — searching "Dmod" finds "duration modificada", "modified duration", etc.
- **Section-level indexing** — precise results at section level, not full documents
- **100+ synonym groups** — comprehensive coverage of instruments, rates, concepts, derivatives

### Topic Taxonomy

Renda Fixa · Derivativos · Operações de Tesouraria · Câmbio · Risco e Controle · Cálculo Financeiro · Institucional

---

## Knowledge Base

| Document | Sections | Topics |
|---|---|---|
| Cálculo Financeiro das Tesourarias | 400+ | Juros, capitalização, desconto, duration, convexidade |
| Mercado Financeiro (Assaf) | 350+ | Sistema financeiro, renda fixa, derivativos |
| Derivativos: Negociação e Precificação | 250+ | Futuros, swaps, opções, gregas, hedge |
| Mercado de Renda Fixa | 200+ | Títulos públicos, curva de juros, DI futuro |
| Ebook DAP | 80+ | Cupom IPCA, DAP, ajuste diário |
| Metodologia ANBIMA | 15+ | Precificação de títulos públicos |

---

## Web Frontend

The project includes a professional web interface for treasury traders with three main features:

### Features

- **Chat** — AI-powered assistant (OpenAI GPT-4o) with access to all 80+ calculation tools and the knowledge base. Streaming responses with markdown rendering.
- **Portfolio** — Input your bond portfolio (LTN, NTN-F, NTN-B, LFT), compute per-bond and aggregate risk metrics (Duration, DV01, Convexity), get DI futures hedge suggestions, and simulate parallel rate shocks.
- **Calculator** — Standalone ANBIMA-compliant bond pricing with full truncation/rounding rules.

### REST API (for the frontend)

| Endpoint | Description |
|---|---|
| `POST /api/chat` | AI chat with tool calling (streaming SSE) |
| `POST /api/calculate` | Call any tool directly by name |
| `GET /api/tools` | List all available tools with metadata |
| `POST /api/portfolio/risk` | Compute portfolio risk metrics |
| `POST /api/portfolio/hedge` | DI futures hedge suggestion |
| `POST /api/portfolio/scenario` | Parallel rate shock simulation |
| `GET /api/health` | Health check |
| `GET /api/docs` | Interactive API documentation (Swagger) |

---

## Self-Hosting

### Docker

```bash
docker build -t treasury-mcp .
docker run -p 8000:8000 -e OPENAI_API_KEY=your-key treasury-mcp
```

The web frontend will be at `http://localhost:8000`.
MCP endpoint at `http://localhost:8000/mcp`.
API docs at `http://localhost:8000/api/docs`.

### Local Development

```bash
# Backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
echo 'OPENAI_API_KEY=your-key' >> .env
export $(grep -v '^#' .env | xargs)
uvicorn server.app:app --host 0.0.0.0 --port 8000 --reload

# Frontend (separate terminal)
cd web
npm install
npm run dev
```

The Vite dev server proxies `/api` requests to `localhost:8000`.

### MCP only (stdio, for Cursor/Claude)

```bash
TRANSPORT=stdio python server/treasury_mcp.py docs
```

### Deploy to Railway

1. Fork this repo
2. Connect to [Railway](https://railway.app)
3. Railway auto-detects the `Dockerfile` and deploys
4. Set env vars: `OPENAI_API_KEY` (required for chat), `PORT` (Railway provides automatically)
5. Your app will be at `https://your-app.up.railway.app`
6. MCP endpoint at `https://your-app.up.railway.app/mcp`

### Deploy to Render

1. Fork this repo
2. Create a new **Web Service** on [Render](https://render.com)
3. Point to this repo, Render detects the `Dockerfile`
4. Set `OPENAI_API_KEY` in environment variables
5. Your app will be at `https://your-app.onrender.com`

### Environment Variables

| Variable | Default | Description |
|---|---|---|
| `OPENAI_API_KEY` | — | OpenAI API key (required for chat feature) |
| `OPENAI_MODEL` | `gpt-4o` | OpenAI model for chat |
| `PORT` | `8000` | HTTP server port |
| `HOST` | `0.0.0.0` | HTTP server bind address |
| `DOCS_DIR` | `docs` | Path to the knowledge base directory |

---

## Architecture

```
TradingCore-MCP/
├── server/
│   ├── app.py                 # Unified ASGI entrypoint (FastAPI + MCP + static)
│   ├── treasury_mcp.py        # MCP server (BM25 + FastMCP)
│   ├── synonyms.py            # Synonym dictionary + topic taxonomy
│   ├── api/                   # REST API endpoints
│   │   ├── chat.py            # POST /api/chat (OpenAI + tool calling)
│   │   ├── calculate.py       # POST /api/calculate (direct tool invocation)
│   │   └── portfolio.py       # POST /api/portfolio/* (risk, hedge, scenario)
│   ├── services/              # Business logic
│   │   ├── chat_service.py    # OpenAI orchestration with streaming
│   │   ├── portfolio_service.py # Portfolio risk computations
│   │   └── tool_registry.py   # Auto-collects 90+ tool functions
│   └── tools/                 # Calculation tools (18 modules)
├── web/                       # React frontend (Vite + TailwindCSS)
│   ├── src/
│   │   ├── pages/             # ChatPage, PortfolioPage, CalculatorPage
│   │   ├── components/        # UI components (chat, portfolio, calculator)
│   │   ├── stores/            # Zustand state (portfolio in localStorage)
│   │   └── api/               # API client
│   └── package.json
├── docs/
│   ├── books/                 # Converted reference books (markdown)
│   └── methodologies/         # Converted methodologies (markdown)
├── scripts/
│   ├── convert_pdfs.py        # PDF → Markdown converter (Mistral OCR)
│   └── sanitize_latex.py      # LaTeX residue cleaner
├── Dockerfile                 # Multi-stage: Node build + Python runtime
├── Procfile                   # PaaS deployment
└── requirements.txt
```

## Adding New Documents

### 1. Set up the API key (once)

The converter uses the [Mistral AI](https://console.mistral.ai/) OCR API. Create a `.env` file at the project root:

```bash
echo 'MISTRAL_API_KEY=your-key-here' > .env
```

The `.env` is in `.gitignore` — your key never goes to the repository.

### 2. Run the conversion

```bash
source .venv/bin/activate
export $(grep -v '^#' .env | xargs)
python scripts/convert_pdfs.py "path/to/file.pdf" --category books
```

For ANBIMA methodologies or similar:

```bash
python scripts/convert_pdfs.py "path/to/file.pdf" --category methodologies
```

### What the script does

```
PDF → Mistral OCR → Raw markdown → LaTeX sanitizer → docs/{category}/{slug}.md
```

1. Sends the PDF to Mistral OCR API (`mistral-ocr-latest`)
2. Receives per-page markdown and assembles the file with YAML frontmatter
3. Automatically runs `sanitize_latex.py` to clean LaTeX notation residues from OCR
4. Writes the result to `docs/books/` or `docs/methodologies/`

### Options

| Flag | Effect |
|---|---|
| `--category books` | Write to `docs/books/` (default) |
| `--category methodologies` | Write to `docs/methodologies/` |
| `--output path/custom.md` | Custom output path |
| `--overwrite` | Overwrite if `.md` already exists |

### 3. Verify in the MCP

After conversion, the MCP server detects the new file automatically (compares mtimes).
To force: Ctrl+Shift+P → "MCP: Reload" in Cursor.

## Tests

```bash
source .venv/bin/activate
python -m pytest tests/ -v
```
