"""
Dicionário de sinônimos e taxonomia de tópicos para tesouraria brasileira.
Cada grupo contém termos equivalentes — buscar qualquer um retorna resultados
de todos os outros do mesmo grupo.
"""

SYNONYM_GROUPS: list[list[str]] = [
    # ── TÍTULOS PÚBLICOS ──────────────────────────────────────────────
    ["LTN", "Letra do Tesouro Nacional", "Tesouro Prefixado",
     "prefixado zero cupom", "titulo prefixado sem cupom"],
    ["NTN-F", "NTNF", "Nota do Tesouro Nacional série F",
     "Tesouro Prefixado com Juros Semestrais", "prefixado com cupom"],
    ["NTN-B", "NTNB", "Nota do Tesouro Nacional série B",
     "Tesouro IPCA+", "título indexado ao IPCA", "ntnb com cupom"],
    ["NTN-B Principal", "NTNB Principal",
     "Tesouro IPCA+ sem juros semestrais", "ntnb principal"],
    ["LFT", "Letra Financeira do Tesouro", "Tesouro Selic",
     "pós-fixado Selic", "pos fixado selic"],
    ["NTN-C", "NTNC", "Nota do Tesouro Nacional série C",
     "indexado IGP-M", "título indexado igpm"],
    ["NTN-A", "NTNA", "Nota do Tesouro Nacional série A",
     "título cambial governo"],
    ["NTN-D", "NTND", "Nota do Tesouro Nacional série D"],

    # ── TÍTULOS PRIVADOS ──────────────────────────────────────────────
    ["CDB", "Certificado de Depósito Bancário", "certificado deposito"],
    ["LCI", "Letra de Crédito Imobiliário"],
    ["LCA", "Letra de Crédito do Agronegócio"],
    ["debênture", "debenture", "título corporativo", "debentures"],
    ["CRI", "Certificado de Recebíveis Imobiliários"],
    ["CRA", "Certificado de Recebíveis do Agronegócio"],
    ["DPGE", "Depósito a Prazo com Garantia Especial"],
    ["LC", "Letra de Câmbio", "letra cambio"],
    ["CCB", "Cédula de Crédito Bancário"],
    ["FIDC", "Fundo de Investimento em Direitos Creditórios"],
    ["CPR", "Cédula de Produto Rural"],
    ["LF", "Letra Financeira"],

    # ── TAXAS E ÍNDICES ───────────────────────────────────────────────
    ["CDI", "Certificado de Depósito Interbancário", "taxa DI",
     "taxa interbancária", "DI over", "taxa CDI"],
    ["SELIC", "taxa Selic", "taxa básica de juros", "Selic meta",
     "Selic over", "taxa basica"],
    ["IPCA", "Índice Nacional de Preços ao Consumidor Amplo",
     "inflação IPCA", "inflação oficial"],
    ["IGP-M", "IGPM", "Índice Geral de Preços do Mercado"],
    ["INPC", "Índice Nacional de Preços ao Consumidor"],
    ["TR", "Taxa Referencial", "taxa referencial"],
    ["TJLP", "Taxa de Juros de Longo Prazo"],
    ["TLP", "Taxa de Longo Prazo"],
    ["PTAX", "ptax", "taxa ptax", "dólar ptax", "cotação ptax"],
    ["COPOM", "Copom", "Comitê de Política Monetária"],

    # ── DURATION E RISCO DE TAXA ──────────────────────────────────────
    ["duration", "duração", "duration de Macaulay", "Macaulay duration",
     "prazo médio ponderado"],
    ["duration modificada", "Dmod", "modified duration",
     "duração modificada", "sensibilidade ao yield"],
    ["duration efetiva", "effective duration", "duração efetiva",
     "OAD", "option adjusted duration"],
    ["convexidade", "convexity", "curvatura", "convexidade positiva",
     "convexidade negativa"],
    ["DV01", "basis point value", "BPV", "PVBP", "PV01",
     "risco de um basis point", "dollar value of 01"],
    ["key rate duration", "KRD", "duration parcial",
     "partial duration", "duration por vértice"],
    ["dollar duration", "DD", "duration em dólar",
     "duration ponderada pelo preço"],

    # ── PRECIFICAÇÃO ──────────────────────────────────────────────────
    ["PU", "Preço Unitário", "preço do título", "preço de mercado",
     "preco unitario"],
    ["valor presente", "VP", "PV", "present value",
     "valor atual", "valor descontado"],
    ["valor futuro", "VF", "FV", "future value",
     "montante", "valor capitalizado"],
    ["valor nominal", "VN", "VNA", "face value", "notional", "nocional",
     "principal", "valor de face"],
    ["YTM", "yield to maturity", "taxa interna de retorno", "TIR",
     "yield", "rendimento até o vencimento"],
    ["current yield", "taxa de retorno corrente", "yield corrente"],
    ["fluxo de caixa", "cash flow", "FC", "fluxos", "fluxo"],
    ["cupom", "coupon", "juros semestrais", "cupom semestral"],
    ["cupom limpo", "clean price", "preço limpo", "preco limpo"],
    ["cupom sujo", "dirty price", "preço sujo", "preço cheio",
     "full price", "preco sujo"],
    ["juros acumulados", "accrued interest", "juros acruados",
     "juros pro rata"],
    ["deságio", "desconto", "discount", "abaixo do par"],
    ["ágio", "prêmio", "premium", "acima do par"],
    ["par", "ao par", "valor ao par", "preço par"],
    ["cotação", "quote", "preço cotado"],

    # ── CURVA DE JUROS ────────────────────────────────────────────────
    ["ETTJ", "Estrutura a Termo da Taxa de Juros", "curva de juros",
     "yield curve", "term structure", "estrutura a termo",
     "curva a termo"],
    ["taxa spot", "taxa zero", "zero rate", "spot rate",
     "taxa à vista"],
    ["taxa forward", "taxa a termo", "taxa futura", "forward rate",
     "taxa implícita"],
    ["interpolação", "interpolar", "interpolação flat forward",
     "flat forward", "interpolação linear"],
    ["bootstrapping", "bootstrap", "extração de taxas zero",
     "stripping"],
    ["curva pré", "curva prefixada", "curva DI", "curva nominal"],
    ["curva de cupom", "curva cupom IPCA", "curva real",
     "curva de juros reais"],
    ["curva cupom cambial", "curva de dólar", "cupom cambial",
     "curva cupom limpo", "FRA curve"],
    ["spread de crédito", "credit spread", "prêmio de crédito"],
    ["vértice", "tenor", "prazo", "maturity", "bucket"],

    # ── DERIVATIVOS: FUTUROS ──────────────────────────────────────────
    ["DI futuro", "contrato futuro de DI", "DI1", "futuro de DI",
     "futuro de taxa de juros", "contrato DI"],
    ["dólar futuro", "DOL", "contrato futuro de dólar",
     "futuro de câmbio", "dolar futuro"],
    ["mini dólar", "WDO", "mini contrato de dólar"],
    ["DDI", "futuro de cupom cambial", "cupom cambial futuro",
     "DI x dólar"],
    ["FRC", "forward rate agreement de cupom", "FRA de cupom",
     "cupom limpo futuro"],
    ["DAP", "futuro de cupom IPCA", "DI x IPCA",
     "cupom IPCA futuro"],
    ["SCC", "swap cambial com cupom"],
    ["Ibovespa futuro", "IND", "índice futuro",
     "futuro de Ibovespa", "WIN"],

    # ── DERIVATIVOS: SWAPS ────────────────────────────────────────────
    ["swap", "swap de taxa", "swap DI pré", "swap pré x DI",
     "interest rate swap"],
    ["swap cambial", "swap de câmbio", "swap dólar",
     "swap DI x dólar"],
    ["swap IPCA", "swap DI x IPCA", "swap inflação"],
    ["swap reverso", "reverse swap"],
    ["ponta ativa", "leg ativa", "receiving leg"],
    ["ponta passiva", "leg passiva", "paying leg"],
    ["nocional do swap", "notional do swap", "valor de referência"],
    ["ajuste diário", "daily settlement", "ajuste"],

    # ── DERIVATIVOS: OPÇÕES ───────────────────────────────────────────
    ["opção", "option", "opções", "options"],
    ["call", "opção de compra", "direito de compra"],
    ["put", "opção de venda", "direito de venda"],
    ["Black-Scholes", "Black Scholes", "BS",
     "modelo Black-Scholes", "Black-Scholes-Merton"],
    ["Black 76", "modelo Black", "Black model",
     "modelo de Black 76"],
    ["binomial", "modelo binomial", "árvore binomial", "CRR",
     "Cox Ross Rubinstein"],
    ["volatilidade implícita", "implied vol", "vol implícita", "IV"],
    ["superfície de volatilidade", "vol surface",
     "smile de volatilidade", "smile", "skew"],
    ["strike", "preço de exercício", "exercise price"],
    ["prêmio da opção", "option premium", "prêmio"],
    ["valor intrínseco", "intrinsic value"],
    ["valor extrínseco", "extrinsic value", "valor tempo",
     "time value"],
    ["in the money", "ITM", "dentro do dinheiro"],
    ["out of the money", "OTM", "fora do dinheiro"],
    ["at the money", "ATM", "no dinheiro"],
    ["cap", "teto", "interest rate cap"],
    ["floor", "piso", "interest rate floor"],
    ["collar", "colar", "interest rate collar"],
    ["swaption", "opção sobre swap"],

    # ── GREGAS ────────────────────────────────────────────────────────
    ["delta", "Δ", "delta da opção"],
    ["gamma", "Γ", "gama", "gamma da opção"],
    ["theta", "Θ", "theta da opção", "decaimento temporal"],
    ["vega", "ν", "sensibilidade à volatilidade"],
    ["rho", "ρ", "sensibilidade à taxa de juros"],
    ["greeks", "gregas", "sensibilidades", "letras gregas"],

    # ── OPERAÇÕES: FORWARDS E TERMOS ──────────────────────────────────
    ["NDF", "Non Deliverable Forward", "termo de moeda",
     "forward de câmbio", "forward cambial"],
    ["termo", "forward", "contrato a termo"],
    ["casado", "câmbio casado", "operação casada",
     "spot + forward"],

    # ── OPERAÇÕES: REPO E FUNDING ─────────────────────────────────────
    ["compromissada", "repo", "operação compromissada",
     "repurchase agreement", "overnight repo"],
    ["compromissada reversa", "reverse repo",
     "compromissada de entrada"],
    ["funding", "captação", "custo de captação",
     "custo de funding"],
    ["CDI over", "overnight", "taxa overnight", "DI over"],

    # ── OPERAÇÕES: ESTRATÉGIAS ────────────────────────────────────────
    ["hedge", "proteção", "hedging", "cobertura"],
    ["imunização", "immunization", "hedge de duration",
     "imunização de carteira"],
    ["carry", "carrego", "carry trade"],
    ["roll down", "rolagem", "roll", "efeito rolagem"],
    ["spread trade", "operação de spread",
     "arbitragem de spread"],
    ["butterfly", "borboleta", "butterfly spread"],
    ["flattener", "achatamento", "aposta no achatamento"],
    ["steepener", "inclinação", "aposta na inclinação"],
    ["basis trade", "operação de base"],
    ["alavancagem", "leverage", "alavancado"],

    # ── MARCAÇÃO E CONTABILIDADE ──────────────────────────────────────
    ["marcação a mercado", "MtM", "mark to market", "MaM",
     "a mercado", "marcação a mercado"],
    ["marcação na curva", "mark to curve", "pela curva",
     "na curva", "marcação na curva"],
    ["P&L", "resultado", "lucro e perda", "profit and loss"],
    ["MTM", "variação de marcação", "resultado de mercado"],
    ["carregamento", "resultado de carrego", "accrual"],
    ["banking book", "carteira banking", "carteira de crédito"],
    ["trading book", "carteira trading", "carteira de negociação"],

    # ── RISCO ─────────────────────────────────────────────────────────
    ["VaR", "Value at Risk", "valor em risco"],
    ["CVaR", "Expected Shortfall", "ES", "conditional VaR",
     "perda esperada condicional"],
    ["stress test", "teste de estresse", "cenário de estresse"],
    ["risco de mercado", "market risk"],
    ["risco de crédito", "credit risk"],
    ["risco de liquidez", "liquidity risk"],
    ["risco operacional", "operational risk"],
    ["volatilidade", "vol", "volatility", "σ"],
    ["correlação", "correlation"],
    ["backtesting", "backtest", "teste retroativo"],

    # ── ANBIMA ────────────────────────────────────────────────────────
    ["ANBIMA", "Associação Brasileira das Entidades dos Mercados Financeiro e de Capitais"],
    ["metodologia ANBIMA", "precificação ANBIMA",
     "ANBIMA pricing", "ANBIMA metodologia"],
    ["taxa indicativa", "taxa ANBIMA", "taxa referência ANBIMA"],

    # ── CÂMBIO ────────────────────────────────────────────────────────
    ["câmbio", "FX", "foreign exchange", "mercado de câmbio"],
    ["USD/BRL", "dólar real", "dolar real", "USDBRL",
     "cotação do dólar"],
    ["EUR/BRL", "euro real", "EURBRL"],
    ["cupom cambial", "cupom limpo de câmbio",
     "taxa de juros em dólar no Brasil"],
    ["EMBI", "EMBI+", "risco país", "risco brasil",
     "spread soberano"],
    ["CDS", "credit default swap", "CDS Brasil"],

    # ── MERCADO / OPERACIONAL ─────────────────────────────────────────
    ["dias úteis", "du", "business days", "dia útil", "DU"],
    ["dias corridos", "dc", "calendar days", "dia corrido", "DC"],
    ["base 252", "convenção 252", "dias úteis por ano",
     "ano de 252 dias"],
    ["base 360", "convenção 360", "dias corridos por ano"],
    ["base 365", "convenção 365", "actual 365"],
    ["CETIP", "B3", "clearing", "câmara"],
    ["Tesouro Direto", "TD", "programa tesouro direto"],
    ["leilão", "auction", "oferta pública", "leilão tesouro"],
    ["basis point", "bps", "ponto base", "bp",
     "ponto percentual", "basis points"],
    ["notional", "nocional", "valor de referência",
     "valor nocional"],

    # ── CÁLCULO FINANCEIRO ────────────────────────────────────────────
    ["juros compostos", "compound interest",
     "capitalização composta", "exponencial"],
    ["juros simples", "simple interest",
     "capitalização simples", "linear"],
    ["taxa equivalente", "equivalent rate",
     "equivalência de taxas", "taxa equivalente"],
    ["taxa nominal", "nominal rate"],
    ["taxa real", "real rate", "taxa deflacionada",
     "taxa descontada da inflação"],
    ["taxa efetiva", "effective rate", "taxa efetiva anual"],
    ["taxa over", "overnight rate", "taxa overnight"],
    ["taxa proporcional", "proportional rate"],
    ["fator de capitalização", "fator de acumulação",
     "fator composto"],
    ["desconto racional", "desconto composto",
     "rational discount"],
    ["desconto comercial", "desconto bancário",
     "desconto simples", "bank discount"],
    ["amortização", "amortization", "amortizacao"],
    ["SAC", "Sistema de Amortização Constante"],
    ["Price", "tabela Price", "sistema francês",
     "parcela fixa", "sistema price"],
    ["perpetuidade", "perpetuity", "fluxo perpétuo"],
    ["anuidade", "annuity", "série uniforme"],
    ["taxa acumulada", "taxa composta acumulada",
     "fator acumulado"],
    ["VNA", "Valor Nominal Atualizado",
     "valor nominal atualizado pelo IPCA"],
    ["cotação percentual", "cotação do título",
     "preço percentual do par"],
    ["truncamento", "truncar", "truncamento CDI",
     "arredondamento CDI"],
    ["over", "taxa over", "CDI over", "taxa diária"],

    # ── INSTITUIÇÕES E REGULAÇÃO ──────────────────────────────────────
    ["Banco Central", "BCB", "BACEN", "BC"],
    ["CVM", "Comissão de Valores Mobiliários"],
    ["STN", "Secretaria do Tesouro Nacional", "Tesouro Nacional"],
    ["CMN", "Conselho Monetário Nacional"],
    ["SUSEP", "Superintendência de Seguros Privados"],
]

