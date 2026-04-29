"""
Estratégias de renda fixa: butterfly de DI e total return.
Baseado em O Mercado de Renda Fixa no Brasil (apêndice A.8)
e conceitos de retorno total de carteira.
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _fmt(v: float, dec: int = 2) -> str:
    neg = v < 0
    x = abs(v)
    s = f"{x:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"-{s}" if neg else s


def butterfly_di(
    taxa1_aa: float,
    du1: int,
    taxa2_aa: float,
    du2: int,
    taxa3_aa: float,
    du3: int,
    qtd3: int = 1000,
) -> str:
    """Butterfly (fly de 3 pontas) com contratos futuros de DI.
    Estratégia duration-neutra e autofinanciada.
    taxa1_aa, du1 = vértice curto (% a.a., du).
    taxa2_aa, du2 = vértice intermediário (barriga).
    taxa3_aa, du3 = vértice longo.
    qtd3 = quantidade de referência do vértice longo (default 1000).

    Restrições: D1×Q1 + D2×Q2 + D3×Q3 = 0 (duration neutra)
                PU1×Q1 + PU2×Q2 + PU3×Q3 = 0 (autofinanciada)
    Solução por Kramer conforme Mercado de Renda Fixa apêndice A.8."""

    r1, r2, r3 = taxa1_aa / 100.0, taxa2_aa / 100.0, taxa3_aa / 100.0

    pu1 = 100_000.0 / (1.0 + r1) ** (du1 / 252.0)
    pu2 = 100_000.0 / (1.0 + r2) ** (du2 / 252.0)
    pu3 = 100_000.0 / (1.0 + r3) ** (du3 / 252.0)

    d1 = (du1 / 252.0) / (1.0 + r1)
    d2 = (du2 / 252.0) / (1.0 + r2)
    d3 = (du3 / 252.0) / (1.0 + r3)

    det = d1 * pu2 - pu1 * d2
    if abs(det) < 1e-12:
        return "Erro: sistema indeterminado (vértices colineares)."

    q1 = qtd3 * (d2 * pu3 - d3 * pu2) / det
    q2 = qtd3 * (d3 * pu1 - d1 * pu3) / det
    q3_f = float(qtd3)

    dv01_1 = d1 * pu1 * abs(q1) / 10000.0
    dv01_2 = d2 * pu2 * abs(q2) / 10000.0
    dv01_3 = d3 * pu3 * abs(q3_f) / 10000.0

    mtm = pu1 * q1 + pu2 * q2 + pu3 * q3_f
    dur_net = d1 * q1 + d2 * q2 + d3 * q3_f

    if q2 > 0:
        interpretacao = "Compra barriga (vértice 2) + vende pontas → aposta em **achatamento** da curvatura"
    else:
        interpretacao = "Vende barriga (vértice 2) + compra pontas → aposta em **aumento** da curvatura"

    lines = [
        "## Butterfly de DI — Fly de 3 Pontas",
        "",
        "**Premissas**",
        "",
        "| Vértice | DU | Taxa (% a.a.) | PU | Dmod (anos) |",
        "|---|---|---|---|---|",
        f"| Curto (1) | {du1} | {_fmt(taxa1_aa, 4)} | {_fmt(pu1)} | {_fmt(d1, 4)} |",
        f"| Barriga (2) | {du2} | {_fmt(taxa2_aa, 4)} | {_fmt(pu2)} | {_fmt(d2, 4)} |",
        f"| Longo (3) | {du3} | {_fmt(taxa3_aa, 4)} | {_fmt(pu3)} | {_fmt(d3, 4)} |",
        "",
        f"Quantidade de referência (vértice longo): {qtd3}",
        "",
        "**Restrições**",
        "",
        "```",
        "D1×Q1 + D2×Q2 + D3×Q3 = 0   (duration neutra)",
        "PU1×Q1 + PU2×Q2 + PU3×Q3 = 0 (autofinanciada)",
        "```",
        "",
        "**Resultado**",
        "",
        "| Vértice | Quantidade | Posição | DV01 |",
        "|---|---|---|---|",
        f"| Curto (du={du1}) | **{_fmt(q1, 0)}** | {'comprado' if q1 > 0 else 'vendido'} | {_fmt(dv01_1)} |",
        f"| Barriga (du={du2}) | **{_fmt(q2, 0)}** | {'comprado' if q2 > 0 else 'vendido'} | {_fmt(dv01_2)} |",
        f"| Longo (du={du3}) | **{_fmt(q3_f, 0)}** | {'comprado' if q3_f > 0 else 'vendido'} | {_fmt(dv01_3)} |",
        "",
        f"- MtM líquido: R$ {_fmt(mtm)} (deve ser ~0)",
        f"- Duration líquida: {_fmt(dur_net, 6)} (deve ser ~0)",
        "",
        f"**Interpretação**: {interpretacao}",
    ]
    return "\n".join(lines)


def total_return(
    pu_inicio: float,
    pu_fim: float,
    cupons_recebidos: float = 0.0,
    du: int = 1,
    cdi_aa: float = 0.0,
) -> str:
    """Retorno total de posição em título de renda fixa entre duas datas.
    pu_inicio = PU na compra.
    pu_fim = PU na venda/marcação.
    cupons_recebidos = soma dos cupons recebidos no período (default 0).
    du = dias úteis entre as duas datas.
    cdi_aa = CDI % a.a. para cálculo do excess return (default 0 = não calcula).

    TR = (PU_fim + cupons) / PU_inicio - 1
    TR_aa = (1 + TR)^(252/du) - 1"""

    tr = (pu_fim + cupons_recebidos) / pu_inicio - 1.0
    tr_pct = tr * 100.0
    tr_aa = (1.0 + tr) ** (252.0 / du) - 1.0 if du > 0 else 0.0
    tr_aa_pct = tr_aa * 100.0

    lines = [
        "## Total Return — Retorno Total",
        "",
        "**Premissas**",
        "",
        f"- PU início: R$ {_fmt(pu_inicio)}",
        f"- PU fim: R$ {_fmt(pu_fim)}",
        f"- Cupons recebidos: R$ {_fmt(cupons_recebidos)}",
        f"- DU no período: {du}",
        "",
        "**Fórmula**",
        "",
        "```",
        "TR = (PU_fim + cupons) / PU_inicio - 1",
        "TR_aa = (1 + TR)^(252/du) - 1",
        "```",
        "",
        "**Cálculo**",
        "",
        f"1) TR = ({_fmt(pu_fim)} + {_fmt(cupons_recebidos)}) / {_fmt(pu_inicio)} - 1 = **{_fmt(tr_pct, 4)}%**",
        f"2) TR a.a. = (1 + {_fmt(tr_pct, 4)}%)^(252/{du}) - 1 = **{_fmt(tr_aa_pct, 4)}%**",
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| Retorno total (período) | **{_fmt(tr_pct, 4)}%** |",
        f"| Retorno total (a.a.) | **{_fmt(tr_aa_pct, 4)}%** |",
        f"| Ganho absoluto | R$ {_fmt(pu_fim + cupons_recebidos - pu_inicio)} |",
    ]

    if cdi_aa > 0:
        cdi_periodo = (1.0 + cdi_aa / 100.0) ** (du / 252.0) - 1.0
        excess = tr - cdi_periodo
        excess_pct = excess * 100.0
        excess_aa = tr_aa - cdi_aa / 100.0
        excess_aa_pct = excess_aa * 100.0
        lines += [
            f"| CDI no período | {_fmt(cdi_periodo * 100, 4)}% |",
            f"| Excess return (período) | **{_fmt(excess_pct, 4)}%** |",
            f"| CDI a.a. | {_fmt(cdi_aa, 4)}% |",
            f"| Excess return (a.a.) | **{_fmt(excess_aa_pct, 4)}%** |",
        ]

    return "\n".join(lines)


def register(mcp: "FastMCP") -> None:
    mcp.tool()(butterfly_di)
    mcp.tool()(total_return)
