"""
Referência rápida por tópico: fórmulas, convenções de mercado e exemplo numérico curto.
"""

from __future__ import annotations

import unicodedata
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _norm_key(s: str) -> str:
    s = s.strip().lower()
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c))


# alias normalizado -> id canônico do tópico
_ALIASES: dict[str, str] = {}
for alias, cid in [
    ("ltn", "LTN"),
    ("tesouro prefixado", "LTN"),
    ("ntn-f", "NTN-F"),
    ("ntn f", "NTN-F"),
    ("prefixado cupom", "NTN-F"),
    ("ntn-b", "NTN-B"),
    ("tesouro ipca", "NTN-B"),
    ("lft", "LFT"),
    ("tesouro selic", "LFT"),
    ("di1", "DI1"),
    ("di futuro", "DI1"),
    ("futuro di", "DI1"),
    ("dol", "DOL"),
    ("dolar futuro", "DOL"),
    ("dap", "DAP"),
    ("cupom ipca", "DAP"),
    ("frc", "FRC"),
    ("cupom cambial", "FRC"),
    ("swap", "SWAP"),
    ("ndf", "NDF"),
    ("forward cambio", "NDF"),
    ("duration", "DURATION"),
    ("dv01", "DV01"),
    ("convexidade", "CONVEXIDADE"),
    ("black-scholes", "BLACK_SCHOLES"),
    ("black scholes", "BLACK_SCHOLES"),
    ("opcoes", "BLACK_SCHOLES"),
    ("opções", "BLACK_SCHOLES"),
    ("%cdi", "PCT_CDI"),
    ("pct cdi", "PCT_CDI"),
    ("percentual cdi", "PCT_CDI"),
    ("cdi+", "CDI_PLUS"),
    ("cdi spread", "CDI_PLUS"),
    ("ipca", "IPCA_FISHER"),
    ("fisher", "IPCA_FISHER"),
    ("base 252", "BASE_252"),
    ("dias uteis", "BASE_252"),
    ("base 360", "BASE_360"),
    ("linear", "BASE_360"),
]:
    _ALIASES[_norm_key(alias)] = cid


def _entry_ltn() -> str:
    return "\n".join([
        "LTN — Letra do Tesouro Nacional (prefixado)",
        "",
        "Fórmulas (cupom zero, VN tipicamente R$ 1.000,00)",
        "  PU = VN / (1 + r/100)^(du/252)   com r = taxa interna % a.a. (base 252, exponencial)",
        "  r = (VN/PU)^(252/du) - 1  (em %)",
        "",
        "Convenções",
        "  • Pagamento único no vencimento; não paga cupons.",
        "  • Cotação em % a.a. ou PU; mercado secundário ANBIMA/B3.",
        "",
        "Exemplo numérico",
        "  VN = 1.000, r = 12% a.a., du = 252 → PU = 1.000 / 1,12^1 ≈ 892,86",
    ])


def _entry_ntnf() -> str:
    return "\n".join([
        "NTN-F — Tesouro Prefixado com cupom",
        "",
        "Fórmulas (esboço)",
        "  Preço = soma dos fluxos descontados: cupons semestrais e principal;",
        "  desconto em base exponencial 252 du com taxa de mercado.",
        "  Cupom: taxa nominal anual, pagamentos a cada ~126 du (semestral).",
        "",
        "Convenções",
        "  • Fluxos prefixados em R$; duration intermediária entre LTN e título longo zerado.",
        "  • Marcação com curva pré ou spread sobre benchmark.",
        "",
        "Exemplo numérico",
        "  Se taxa flat 11% a.a. e cupom 10% a.a., o PU fica próximo do par quando o título está",
        "  na paridade; afastamentos vêm do desalinhamento cupom vs curva.",
    ])


def _entry_ntnb() -> str:
    return "\n".join([
        "NTN-B — Tesouro IPCA+",
        "",
        "Fórmulas (estrutura)",
        "  Fluxos nominais indexados pelo IPCA: VNA_t = VNA_{t-1} × fator IPCA;",
        "  cupom real sobre VNA; desconto com taxa real de mercado (base 252 du).",
        "  Relação Fisher entre componentes nominal e real nas projeções.",
        "",
        "Convenções",
        "  • Proteção contra inflação medida pelo IPCA; cupom semestral em % real.",
        "  • Marcação com ETTJ IPCA ou spreads.",
        "",
        "Exemplo numérico",
        "  IPCA esperado 4,5% a.a. e taxa real 6% a.a. → taxa nominal ≈ (1,045×1,06 - 1) ≈ 10,77% a.a.",
    ])


