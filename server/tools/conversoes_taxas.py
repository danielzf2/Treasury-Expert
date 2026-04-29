"""
Conversões entre convenções de taxa (%CDI, CDI+, pré, real/nominal, 252 vs 360).
Todas as taxas de entrada/saída em percentual (%), salvo indicação no texto.
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _fmt_num(x: float, dec: int = 6) -> str:
    """Formata número com vírgula decimal (estilo BR)."""
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")


def _cdi_over_de_anual(cdi_aa: float) -> float:
    """CDI over (em decimal por dia útil) a partir do CDI % a.a. composto em 252 du."""
    return math.pow(1.0 + cdi_aa / 100.0, 1.0 / 252.0) - 1.0


def _spread_over_para_anual(spread_over: float) -> float:
    """Spread over → % a.a. equivalente em 252 du: (1+s_over)^252 - 1."""
    return (math.pow(1.0 + spread_over, 252.0) - 1.0) * 100.0


def _spread_anual_para_over(spread_aa: float) -> float:
    """% a.a. spread → over diário: (1+s_aa/100)^(1/252) - 1."""
    return math.pow(1.0 + spread_aa / 100.0, 1.0 / 252.0) - 1.0


def pct_cdi_para_cdi_spread(pct_cdi: float, cdi_aa: float, du: int = 252) -> str:
    """
    Converte %CDI em spread CDI+ (sobre CDI over), com equivalência dia a dia.

    Convenção usada: em cada du, o fator %CDI é (1 + CDI_over × (%CDI/100));
    o fator CDI+ equivalente é (1 + CDI_over + spread_over), com mesmo CDI_over.
    """
    if du < 0:
        return "Erro: du não pode ser negativo."
    base_cdi = 1.0 + cdi_aa / 100.0
    if base_cdi <= 0:
        return "Erro: (1 + CDI/100) deve ser positivo."
    cdi_over = _cdi_over_de_anual(cdi_aa)
    if cdi_over <= -1.0:
        return "Erro: CDI over implícito inválido."
    fator_pct_cdi_1d = 1.0 + cdi_over * (pct_cdi / 100.0)
    if fator_pct_cdi_1d <= 0:
        return "Erro: fator diário %CDI não positivo — revise %CDI ou CDI."
    spread_over = fator_pct_cdi_1d - 1.0 - cdi_over
    spread_aa = _spread_over_para_anual(spread_over)
    f_du_pct = math.pow(fator_pct_cdi_1d, float(du))
    f_du_sp = math.pow(1.0 + cdi_over + spread_over, float(du))
    lines = [
        "%CDI → CDI+ (spread sobre CDI over, equivalência por dia útil)",
        "",
        "Passo 1 — CDI % a.a. → CDI over (1 du)",
        f"  CDI a.a. = {_fmt_num(cdi_aa, 6)}%",
        f"  CDI_over = (1 + CDI/100)^(1/252) - 1",
        f"  CDI_over = (1 + {_fmt_num(cdi_aa, 6)}/100)^(1/252) - 1 = {_fmt_num(cdi_over * 100.0, 8)}% (over em % do dia)",
        f"  (valor decimal over) = {_fmt_num(cdi_over, 10)}",
        "",
        "Passo 2 — Fator de 1 du no %CDI",
        f"  %CDI = {_fmt_num(pct_cdi, 6)}%  →  fator 1du = 1 + CDI_over × (%CDI/100)",
        f"  fator_1du = 1 + {_fmt_num(cdi_over, 10)} × ({_fmt_num(pct_cdi, 6)}/100) = {_fmt_num(fator_pct_cdi_1d, 10)}",
        "",
        "Passo 3 — Spread over que iguala o fator de 1 du",
        f"  CDI+ (1du): 1 + CDI_over + spread_over = fator_1du",
        f"  spread_over = fator_1du - 1 - CDI_over = {_fmt_num(spread_over * 100.0, 8)}% (over)",
        f"  (decimal) spread_over = {_fmt_num(spread_over, 10)}",
        "",
        "Passo 4 — Spread % a.a. equivalente (252 du, composto sobre o spread over)",
        f"  spread_a.a. = (1 + spread_over)^252 - 1  (em %)",
        f"  spread_a.a. = {_fmt_num(spread_aa, 6)}%",
        "",
        f"Passo 5 — Conferência em {du} du (deve coincidir)",
        f"  Fator %CDI: (fator_1du)^{du} = {_fmt_num(f_du_pct, 8)}",
        f"  Fator CDI+: (1 + CDI_over + spread_over)^{du} = {_fmt_num(f_du_sp, 8)}",
    ]
    return "\n".join(lines)


def cdi_spread_para_pct_cdi(spread_aa: float, cdi_aa: float, du: int = 252) -> str:
    """
    Inverso de pct_cdi_para_cdi_spread: spread % a.a. (sobre over) → %CDI.
    """
    if du < 0:
        return "Erro: du não pode ser negativo."
    cdi_over = _cdi_over_de_anual(cdi_aa)
    if abs(cdi_over) < 1e-16:
        return "Erro: CDI over ~0 — não dá para inverter %CDI por esta convenção."
    spread_over = _spread_anual_para_over(spread_aa)
    fator_1du = 1.0 + cdi_over + spread_over
    if fator_1du <= 0:
        return "Erro: fator 1 du CDI+ não positivo."
    pct_cdi = (fator_1du - 1.0) / cdi_over * 100.0
    f_du_pct = math.pow(1.0 + cdi_over * (pct_cdi / 100.0), float(du))
    f_du_sp = math.pow(fator_1du, float(du))
    lines = [
        "CDI+ (spread a.a. sobre over) → %CDI",
        "",
        "Passo 1 — CDI over e spread over",
        f"  CDI a.a. = {_fmt_num(cdi_aa, 6)}%",
        f"  CDI_over = {_fmt_num(cdi_over, 10)}",
        f"  spread a.a. = {_fmt_num(spread_aa, 6)}%",
        f"  spread_over = (1 + spread/100)^(1/252) - 1 = {_fmt_num(spread_over, 10)}",
        "",
        "Passo 2 — Fator 1 du CDI+ e %CDI implícito",
        f"  fator_1du = 1 + CDI_over + spread_over = {_fmt_num(fator_1du, 10)}",
        f"  %CDI = (fator_1du - 1) / CDI_over × 100 = {_fmt_num(pct_cdi, 6)}%",
        "",
        f"Passo 3 — Conferência em {du} du",
        f"  Fator %CDI: (1 + CDI_over×%CDI/100)^{du} = {_fmt_num(f_du_pct, 8)}",
        f"  Fator CDI+: (fator_1du)^{du} = {_fmt_num(f_du_sp, 8)}",
    ]
    return "\n".join(lines)


def pre_para_pct_cdi(taxa_pre_aa: float, cdi_aa: float) -> str:
    """
    Pré % a.a. → %CDI via equivalência pelo fator diário.

    Fator diário pré = (1 + pré/100)^(1/252).
    Fator diário CDI = 1 + CDI_over × (%CDI/100), onde CDI_over = (1+CDI/100)^(1/252) - 1.
    Igualando: %CDI = [(1+pré/100)^(1/252) - 1] / CDI_over × 100.
    """
    if abs(cdi_aa) < 1e-16:
        return "Erro: CDI não pode ser zero."
    cdi_over = math.pow(1.0 + cdi_aa / 100.0, 1.0 / 252.0) - 1.0
    if abs(cdi_over) < 1e-16:
        return "Erro: CDI over ~0 — não é possível calcular %CDI."
    fator_pre_dia = math.pow(1.0 + taxa_pre_aa / 100.0, 1.0 / 252.0) - 1.0
    pct = fator_pre_dia / cdi_over * 100.0
    # Conferência
    fator_check = math.pow(1.0 + cdi_over * (pct / 100.0), 252.0) - 1.0
    return "\n".join([
        "Pré % a.a. → %CDI (via fator diário)",
        "",
        f"  pré = {_fmt_num(taxa_pre_aa, 6)}% a.a.",
        f"  CDI = {_fmt_num(cdi_aa, 6)}% a.a.",
        f"  CDI_over = (1+CDI/100)^(1/252) - 1 = {_fmt_num(cdi_over * 100.0, 8)}% a.d.",
        f"  fator_dia_pré = (1+pré/100)^(1/252) - 1 = {_fmt_num(fator_pre_dia * 100.0, 8)}% a.d.",
        f"  %CDI = fator_dia_pré / CDI_over × 100 = {_fmt_num(pct, 6)}%",
        "",
        f"  Conferência: (1 + CDI_over × {_fmt_num(pct, 6)}%)^252 - 1 = {_fmt_num(fator_check * 100.0, 6)}% a.a.",
    ])


def pct_cdi_para_pre(pct_cdi: float, cdi_aa: float) -> str:
    """
    %CDI → pré % a.a. via fator diário.

    Fator diário %CDI = 1 + CDI_over × (%CDI/100).
    Pré equivalente = (fator_dia)^252 - 1.
    """
    cdi_over = math.pow(1.0 + cdi_aa / 100.0, 1.0 / 252.0) - 1.0
    fator_dia = 1.0 + cdi_over * (pct_cdi / 100.0)
    if fator_dia <= 0:
        return "Erro: fator diário não positivo — revise %CDI ou CDI."
    pre = (math.pow(fator_dia, 252.0) - 1.0) * 100.0
    return "\n".join([
        "%CDI → pré % a.a. (via fator diário)",
        "",
        f"  CDI = {_fmt_num(cdi_aa, 6)}% a.a.",
        f"  %CDI = {_fmt_num(pct_cdi, 6)}%",
        f"  CDI_over = (1+CDI/100)^(1/252) - 1 = {_fmt_num(cdi_over * 100.0, 8)}% a.d.",
        f"  fator_dia = 1 + CDI_over × (%CDI/100) = {_fmt_num(fator_dia, 10)}",
        f"  pré = (fator_dia)^252 - 1 = {_fmt_num(pre, 6)}% a.a.",
    ])


def pre_para_cdi_spread(taxa_pre_aa: float, cdi_aa: float) -> str:
    """
    Relação composta anual: (1+pré/100) = (1+CDI/100) × (1+spread/100).
    """
    den = 1.0 + cdi_aa / 100.0
    if den == 0:
        return "Erro: (1+CDI/100) não pode ser zero."
    spread = ((1.0 + taxa_pre_aa / 100.0) / den - 1.0) * 100.0
    return "\n".join([
        "Pré → spread CDI (composto anual)",
        "",
        "  (1 + pré/100) = (1 + CDI/100) × (1 + spread/100)",
        f"  pré = {_fmt_num(taxa_pre_aa, 6)}%  |  CDI = {_fmt_num(cdi_aa, 6)}%",
        f"  spread = ((1+pré/100)/(1+CDI/100) - 1) × 100 = {_fmt_num(spread, 6)}%",
        "",
        "Conferência:",
        f"  (1+CDI/100)×(1+spread/100) = {_fmt_num((1 + cdi_aa / 100.0) * (1 + spread / 100.0), 8)}",
        f"  1+pré/100 = {_fmt_num(1 + taxa_pre_aa / 100.0, 8)}",
    ])


def cdi_spread_para_pre(spread_aa: float, cdi_aa: float) -> str:
    """Pré % a.a. a partir de CDI e spread compostos."""
    pre = ((1.0 + cdi_aa / 100.0) * (1.0 + spread_aa / 100.0) - 1.0) * 100.0
    return "\n".join([
        "CDI + spread → pré % a.a. (composto anual)",
        "",
        f"  pré = ((1+CDI/100)×(1+spread/100) - 1) × 100",
        f"  CDI = {_fmt_num(cdi_aa, 6)}%  |  spread = {_fmt_num(spread_aa, 6)}%",
        f"  pré = {_fmt_num(pre, 6)}% a.a.",
    ])


def nominal_para_real(taxa_nominal_aa: float, ipca_aa: float) -> str:
    """Fisher: (1+real) = (1+nominal)/(1+IPCA)."""
    den = 1.0 + ipca_aa / 100.0
    if den == 0:
        return "Erro: (1+IPCA/100) não pode ser zero."
    real = ((1.0 + taxa_nominal_aa / 100.0) / den - 1.0) * 100.0
    return "\n".join([
        "Taxa nominal → real (Fisher), taxas em % a.a.",
        "",
        f"  (1 + real/100) = (1 + nominal/100) / (1 + IPCA/100)",
        f"  nominal = {_fmt_num(taxa_nominal_aa, 6)}%  |  IPCA = {_fmt_num(ipca_aa, 6)}%",
        f"  real = {_fmt_num(real, 6)}% a.a.",
    ])


def real_para_nominal(taxa_real_aa: float, ipca_aa: float) -> str:
    """Nominal a partir de real e IPCA (Fisher)."""
    nom = ((1.0 + taxa_real_aa / 100.0) * (1.0 + ipca_aa / 100.0) - 1.0) * 100.0
    return "\n".join([
        "Taxa real → nominal (Fisher), taxas em % a.a.",
        "",
        f"  (1 + nominal/100) = (1 + real/100) × (1 + IPCA/100)",
        f"  real = {_fmt_num(taxa_real_aa, 6)}%  |  IPCA = {_fmt_num(ipca_aa, 6)}%",
        f"  nominal = {_fmt_num(nom, 6)}% a.a.",
    ])


def exponencial_para_linear(taxa_exp_aa: float, du: int, dc: int) -> str:
    """
    Exponencial 252 du → linear 360/dc: mesmo fator no período.
    fator = (1 + taxa/100)^(du/252); taxa_linear = (fator - 1) × (360/dc) × 100.
    """
    if du == 0:
        return "Erro: du deve ser diferente de zero."
    if dc == 0:
        return "Erro: dc deve ser diferente de zero."
    base = 1.0 + taxa_exp_aa / 100.0
    if base <= 0:
        return "Erro: base (1+taxa/100) deve ser positiva."
    expo = du / 252.0
    fator = math.pow(base, expo)
    taxa_lin = (fator - 1.0) * (360.0 / float(dc)) * 100.0
    return "\n".join([
        "Exponencial (252 du) → linear (360, dc dias corridos no período)",
        "",
        f"  taxa exp = {_fmt_num(taxa_exp_aa, 6)}% a.a. (base 252)",
        f"  du = {du}  |  dc = {dc}",
        f"  fator período = (1 + taxa/100)^(du/252) = {_fmt_num(fator, 8)}",
        f"  taxa linear % = (fator - 1) × (360/dc) × 100 = {_fmt_num(taxa_lin, 6)}%",
    ])


def linear_para_exponencial(taxa_lin_aa: float, du: int, dc: int) -> str:
    """
    Linear 360/dc → exponencial 252 du.
    fator = 1 + taxa/100 × dc/360; taxa_exp = (fator^(252/du) - 1) × 100.
    """
    if du == 0:
        return "Erro: du deve ser diferente de zero."
    if dc == 0:
        return "Erro: dc deve ser diferente de zero."
    fator = 1.0 + (taxa_lin_aa / 100.0) * (float(dc) / 360.0)
    if fator <= 0:
        return "Erro: fator linear não positivo."
    expo = 252.0 / float(du)
    taxa_exp = (math.pow(fator, expo) - 1.0) * 100.0
    return "\n".join([
        "Linear (360, dc) → exponencial (252 du)",
        "",
        f"  taxa linear = {_fmt_num(taxa_lin_aa, 6)}% (sobre dc/360)",
        f"  du = {du}  |  dc = {dc}",
        f"  fator período = 1 + taxa/100 × dc/360 = {_fmt_num(fator, 8)}",
        f"  taxa exp % a.a. = (fator^(252/du) - 1) × 100 = {_fmt_num(taxa_exp, 6)}%",
    ])


def register(mcp: "FastMCP") -> None:
    """Registra as ferramentas deste módulo no servidor FastMCP."""

    @mcp.tool()
    def pct_cdi_para_cdi_spread_tool(pct_cdi: float, cdi_aa: float, du: int = 252) -> str:
        """%CDI → spread CDI+ (equivalência diária: fator %CDI vs CDI_over+spread_over)."""
        return pct_cdi_para_cdi_spread(pct_cdi, cdi_aa, du)

    @mcp.tool()
    def cdi_spread_para_pct_cdi_tool(spread_aa: float, cdi_aa: float, du: int = 252) -> str:
        """Spread CDI+ % a.a. (sobre over) → %CDI; inverso de pct_cdi_para_cdi_spread."""
        return cdi_spread_para_pct_cdi(spread_aa, cdi_aa, du)

    @mcp.tool()
    def pre_para_pct_cdi_tool(taxa_pre_aa: float, cdi_aa: float) -> str:
        """Pré % a.a. → %CDI pela razão (pré/CDI)×100."""
        return pre_para_pct_cdi(taxa_pre_aa, cdi_aa)

    @mcp.tool()
    def pct_cdi_para_pre_tool(pct_cdi: float, cdi_aa: float) -> str:
        """%CDI → pré % a.a. (pré = CDI × %CDI/100)."""
        return pct_cdi_para_pre(pct_cdi, cdi_aa)

    @mcp.tool()
    def pre_para_cdi_spread_tool(taxa_pre_aa: float, cdi_aa: float) -> str:
        """Pré → spread sobre CDI com (1+pré)=(1+CDI)(1+spread)."""
        return pre_para_cdi_spread(taxa_pre_aa, cdi_aa)

    @mcp.tool()
    def cdi_spread_para_pre_tool(spread_aa: float, cdi_aa: float) -> str:
        """CDI e spread compostos → pré % a.a."""
        return cdi_spread_para_pre(spread_aa, cdi_aa)

    @mcp.tool()
    def nominal_para_real_tool(taxa_nominal_aa: float, ipca_aa: float) -> str:
        """Nominal e IPCA → taxa real (Fisher)."""
        return nominal_para_real(taxa_nominal_aa, ipca_aa)

    @mcp.tool()
    def real_para_nominal_tool(taxa_real_aa: float, ipca_aa: float) -> str:
        """Real e IPCA → taxa nominal (Fisher)."""
        return real_para_nominal(taxa_real_aa, ipca_aa)

    @mcp.tool()
    def exponencial_para_linear_tool(taxa_exp_aa: float, du: int, dc: int) -> str:
        """Taxa exponencial 252 du → linear base 360 para dc dias corridos."""
        return exponencial_para_linear(taxa_exp_aa, du, dc)

    @mcp.tool()
    def linear_para_exponencial_tool(taxa_lin_aa: float, du: int, dc: int) -> str:
        """Taxa linear 360 (dc dias) → exponencial 252 du."""
        return linear_para_exponencial(taxa_lin_aa, du, dc)

    _ = (
        pct_cdi_para_cdi_spread_tool,
        cdi_spread_para_pct_cdi_tool,
        pre_para_pct_cdi_tool,
        pct_cdi_para_pre_tool,
        pre_para_cdi_spread_tool,
        cdi_spread_para_pre_tool,
        nominal_para_real_tool,
        real_para_nominal_tool,
        exponencial_para_linear_tool,
        linear_para_exponencial_tool,
    )
