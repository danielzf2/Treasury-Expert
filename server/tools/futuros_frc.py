"""
Ferramentas MCP para FRC (forward rate agreement de cupom cambial).
Convenção linear, base 360 dias corridos e face USD 50.000.
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


def pu_frc(cupom_cambial_aa: float, dc: int) -> str:
    """
    Calcula o PU do FRC a partir do cupom cambial % a.a. (linear, base 360 dc).

    PU = 50.000 / (1 + cupom/100 × dc/360)
    """
    if dc < 0:
        return "Erro: dc não pode ser negativo."
    if dc == 0:
        return "Erro: dc = 0 deixa a convenção linear indefinida; use dc > 0."
    den = 1.0 + (cupom_cambial_aa / 100.0) * (dc / 360.0)
    if den == 0:
        return "Erro: denominador não pode ser zero."
    pu = 50_000.0 / den
    juros_linear = (cupom_cambial_aa / 100.0) * (dc / 360.0)
    lines = [
        "FRC — PU a partir do cupom cambial (linear, base 360 dc)",
        "",
        "Passo 1 — Parâmetros",
        f"  Face de referência: USD 50.000,00",
        f"  Cupom cambial (a.a. linear 360): {_fmt_num(cupom_cambial_aa, 6)}%",
        f"  Prazo: {dc} dias corridos",
        "",
        "Passo 2 — Juros linear no período",
        f"  juros_dc = (cupom/100) × (dc/360)",
        f"  juros_dc = ({_fmt_num(cupom_cambial_aa, 6)}/100) × ({dc}/360) = {_fmt_num(juros_linear, 8)}",
        "",
        "Passo 3 — Denominador e PU",
        f"  1 + juros_dc = {_fmt_num(den, 8)}",
        f"  PU = 50.000 / (1 + juros_dc) = 50.000 / {_fmt_num(den, 8)}",
        f"  PU = {_fmt_num(pu, 6)}",
        "",
        "Obs.: diferente do DI futuro — DI usa exponencial base 252 du; FRC usa linear 360 dc.",
    ]
    return "\n".join(lines)


def taxa_frc(pu: float, dc: int) -> str:
    """
    Cupom cambial % a.a. (linear 360) a partir do PU.

    cupom = (50.000/PU - 1) × (360/dc) × 100
    """
    if dc <= 0:
        return "Erro: dc deve ser positivo."
    if pu <= 0:
        return "Erro: PU deve ser positivo."
    razao = 50_000.0 / pu
    cupom = (razao - 1.0) * (360.0 / dc) * 100.0
    lines = [
        "FRC — Cupom cambial implícito a partir do PU (linear 360)",
        "",
        "Passo 1 — Parâmetros",
        f"  PU: {_fmt_num(pu, 6)}",
        f"  dc: {dc}",
        "",
        "Passo 2 — Razão",
        f"  50.000/PU = 50.000 / {_fmt_num(pu, 6)} = {_fmt_num(razao, 8)}",
        "",
        "Passo 3 — Cupom % a.a.",
        f"  cupom = (50.000/PU - 1) × (360/dc) × 100",
        f"  cupom = ({_fmt_num(razao, 8)} - 1) × (360/{dc}) × 100",
        f"  cupom = {_fmt_num(cupom, 6)}% a.a. (linear, base 360 dc)",
    ]
    return "\n".join(lines)


def fra_cupom_cambial(
    cupom_curto: float,
    dc_curto: int,
    cupom_longo: float,
    dc_longo: int,
) -> str:
    """
    Cupom cambial forward (FRA) entre dois vértices, linear 360.

    (1 + cc_longo×dc_longo/360) = (1 + cc_curto×dc_curto/360) × (1 + FRA×(dc_longo-dc_curto)/360)
    com cc em decimal = cupom/100.
    """
    delta = dc_longo - dc_curto
    if delta == 0:
        return "Erro: dc_longo deve ser diferente de dc_curto para definir o FRA."
    cc_c = cupom_curto / 100.0
    cc_l = cupom_longo / 100.0
    fator_curto = 1.0 + cc_c * (dc_curto / 360.0)
    fator_longo = 1.0 + cc_l * (dc_longo / 360.0)
    if fator_curto == 0:
        return "Erro: fator curto nulo (combinação inválida de cupom e dc)."
    ratio = fator_longo / fator_curto
    fra = (ratio - 1.0) * (360.0 / delta) * 100.0
    lines = [
        "FRC — Cupom cambial forward (FRA) entre dois prazos (linear 360)",
        "",
        "Passo 1 — Parâmetros (% a.a. linear 360)",
        f"  Cupom curto: {_fmt_num(cupom_curto, 6)}%  |  dc_curto: {dc_curto}",
        f"  Cupom longo: {_fmt_num(cupom_longo, 6)}%  |  dc_longo: {dc_longo}",
        f"  Δdc = dc_longo - dc_curto = {delta}",
        "",
        "Passo 2 — Fatores de capitalização linear",
        f"  F_curto = 1 + (cupom_curto/100)×(dc_curto/360) = {_fmt_num(fator_curto, 8)}",
        f"  F_longo = 1 + (cupom_longo/100)×(dc_longo/360) = {_fmt_num(fator_longo, 8)}",
        "",
        "Passo 3 — Implied forward",
        f"  F_longo = F_curto × (1 + FRA×Δdc/360)",
        f"  1 + FRA×Δdc/360 = F_longo/F_curto = {_fmt_num(ratio, 8)}",
        f"  FRA = (F_longo/F_curto - 1) × (360/Δdc) × 100",
        f"  FRA = {_fmt_num(fra, 6)}% a.a. (linear, sobre {delta} dc, base 360)",
    ]
    return "\n".join(lines)


def ref_frc() -> str:
    """Texto de referência rápida sobre o contrato FRC."""
    return "\n".join([
        "FRC — referência",
        "",
        "• FRC vs DDI: DDI negocia cupom “sujo” (com embarque); FRC isola cupom cambial “limpo”",
        "  (sem o efeito do prêmio de embarque embutido no DDI).",
        "• Cotação: taxa linear % a.a., base 360 dias corridos (não exponencial 252 du).",
        "• Face: USD 50.000,00; na prática o notional efetivo em dólar costuma ser interpretado",
        "  com o fator 0,5 sobre o PU conforme especificação do contrato (PU × 0,5).",
        "• Vencimento: primeiro dia útil do mês (calendário B3; conferir série/regulamento).",
        "• Relação com DOL e DI: cupom cambial combina expectativa de câmbio, juros USD/BRL e",
        "  prêmios; operações “casadas” costumam amarrar FRC/DDI com DOL e pontos da curva DI.",
    ])


def register(mcp: "FastMCP") -> None:
    """Registra as ferramentas deste módulo no servidor FastMCP."""

    mcp.tool(name="pu_frc")(pu_frc)
    mcp.tool(name="taxa_frc")(taxa_frc)
    mcp.tool(name="fra_cupom_cambial")(fra_cupom_cambial)
    mcp.tool(name="ref_frc")(ref_frc)