def _entry_lft() -> str:
    return "\n".join([
        "LFT — Tesouro Selic",
        "",
        "Fórmulas",
        "  Valor nominal atualizado pela taxa Selic (ou fator equivalente divulgado pela STN);",
        "  PU cotado como % do VNA (quotes em percentual do VNA).",
        "",
        "Convenções",
        "  • Pós-fixado diário; marcação acompanha variação da Selic/meta.",
        "  • Duration baixa (próxima de zero em certas métricas de carteira overnight).",
        "",
        "Exemplo numérico",
        "  VNA sobe com os fatores diários da Selic; se PU = 100% do VNA, investidor recebe exatamente",
        "  a remuneração do indexador no período.",
    ])


def _entry_di1() -> str:
    return "\n".join([
        "DI1 — contrato futuro de juros (DI)",
        "",
        "Fórmulas",
        "  PU do contrato (referência) ≈ 100.000 / (1 + i/100)^(du/252) para o vencimento;",
        "  variação de marcação proporcional à mudança da taxa implícita i (% a.a., 252 du).",
        "",
        "Convenções",
        "  • Ajuste diário em R$; tick e especificação B3.",
        "  • Hedge de taxa pré para bancos e fundos; alinhamento com CDI/curva DI.",
        "",
        "Exemplo numérico",
        "  du = 126, i = 10,5% a.a. → fator = 1,105^(126/252) ≈ 1,05114 → PU ≈ 100.000/1,05114 ≈ 95.133",
    ])


def _entry_dol() -> str:
    return "\n".join([
        "DOL — dólar futuro (B3)",
        "",
        "Fórmulas",
        "  PnL em R$ ligado à variação do dólar de ajuste vs entrada, vezes tamanho do contrato;",
        "  pontos de dólar × valor por ponto (conforme contrato/vencimento).",
        "",
        "Convenções",
        "  • Ajuste diário; referência de câmbio para hedge corporativo.",
        "  • Não confundir com NDF (OTC) nas regras de liquidação.",
        "",
        "Exemplo numérico",
        "  Se o contrato move 0,05 R$/US$ e o multiplicador for US$ 50.000, o impacto é 0,05 × 50.000 = 2.500 R$ por contrato.",
    ])


def _entry_dap() -> str:
    return "\n".join([
        "DAP — cupom IPCA futuro",
        "",
        "Fórmulas",
        "  PU ≈ 100.000 / (1 + c/100)^(du/252)  com c = cupom IPCA implícito % a.a. (252 du).",
        "",
        "Convenções",
        "  • Exposição à taxa real forward; face de referência R$ 100.000 por contrato.",
        "  • Ajuste envolve CDI e IPCA conforme especificação da bolsa.",
        "",
        "Exemplo numérico",
        "  c = 6,20% a.a., du = 504 → PU ≈ 100.000 / 1,062^2 ≈ 88.696 (ilustrativo).",
    ])


def _entry_frc() -> str:
    return "\n".join([
        "FRC — forward rate agreement cambial (cupom cambial)",
        "",
        "Fórmulas (conceito)",
        "  Compensa diferença entre taxa cambial forward acordada e taxa de mercado no vencimento,",
        "  sobre notional em moeda (estrutura OTC ou bolsa conforme série).",
        "",
        "Convenções",
        "  • Hedge de taxa de câmbio futura; fixa nível forward vs spot+carry.",
        "",
        "Exemplo numérico",
        "  Forward acordado 5,40 R$/US$ vs mercado 5,50 no vencimento → pagamento proporcional ao notional",
        "  e ao desvio (conforme lado da operação).",
    ])


def _entry_swap() -> str:
    return "\n".join([
        "Swap — troca de fluxos",
        "",
        "Fórmulas",
        "  Valor = PV(recebidos) - PV(pagos); cada perna descontada com curva apropriada (pré, %CDI, IPCA).",
        "  Taxa par: taxa fixa que zera o NPV na origem.",
        "",
        "Convenções",
        "  • Swap DI x pré: perna flutuante em %CDI; perna fixa em pré composto 252.",
        "  • Marcação a mercado com curva DI e convenções de calendário.",
        "",
        "Exemplo numérico",
        "  Notional 10 mi, recebe CDI, paga 11% a.a.; se curva implicar CDI médio 10,2%, o swap pode abrir",
        "  com valor diferente de zero até o ajuste de spread.",
    ])


def _entry_ndf() -> str:
    return "\n".join([
        "NDF — forward de câmbio não entregável",
        "",
        "Fórmulas",
        "  Liquidação em R$ pela diferença entre taxa forward contratada e taxa de fixação à vista,",
        "  vezes notional em moeda estrangeira (sem entrega física da moeda).",
        "",
        "Convenções",
        "  • OTC; datas de fixação e PTAX; crédito de contraparte.",
        "",
        "Exemplo numérico",
        "  NDF compra US$ 1 mi a 5,20; fixação 5,35 → recebedor de dólar ganha (5,35-5,20)×1 mi US$ em R$.",
    ])