TOPIC_TAXONOMY: dict[str, dict[str, list[str]]] = {
    "Renda Fixa": {
        "Títulos Públicos Federais": [
            "LTN", "NTN-F", "NTN-B", "NTN-B Principal", "LFT",
        ],
        "Títulos Privados": [
            "CDB", "LCI", "LCA", "debênture", "CRI", "CRA", "LF",
        ],
        "Precificação de Títulos": [
            "PU", "fluxo de caixa", "valor presente", "YTM",
            "cupom limpo", "cupom sujo", "VNA",
        ],
        "Risco de Taxa de Juros": [
            "duration", "duration modificada", "convexidade",
            "DV01", "key rate duration",
        ],
        "Curva de Juros": [
            "ETTJ", "taxa spot", "taxa forward", "interpolação",
            "bootstrapping", "curva pré", "curva de cupom",
        ],
    },
    "Derivativos": {
        "Contratos Futuros": [
            "DI futuro", "dólar futuro", "DDI", "FRC", "DAP",
        ],
        "Swaps": [
            "swap", "swap cambial", "swap IPCA", "ponta ativa",
            "ponta passiva", "ajuste diário",
        ],
        "Opções": [
            "call", "put", "Black-Scholes", "Black 76",
            "binomial", "cap", "floor", "collar", "swaption",
        ],
        "Gregas": [
            "delta", "gamma", "theta", "vega", "rho",
        ],
        "Forwards e Termos": [
            "NDF", "termo", "casado",
        ],
    },
    "Operações de Tesouraria": {
        "Hedge e Imunização": [
            "hedge", "imunização", "key rate duration",
        ],
        "Carry e Rolagem": [
            "carry", "roll down",
        ],
        "Estratégias de Curva": [
            "butterfly", "flattener", "steepener", "spread trade",
        ],
        "Funding e Repo": [
            "compromissada", "funding", "CDI over",
        ],
    },
    "Câmbio": {
        "Mercado Spot": ["câmbio", "USD/BRL", "PTAX"],
        "Derivativos de Câmbio": [
            "dólar futuro", "NDF", "swap cambial", "DDI",
            "cupom cambial",
        ],
        "Risco País": ["EMBI", "CDS"],
    },
    "Risco e Controle": {
        "Métricas de Risco": ["VaR", "CVaR", "stress test"],
        "Categorias de Risco": [
            "risco de mercado", "risco de crédito",
            "risco de liquidez",
        ],
        "Marcação": [
            "marcação a mercado", "marcação na curva",
        ],
    },
    "Cálculo Financeiro": {
        "Regimes de Capitalização": [
            "juros compostos", "juros simples",
        ],
        "Taxas": [
            "taxa equivalente", "taxa nominal", "taxa real",
            "taxa efetiva", "taxa over",
        ],
        "Amortização": [
            "SAC", "Price", "amortização",
        ],
        "Desconto": [
            "desconto racional", "desconto comercial",
        ],
        "Séries": [
            "perpetuidade", "anuidade",
        ],
    },
    "Institucional": {
        "Reguladores": [
            "Banco Central", "CVM", "STN", "CMN",
        ],
        "Infraestrutura": [
            "CETIP", "B3", "Tesouro Direto", "ANBIMA",
        ],
        "Convenções": [
            "dias úteis", "base 252", "base 360", "basis point",
        ],
    },
}


def build_synonym_lookup() -> dict[str, list[str]]:
    """Retorna {termo_normalizado: [todos os sinônimos do grupo]}."""
    import unicodedata
    lookup: dict[str, list[str]] = {}
    for group in SYNONYM_GROUPS:
        for alias in group:
            key = unicodedata.normalize("NFKD", alias.lower())
            key = "".join(c for c in key if not unicodedata.combining(c))
            lookup[key] = group
    return lookup
