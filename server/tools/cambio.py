"""
Ferramentas MCP para câmbio: NDF, cupom implícito, casado e arbitragem coberta.
Convencões: pré composto 252 du; cupom cambial linear base 360 dc.
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mcp.server.fastmcp import FastMCP


def _fmt(v: float, dec: int = 6) -> str:
    return f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calcular_ndf(
    spot: float,
    taxa_pre_aa: float,
    cupom_cambial_aa: float,
    du: int,
    dc: int,
) -> str:
    """
    Preço teórico de forward/NDF pela paridade coberta de juros.

    NDF = spot × (1 + taxa_pré/100)^(du/252) / (1 + (cupom_cambial_aa/100)×(dc/360)).
    """
    if spot <= 0 or du < 0 or dc <= 0:
        return "Erro: spot > 0, du ≥ 0 e dc > 0."

    num = spot * math.pow(1.0 + taxa_pre_aa / 100.0, du / 252.0)
    den = 1.0 + (cupom_cambial_aa / 100.0) * (dc / 360.0)
    ndf = num / den

    lines = [
        "=== NDF teórico (paridade coberta) ===",
        "",
        "Passo 1 — Numerador (lado BRL, pré 252 du)",
        f"  spot × (1 + pré/100)^(du/252) = {_fmt(spot, 4)} × (1 + {_fmt(taxa_pre_aa, 4)}/100)^{du/252}",
        f"  = {_fmt(num, 6)}",
        "",
        "Passo 2 — Denominador (cupom cambial linear 360 dc)",
        f"  1 + (cupom/100) × (dc/360) = 1 + ({_fmt(cupom_cambial_aa, 4)}/100)×({dc}/360)",
        f"  = {_fmt(den)}",
        "",
        "Passo 3 — NDF",
        f"  NDF = numerador / denominador = {_fmt(ndf, 6)}",
    ]
    return "\n".join(lines)


def calcular_cupom_cambial(
    spot: float,
    futuro: float,
    taxa_pre_aa: float,
    du: int,
    dc: int,
) -> str:
    """
    Cupom cambial implícito anual (%, linear 360) a partir de spot e futuro.

    cupom = [ (spot/futuro) × (1 + pré/100)^(du/252) − 1 ] × (360/dc) × 100.
    """
    if spot <= 0 or futuro <= 0 or dc <= 0:
        return "Erro: spot > 0, futuro > 0 e dc > 0."

    f_pre = math.pow(1.0 + taxa_pre_aa / 100.0, du / 252.0)
    ratio = spot / futuro
    inner = ratio * f_pre - 1.0
    cupom = inner * (360.0 / dc) * 100.0

    lines = [
        "=== Cupom cambial implícito ===",
        "",
        "Passo 1 — Fator pré",
        f"  (1 + pré/100)^(du/252) = {_fmt(f_pre)}",
        "",
        "Passo 2 — Termo (spot/futuro) × fator pré − 1",
        f"  spot/futuro = {_fmt(spot, 4)}/{_fmt(futuro, 4)} = {_fmt(ratio)}",
        f"  (spot/futuro) × fator_pré − 1 = {_fmt(inner)}",
        "",
        "Passo 3 — Anualizar em % linear 360 dc",
        f"  cupom_aa = {_fmt(inner)} × (360/{dc}) × 100 = {_fmt(cupom, 4)} % a.a. (linear 360)",
    ]
    return "\n".join(lines)


def calcular_casado(spot: float, futuro: float) -> str:
    """
    Pontos a termo e prêmio/desconto percentual.

    Diferença absoluta: futuro − spot.
    Convenção BRL por USD 1.000: pontos = (futuro − spot) × 1.000.
    """
    if spot <= 0:
        return "Erro: spot deve ser positivo."

    diff = futuro - spot
    pontos_1000 = diff * 1000.0
    pct = (futuro / spot - 1.0) * 100.0

    lines = [
        "=== Casado (spot vs futuro) ===",
        "",
        "Passo 1 — Diferença R$/USD",
        f"  futuro − spot = {_fmt(futuro, 4)} − {_fmt(spot, 4)} = {_fmt(diff, 4)}",
        "",
        "Passo 2 — Pontos por USD 1.000 (convenção pedida)",
        f"  (futuro − spot) × 1.000 = {_fmt(pontos_1000, 2)}",
        "",
        "Passo 3 — Prêmio (+) ou desconto (−) sobre o spot, em %",
        f"  (futuro/spot − 1) × 100 = {_fmt(pct, 4)} %",
    ]
    return "\n".join(lines)


def arbitragem_cambio_juros(
    spot: float,
    futuro: float,
    taxa_pre_aa: float,
    cupom_aa: float,
    du: int,
    dc: int,
) -> str:
    """
    Compara NDF teórico (paridade) com futuro de mercado e indica desvio.
    """
    if spot <= 0 or futuro <= 0 or dc <= 0 or du < 0:
        return "Erro: spot > 0, futuro > 0, du ≥ 0, dc > 0."

    ndf_teo = spot * math.pow(1.0 + taxa_pre_aa / 100.0, du / 252.0) / (
        1.0 + (cupom_aa / 100.0) * (dc / 360.0)
    )
    desvio = futuro - ndf_teo
    desvio_pct = (desvio / ndf_teo) * 100.0 if ndf_teo != 0 else float("nan")
    eps = max(1e-9, abs(ndf_teo) * 1e-6)

    lines = [
        "=== Arbitragem câmbio–juros (paridade vs mercado) ===",
        "",
        "Passo 1 — NDF teórico",
        f"  NDF_teo = {_fmt(ndf_teo, 6)}",
        "",
        "Passo 2 — Futuro de mercado",
        f"  Futuro = {_fmt(futuro, 6)}",
        "",
        "Passo 3 — Desvio",
        f"  Futuro − NDF_teo = {_fmt(desvio, 6)}  ({_fmt(desvio_pct, 4)} % do NDF teórico)",
        "",
        "Passo 4 — Leitura operacional (simplificada)",
    ]

    if abs(desvio) <= eps:
        lines.append("  Desvio desprezível: paridade aproximadamente satisfeita (sem oportunidade clara).")
    elif desvio > 0:
        lines.extend([
            "  Futuro > NDF_teo: o forward está caro vs a síntese pré/cupom.",
            "  Ideia: vender forward (ou equivalente) e montar a posição sintética mais barata",
            "  (comprar BRL barato no sintético / estrutura espelhando paridade), sujeito a custos e riscos.",
        ])
    else:
        lines.extend([
            "  Futuro < NDF_teo: o forward está barato vs a síntese.",
            "  Ideia: comprar forward e vender o sintético (lado oposto à linha acima), sujeito a custos e riscos.",
        ])

    return "\n".join(lines)


def ref_cambio() -> str:
    """Referência de conceitos de câmbio para tesouraria."""
    return "\n".join([
        "=== Referência — câmbio ===",
        "",
        "PTAX",
        "  Taxa de câmbio de referência; convenção usual D-1 para operações em BRL.",
        "",
        "Casado",
        "  Combinação spot + ajuste a termo (forward points) para formar o preço forward.",
        "  Pontos: diferença entre futuro e spot; aqui também em R$ por USD 1.000.",
        "",
        "NDF (non-deliverable forward)",
        "  Forward sem entrega física da moeda no vencimento; liquidação em BRL pela diferença.",
        "",
        "Cupom cambial",
        "  Cupom limpo: taxa linear sobre USD no período, base 360.",
        "  Cupom sujo: inclui efeitos de custos/spread e condições de mercado (não modelados nas fórmulas puras).",
        "",
        "Paridade coberta de juros (forma usada nas tools)",
        "  NDF ≈ spot × (1 + pré)^(du/252) / (1 + cupom×dc/360),",
        "  com pré em 252 du e cupom linear 360 dc.",
    ])


def register(mcp: "FastMCP") -> None:
    """Registra as ferramentas de câmbio no servidor FastMCP."""
    mcp.tool()(calcular_ndf)
    mcp.tool()(calcular_cupom_cambial)
    mcp.tool()(calcular_casado)
    mcp.tool()(arbitragem_cambio_juros)
    mcp.tool()(ref_cambio)