def _entry_duration() -> str:
    return "\n".join([
        "Duration (Macaulay e modificada)",
        "",
        "Fórmulas",
        "  D_mac = Σ t_k × w_k   com w_k = PV(fluxo_k) / preço",
        "  D_mod = D_mac / (1 + y/m)  (m = períodos por ano da taxa y)",
        "  Aproximação ΔP/P ≈ -D_mod × Δy (linear)",
        "",
        "Convenções",
        "  • Renda fixa BR: y em base 252 exponencial para títulos públicos em muitos modelos.",
        "  • Portfolio duration = média das durations ponderada por valor de mercado (aproximação).",
        "",
        "Exemplo numérico",
        "  Título com D_mod = 4,0 e Δy = +0,50 p.p. → ΔP/P ≈ -4 × 0,005 = -2,0% (linear).",
    ])


def _entry_dv01() -> str:
    return "\n".join([
        "DV01 — dollar value of 01",
        "",
        "Fórmulas",
        "  DV01 ≈ - (dP/dy) × 1 bp  ou  P × D_mod × 0,0001  (aproximação)",
        "",
        "Convenções",
        "  • Mede sensibilidade do valor em dinheiro a 1 basis point na curva.",
        "  • Soma de DV01s em hedge ratio entre ativo e hedge.",
        "",
        "Exemplo numérico",
        "  Posição R$ 50.000.000, D_mod = 5 → |ΔP| ≈ P × D_mod × 1 bp = 50.000.000 × 5 × 0,0001 = 25.000 R$",
        "  (ordem de grandeza da variação de valor para +1 basis point na taxa).",
    ])


def _entry_convexidade() -> str:
    return "\n".join([
        "Convexidade",
        "",
        "Fórmulas",
        "  ΔP/P ≈ -D_mod × Δy + 1/2 × C × (Δy)²",
        "  C convexidade (medida de curvatura da relação preço-taxa).",
        "",
        "Convenções",
        "  • Corrige a duration para movimentos grandes de curva; ativos com fluxos dispersos têm mais convexidade.",
        "",
        "Exemplo numérico",
        "  D_mod = 6, C = 55, Δy = +1 p.p. → parte linear -6×0,01 = -6%; parte convexa +0,5×55×0,0001 = +0,275%",
    ])


def _entry_black_scholes() -> str:
    return "\n".join([
        "Black-Scholes / opções",
        "",
        "Fórmulas (call europeia, S=spot, K=strike, r sem risco, σ vol, T em anos)",
        "  d1 = (ln(S/K) + (r + σ²/2) T) / (σ √T)",
        "  d2 = d1 - σ √T",
        "  C = S N(d1) - K e^(-rT) N(d2)",
        "",
        "Convenções",
        "  • Mercado de ações: dividendos ajustam S ou usa Black-Scholes-Merton;",
        "  • FX/opções cambiais: usação de duas taxas (doméstica e estrangeira).",
        "",
        "Exemplo numérico",
        "  S=100, K=100, T=1, r=5% a.a., σ=20% → d1≈0,35, call ≈ 10,45 (ordem de grandeza; use calculadora).",
    ])


def _entry_pct_cdi() -> str:
    return "\n".join([
        "%CDI — percentual do CDI",
        "",
        "Fórmulas (convenção diária usual)",
        "  Fator 1 du = 1 + CDI_over × (%CDI/100)  com CDI_over = (1+CDI/100)^(1/252) - 1",
        "",
        "Convenções",
        "  • CCB, CDB, operações overnight frequentemente indexadas a %CDI.",
        "  • Diferente de 'CDI + spread' composto multiplicativo anual — ver também tópico CDI+.",
        "",
        "Exemplo numérico",
        "  CDI 13,65% a.a., %CDI = 100% → mesmo que CDI; %CDI = 105% → remunera 5% a mais que o over",
        "  aplicado no produto diário (não é só somar 5 p.p. na taxa a.a. sem converter).",
    ])


def _entry_cdi_plus() -> str:
    return "\n".join([
        "CDI+ / spread sobre CDI",
        "",
        "Fórmulas",
        "  Forma multiplicativa anual: (1+pré/100) = (1+CDI/100) × (1+spread/100)",
        "  ou equivalência diária: (1 + CDI_over + spread_over) vs %CDI no outro módulo.",
        "",
        "Convenções",
        "  • Crédito privado: 'CDI + X%' costuma ser spread composto ou embutido no contrato;",
        "  • Sempre confirmar se X é linear em taxa a.a. ou embutido no dia a dia.",
        "",
        "Exemplo numérico",
        "  CDI 12% a.a., spread 1,5% a.a. → pré ≈ 1,12×1,015 - 1 = 13,68% a.a.",
    ])


