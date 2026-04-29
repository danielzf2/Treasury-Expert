"""
Precificação de títulos de crédito privado: CDB (pré, %CDI, DI+spread).
Baseado em Mercado de Renda Fixa (cap 8.2.1) e Mercado Financeiro Assaf (cap 9.1).
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _fmt(v: float, dec: int = 6) -> str:
    neg = v < 0
    x = abs(v)
    s = f"{x:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"-{s}" if neg else s


def precificar_cdb(
    tipo: str,
    valor_face: float,
    taxa_ou_pct: float,
    du: int,
    cdi_aa: float = 0.0,
) -> str:
    """Precifica CDB em 3 modalidades.
    tipo = 'pre', 'pct_cdi' ou 'di_spread'.
    valor_face = valor de face / resgate (R$).
    taxa_ou_pct = taxa pré (% a.a.) OU %CDI OU spread DI+ (% a.a.), conforme tipo.
    du = dias úteis até o vencimento.
    cdi_aa = taxa CDI % a.a. (obrigatório para pct_cdi e di_spread).

    CDB Pré: PU = VF / (1 + taxa/100)^(du/252)
    CDB %CDI: fator_dia = 1 + CDI_over × (pct/100); PU = VF / fator_dia^du
    CDB DI+spread: PU = VF / [(1+CDI/100) × (1+spread/100)]^(du/252)"""

    t = tipo.strip().lower().replace(" ", "_").replace("-", "_")

    if t == "pre":
        r = taxa_ou_pct / 100.0
        fator = (1.0 + r) ** (du / 252.0)
        pu = valor_face / fator
        taxa_equiv = taxa_ou_pct

        lines = [
            "## CDB Prefixado",
            "",
            "**Premissas**",
            "",
            f"- Valor de face: R$ {_fmt(valor_face, 2)}",
            f"- Taxa: {_fmt(taxa_ou_pct, 4)}% a.a.",
            f"- DU: {du}",
            "",
            "**Fórmula**",
            "",
            "```",
            "PU = VF / (1 + taxa/100)^(du/252)",
            "```",
            "",
            f"PU = {_fmt(valor_face, 2)} / (1 + {_fmt(r, 6)})^({du}/252) = {_fmt(valor_face, 2)} / {_fmt(fator, 8)} = **R$ {_fmt(pu, 2)}**",
        ]

    elif t == "pct_cdi":
        if cdi_aa <= 0:
            return "Erro: informe cdi_aa para CDB %CDI."
        cdi_over = (1.0 + cdi_aa / 100.0) ** (1.0 / 252.0) - 1.0
        fator_dia = 1.0 + cdi_over * (taxa_ou_pct / 100.0)
        fator = fator_dia ** du
        pu = valor_face / fator
        taxa_equiv = (fator ** (252.0 / du) - 1.0) * 100.0

        lines = [
            f"## CDB {_fmt(taxa_ou_pct, 0)}% do CDI",
            "",
            "**Premissas**",
            "",
            f"- Valor de face: R$ {_fmt(valor_face, 2)}",
            f"- %CDI: {_fmt(taxa_ou_pct, 2)}%",
            f"- CDI: {_fmt(cdi_aa, 2)}% a.a.",
            f"- DU: {du}",
            "",
            "**Fórmula**",
            "",
            "```",
            "CDI_over = (1 + CDI/100)^(1/252) - 1",
            "fator_dia = 1 + CDI_over × (%CDI/100)",
            "PU = VF / fator_dia^du",
            "```",
            "",
            f"1) CDI_over = {_fmt(cdi_over, 8)}",
            f"2) fator_dia = 1 + {_fmt(cdi_over, 8)} × {_fmt(taxa_ou_pct / 100.0, 4)} = {_fmt(fator_dia, 10)}",
            f"3) fator = {_fmt(fator_dia, 10)}^{du} = {_fmt(fator, 8)}",
            f"4) PU = {_fmt(valor_face, 2)} / {_fmt(fator, 8)} = **R$ {_fmt(pu, 2)}**",
        ]

    elif t == "di_spread":
        if cdi_aa <= 0:
            return "Erro: informe cdi_aa para CDB DI+spread."
        spread = taxa_ou_pct
        fator_composto = (1.0 + cdi_aa / 100.0) * (1.0 + spread / 100.0)
        fator = fator_composto ** (du / 252.0)
        pu = valor_face / fator
        taxa_equiv = (fator_composto - 1.0) * 100.0

        lines = [
            f"## CDB DI + {_fmt(spread, 2)}% a.a.",
            "",
            "**Premissas**",
            "",
            f"- Valor de face: R$ {_fmt(valor_face, 2)}",
            f"- CDI: {_fmt(cdi_aa, 2)}% a.a.",
            f"- Spread: {_fmt(spread, 2)}% a.a.",
            f"- DU: {du}",
            "",
            "**Fórmula**",
            "",
            "```",
            "fator = [(1 + CDI/100) × (1 + spread/100)]^(du/252)",
            "PU = VF / fator",
            "```",
            "",
            f"1) fator anual = (1 + {_fmt(cdi_aa / 100.0, 4)}) × (1 + {_fmt(spread / 100.0, 4)}) = {_fmt(fator_composto, 8)}",
            f"2) fator = {_fmt(fator_composto, 8)}^({du}/252) = {_fmt(fator, 8)}",
            f"3) PU = {_fmt(valor_face, 2)} / {_fmt(fator, 8)} = **R$ {_fmt(pu, 2)}**",
        ]
    else:
        return "Erro: tipo deve ser 'pre', 'pct_cdi' ou 'di_spread'."

    lines += [
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| PU | **R$ {_fmt(pu, 2)}** |",
        f"| Valor de face | R$ {_fmt(valor_face, 2)} |",
        f"| Taxa equivalente a.a. | {_fmt(taxa_equiv, 4)}% |",
        f"| Rendimento bruto | R$ {_fmt(valor_face - pu, 2)} |",
    ]
    return "\n".join(lines)


def register(mcp: "FastMCP") -> None:
    mcp.tool()(precificar_cdb)
