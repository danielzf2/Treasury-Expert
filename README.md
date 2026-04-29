# Treasury Expert

Simulador de operacoes de renda fixa brasileira + MCP server para AI agents.

**Live:** [web-production-d31cd.up.railway.app](https://web-production-d31cd.up.railway.app)

## Simulador TPF + Derivativos

Simulador interativo com 9 instrumentos, dados de mercado ao vivo, cenarios multi-fator e graficos Plotly.

### Instrumentos

| Tipo | Instrumento | Convencao |
|---|---|---|
| TPF | LTN, NTN-F, NTN-B, LFT | Exponencial 252 DU |
| Derivativos | DI1, DAP | Exponencial 252 DU |
| Cambio | DOL | Preco (R$/1000 USD) |
| Cupom | DDI, FRC | Linear 360 DC |

### Funcionalidades

- **Presets**: Casada LTN+DI1, NTN-F+DI1, NTN-B+DAP, DOL+DI1 (cupom sintetico), DI1+FRC (dolar sintetico)
- **Dados ao vivo**: B3 (DI1, DAP, FRC, DDI, DOL) + BCB (CDI, PTAX)
- **Ativo vs Passivo**: deteccao automatica de estrategia, fatores de risco hedgeados/expostos
- **Cenarios de curva**: Bull/Bear Parallel, Steepener, Flattener, Butterfly, Custom
- **Multi-fator**: sliders independentes para Pre, Cambio, IPCA, Cupom Cambial
- **Graficos**: Curva DI (flat forward B3 V14), Cupom Cambial, Dolar Forward, Taxa Real
- **Interpolacao**: flat forward exponencial 252 e linear 360, validada contra ANBIMA
- **KRD**: Key-Rate Duration para titulos com cupom (NTN-F, NTN-B)
- **Formulas**: referencia completa em LaTeX (KaTeX)

## MCP Server (treasury-expert-dzf)

80+ ferramentas de calculo financeiro para AI agents (Cursor, Claude, etc).

### Conectar

**Cursor** — adicione em `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "treasury-expert-dzf": {
      "url": "https://web-production-d31cd.up.railway.app/mcp"
    }
  }
}
```

**Claude Desktop:**

```json
{
  "mcpServers": {
    "treasury-expert-dzf": {
      "url": "https://web-production-d31cd.up.railway.app/mcp"
    }
  }
}
```

### Ferramentas

| Modulo | Ferramentas | Descricao |
|---|---|---|
| Titulos Publicos | 6 | LTN, NTN-F, NTN-B, LFT, fluxo de caixa |
| Curva de Juros | 4 | Flat forward, forward implicito, spot-to-PU |
| DI Futuro | 6 | PU, taxa, ajuste, carry, hedge |
| DOL Futuro | 4 | Ajuste, simulacao, forward points |
| DAP | 4 | PU, taxa, ajuste |
| FRC | 4 | PU, taxa, FRA cupom cambial |
| Swaps | 5 | Pre x CDI, cambial, IPCA, MtM |
| Cambio | 5 | NDF, cupom cambial, casado, arbitragem |
| Risco | 7 | Duration, DV01, convexidade, hedge |
| Opcoes | 4 | Black-Scholes, gregas, vol implicita |
| Conversoes | 10 | %CDI, CDI+spread, Fisher, lin360/exp252 |
| Calculo Financeiro | 7 | PV, FV, amortizacao, CDI acumulado |
| Dias Uteis | 6 | Calendario ANBIMA 2001-2099 |
| Documentacao | 7 | BM25 search, glossario, taxonomia |

### Knowledge Base

14 documentos indexados, 4.444 secoes — livros de renda fixa, derivativos, cambio, metodologia ANBIMA.

## Arquitetura

```
Treasury-Expert/
├── static/                   # Frontend (HTML/CSS/JS + Plotly.js + KaTeX)
│   ├── index.html
│   ├── app.js
│   └── style.css
├── server/                   # Backend (FastAPI + MCP)
│   ├── app.py                # ASGI entrypoint (API + MCP + static)
│   ├── treasury_mcp.py       # MCP server (BM25 + FastMCP)
│   ├── api/
│   │   ├── simulator.py      # /sim/* endpoints (12 rotas)
│   │   ├── chat.py           # AI chat com tool calling
│   │   ├── calculate.py      # Invocacao direta de tools
│   │   └── portfolio.py      # Risco de portfolio
│   └── tools/                # 18 modulos de calculo
├── casada-tool/lib/          # Logica Python do simulador
│   ├── instruments.py        # PU, Duration, DV01, KRD
│   ├── calendar.py           # Calendario ANBIMA, DU, DC
│   ├── curves.py             # Flat forward interpolation
│   ├── scenarios.py          # 9 cenarios de curva
│   ├── charts.py             # Graficos Plotly
│   ├── exposure.py           # Ativo/Passivo, estrategia, hedge
│   └── market_data.py        # B3 + BCB ao vivo
├── docs/                     # Knowledge base (markdown)
├── Dockerfile
└── requirements.txt
```

## Deploy

### Railway (recomendado)

1. Fork este repo
2. Conecte ao [Railway](https://railway.app)
3. Railway detecta o `Dockerfile` automaticamente
4. Defina `PORT` (Railway fornece) e `OPENAI_API_KEY` (opcional, para chat)
5. Site em `https://your-app.up.railway.app`
6. MCP em `https://your-app.up.railway.app/mcp`

### Docker

```bash
docker build -t treasury-expert .
docker run -p 8000:8000 treasury-expert
```

### Local

```bash
pip install -r requirements.txt
PYTHONPATH=casada-tool python server/app.py
```

Site em `http://localhost:8000`, MCP em `http://localhost:8000/mcp`.

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