def _entry_ipca_fisher() -> str:
    return "\n".join([
        "IPCA / Fisher",
        "",
        "Fórmulas",
        "  (1 + i_nom/100) = (1 + i_real/100) × (1 + π/100)",
        "  i_real = ((1+i_nom)/(1+π) - 1) × 100",
        "",
        "Convenções",
        "  • IPCA é índice oficial de consumidor no Brasil; NTN-B e projeções de mercado usam IPCA implícito.",
        "",
        "Exemplo numérico",
        "  i_nom = 11%, π = 4% → i_real = (1,11/1,04 - 1)×100 ≈ 6,73% a.a.",
    ])


def _entry_base_252() -> str:
    return "\n".join([
        "Base 252 — dias úteis",
        "",
        "Fórmulas",
        "  Fator exponencial: (1 + r/100)^(du/252) com r em % a.a. e du = dias úteis.",
        "",
        "Convenções",
        "  • Padrão em títulos públicos BR, DI, muitos swaps e CDBs em taxa composta.",
        "  • Calendário: feriados ANBIMA; não confundir com 252 como 'dias do ano comercial' em outros países.",
        "",
        "Exemplo numérico",
        "  r = 10,4% a.a., du = 21 → fator = 1,104^(21/252) ≈ 1,00835 (+0,835% no mês).",
    ])


def _entry_base_360() -> str:
    return "\n".join([
        "Base 360 — juros linear (comercial)",
        "",
        "Fórmulas",
        "  Juros = principal × (taxa/100) × (dc/360)  ou desconto linear proporcional a dc.",
        "",
        "Convenções",
        "  • Comum em operações de compromissada, alguns empréstimos e mercados internacionais;",
        "  • Converter para 252 exponencial exige equivalência de taxa (ver conversões 252↔360).",
        "",
        "Exemplo numérico",
        "  Principal 1.000.000, taxa 12% a.a. linear, dc = 30 → juros = 1e6 × 0,12 × 30/360 = 10.000",
    ])


_ENTRIES: dict[str, str] = {
    "LTN": _entry_ltn(),
    "NTN-F": _entry_ntnf(),
    "NTN-B": _entry_ntnb(),
    "LFT": _entry_lft(),
    "DI1": _entry_di1(),
    "DOL": _entry_dol(),
    "DAP": _entry_dap(),
    "FRC": _entry_frc(),
    "SWAP": _entry_swap(),
    "NDF": _entry_ndf(),
    "DURATION": _entry_duration(),
    "DV01": _entry_dv01(),
    "CONVEXIDADE": _entry_convexidade(),
    "BLACK_SCHOLES": _entry_black_scholes(),
    "PCT_CDI": _entry_pct_cdi(),
    "CDI_PLUS": _entry_cdi_plus(),
    "IPCA_FISHER": _entry_ipca_fisher(),
    "BASE_252": _entry_base_252(),
    "BASE_360": _entry_base_360(),
}


def _lista_topicos() -> str:
    return ", ".join(sorted({v for v in _ALIASES.values()}))


def referencia_rapida(topico: str) -> str:
    """
    Retorna fórmulas, convenções e exemplo numérico para o tópico informado.
    Busca case-insensitive com sinônimos; se não achar, lista tópicos disponíveis.
    """
    key = _norm_key(topico)
    if not key:
        return "\n".join([
            "Informe um tópico (ex.: LTN, NTN-B, DI1, duration, %CDI).",
            "",
            "Tópicos disponíveis (ids): " + _lista_topicos(),
        ])
    cid = _ALIASES.get(key)
    if cid is None:
        return "\n".join([
            f"Tópico não encontrado: {topico!r}",
            "",
            "Tente palavras-chave como: LTN, NTN-F, NTN-B, LFT, DI1, DOL, DAP, FRC, swap, NDF,",
            "duration, DV01, convexidade, Black-Scholes, %CDI, CDI+, IPCA, base 252, base 360.",
            "",
            "Ids mapeados: " + _lista_topicos(),
        ])
    return _ENTRIES[cid]


def register(mcp: "FastMCP") -> None:
    """Registra as ferramentas deste módulo no servidor FastMCP."""

    @mcp.tool()
    def referencia_rapida_tool(topico: str) -> str:
        """Lookup: fórmulas, convenções e exemplo por tópico (LTN, DI1, duration, %CDI, etc.)."""
        return referencia_rapida(topico)

    _ = (referencia_rapida_tool,)
