"""
Ferramentas MCP para swaps de taxa de juros e indexadores.
Convencões: pré composto 252 du; cupom cambial linear 360 dc (onde aplicável).
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mcp.server.fastmcp import FastMCP


def _fmt(v: float, dec: int = 6) -> str:
    return f"{v:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def swap_pre_di(nocional: float, taxa_pre_aa: float, du: int, cdi_acumulado: float) -> str:
    """
    Compara as pontas de um swap pré x CDI no vencimento (valor futuro por notional).

    Ponta pré: nocional × (1 + taxa_pré/100)^(du/252).
    Ponta DI: nocional × (1 + CDI_acumulado/100).
    """
    if nocional < 0 or du < 0:
        return "Erro: nocional e du devem ser não negativos."

    exp = du / 252.0
    fator_pre = math.pow(1.0 + taxa_pre_aa / 100.0, exp)
    fator_di = 1.0 + cdi_acumulado / 100.0

    ponta_pre = nocional * fator_pre
    ponta_di = nocional * fator_di
    diff_pre_menos_di = ponta_pre - ponta_di
    diff_di_menos_pre = ponta_di - ponta_pre

    lines = [
        "=== Swap pré × CDI (valores no horizonte du) ===",
        "",
        "Passo 1 — Fator pré (composto 252 du)",
        f"  (1 + taxa_pré/100)^(du/252) = (1 + {_fmt(taxa_pre_aa, 4)}/100)^{du/252}",
        f"  = {_fmt(fator_pre)}",
        "",
        "Passo 2 — Fator CDI acumulado",
        f"  (1 + CDI_acum/100) = 1 + {_fmt(cdi_acumulado, 4)}/100 = {_fmt(fator_di)}",
        "",
        "Passo 3 — Pontas em valor monetário",
        f"  Ponta pré = nocional × fator_pré = {_fmt(nocional, 2)} × {_fmt(fator_pre)} = {_fmt(ponta_pre, 2)}",
        f"  Ponta DI  = nocional × fator_DI  = {_fmt(nocional, 2)} × {_fmt(fator_di)} = {_fmt(ponta_di, 2)}",
        "",
        "Passo 4 — Resultado líquido (quem recebe o quê)",
        "  Perspectiva A — recebe pré e paga CDI (ativo da perna pré):",
        f"    pré − DI = {_fmt(ponta_pre, 2)} − {_fmt(ponta_di, 2)} = {_fmt(diff_pre_menos_di, 2)}",
        "  Perspectiva B — recebe CDI e paga pré (passivo da perna pré):",
        f"    DI − pré = {_fmt(ponta_di, 2)} − {_fmt(ponta_pre, 2)} = {_fmt(diff_di_menos_pre, 2)}",
        "",
        "Interpretação: o sinal favorável depende de qual perna você recebe.",
    ]
    return "\n".join(lines)


def swap_cambial(
    nocional_usd: float,
    ptax_inicio: float,
    ptax_fim: float,
    cupom_aa: float,
    taxa_pre_aa: float,
    du: int,
    dc: int,
) -> str:
    """
    Swap cambial (dólar cupom linear) × pré (BRL, 252 du).

    Ponta cambial: nocional_USD × PTAX_início × (PTAX_fim/PTAX_início) × (1 + cupom×dc/360)
      = nocional_USD × PTAX_fim × (1 + cupom×dc/360).

    Ponta DI (BRL na entrada): nocional_USD × PTAX_início × (1 + taxa_pré/100)^(du/252).
    """
    if nocional_usd < 0 or ptax_inicio <= 0 or ptax_fim <= 0 or du < 0 or dc <= 0:
        return "Erro: verifique nocional ≥ 0, PTAX > 0, du ≥ 0 e dc > 0."

    ratio_ptax = ptax_fim / ptax_inicio
    fator_cupom = 1.0 + (cupom_aa / 100.0) * (dc / 360.0)
    fator_pre = math.pow(1.0 + taxa_pre_aa / 100.0, du / 252.0)

    ponta_cambial = nocional_usd * ptax_inicio * ratio_ptax * fator_cupom
    ponta_di_brl = nocional_usd * ptax_inicio * fator_pre

    diff_cambial_menos_di = ponta_cambial - ponta_di_brl
    diff_di_menos_cambial = ponta_di_brl - ponta_cambial

    lines = [
        "=== Swap cambial × pré (BRL) ===",
        "",
        "Passo 1 — Variação cambial embutida",
        f"  PTAX_fim / PTAX_início = {_fmt(ptax_fim, 4)} / {_fmt(ptax_inicio, 4)} = {_fmt(ratio_ptax)}",
        "",
        "Passo 2 — Fator cupom (linear, base 360 dc)",
        f"  1 + (cupom_aa/100) × (dc/360) = 1 + ({_fmt(cupom_aa, 4)}/100)×({dc}/360) = {_fmt(fator_cupom)}",
        "",
        "Passo 3 — Fator pré (252 du)",
        f"  (1 + taxa_pré/100)^(du/252) = {_fmt(fator_pre)}",
        "",
        "Passo 4 — Ponta cambial (BRL no vencimento, convenção pedida)",
        "  nocional_USD × PTAX_início × (PTAX_fim/PTAX_início) × (1 + cupom×dc/360)",
        f"  = {_fmt(nocional_usd, 2)} × {_fmt(ptax_inicio, 4)} × {_fmt(ratio_ptax)} × {_fmt(fator_cupom)}",
        f"  = {_fmt(ponta_cambial, 2)}",
        "",
        "Passo 5 — Ponta pré em BRL (âncora PTAX_início)",
        "  nocional_USD × PTAX_início × (1 + taxa_pré/100)^(du/252)",
        f"  = {_fmt(nocional_usd, 2)} × {_fmt(ptax_inicio, 4)} × {_fmt(fator_pre)}",
        f"  = {_fmt(ponta_di_brl, 2)}",
        "",
        "Passo 6 — Líquido nas duas perspectivas",
        "  Quem recebe cambial e paga pré:",
        f"    cambial − pré = {_fmt(diff_cambial_menos_di, 2)}",
        "  Quem recebe pré e paga cambial:",
        f"    pré − cambial = {_fmt(diff_di_menos_cambial, 2)}",
    ]
    return "\n".join(lines)


def swap_ipca(
    nocional: float,
    taxa_real_aa: float,
    ipca_acumulado: float,
    cdi_acumulado: float,
    du: int,
) -> str:
    """
    Swap IPCA+ (real) × CDI: compara valor indexado IPCA+ com perna CDI acumulado.
    """
    if nocional < 0 or du < 0:
        return "Erro: nocional e du devem ser não negativos."

    exp = du / 252.0
    fator_real = math.pow(1.0 + taxa_real_aa / 100.0, exp)
    fator_ipca = 1.0 + ipca_acumulado / 100.0
    fator_cdi = 1.0 + cdi_acumulado / 100.0

    ponta_ipca = nocional * fator_ipca * fator_real
    ponta_di = nocional * fator_cdi
    diff_ipca_menos_di = ponta_ipca - ponta_di
    diff_di_menos_ipca = ponta_di - ponta_ipca

    lines = [
        "=== Swap IPCA+ × CDI ===",
        "",
        "Passo 1 — Fator IPCA acumulado",
        f"  1 + IPCA_acum/100 = {_fmt(fator_ipca)}",
        "",
        "Passo 2 — Fator real (252 du)",
        f"  (1 + taxa_real/100)^(du/252) = {_fmt(fator_real)}",
        "",
        "Passo 3 — Ponta IPCA+",
        f"  nocional × (1+IPCA_acum/100) × (1+taxa_real/100)^(du/252)",
        f"  = {_fmt(nocional, 2)} × {_fmt(fator_ipca)} × {_fmt(fator_real)} = {_fmt(ponta_ipca, 2)}",
        "",
        "Passo 4 — Ponta CDI",
        f"  nocional × (1 + CDI_acum/100) = {_fmt(ponta_di, 2)}",
        "",
        "Passo 5 — Resultado",
        "  Quem recebe IPCA+ e paga CDI:",
        f"    IPCA+ − CDI = {_fmt(diff_ipca_menos_di, 2)}",
        "  Quem recebe CDI e paga IPCA+:",
        f"    CDI − IPCA+ = {_fmt(diff_di_menos_ipca, 2)}",
    ]
    return "\n".join(lines)


def mtm_swap_pre(
    nocional: float,
    taxa_original_aa: float,
    taxa_mercado_aa: float,
    du_restante: int,
) -> str:
    """
    Marcação a mercado simplificada de swap pré: compara valor presente do principal
    descontado à taxa de mercado vs taxa original, para os du restantes.

    Observação: a forma completa com fator (1+taxa_original)^(du_original/252) exige
    du_original (prazo total do contrato); aqui usamos apenas du_restante para o
    núcleo PV×(DF_mercado − DF_original).
    """
    if nocional < 0 or du_restante < 0:
        return "Erro: nocional ≥ 0 e du_restante ≥ 0."

    exp = du_restante / 252.0
    df_mercado = 1.0 / math.pow(1.0 + taxa_mercado_aa / 100.0, exp)
    df_original = 1.0 / math.pow(1.0 + taxa_original_aa / 100.0, exp)

    pv_mercado = nocional * df_mercado
    pv_original = nocional * df_original
    mtm_core = nocional * (df_mercado - df_original)

    lines = [
        "=== MtM swap pré (visão simplificada — desconto do principal) ===",
        "",
        "Passo 1 — Fatores de desconto (252 du, du = du_restante)",
        f"  DF_mercado  = 1/(1 + taxa_mercado/100)^(du/252) = {_fmt(df_mercado)}",
        f"  DF_original = 1/(1 + taxa_original/100)^(du/252) = {_fmt(df_original)}",
        "",
        "Passo 2 — Valor presente do nocional (curva mercado)",
        f"  PV @ mercado = nocional × DF_mercado = {_fmt(pv_mercado, 2)}",
        "",
        "Passo 3 — Valor presente do nocional (curva taxa original)",
        f"  PV @ taxa original = nocional × DF_original = {_fmt(pv_original, 2)}",
        "",
        "Passo 4 — Diferença (proxy de MtM da perna fixa puramente descontada)",
        f"  nocional × (DF_mercado − DF_original) = {_fmt(mtm_core, 2)}",
        "",
        "Nota: em operações reais entram fluxos de cupom, convexidade e curva completa;",
        "o fator (1+taxa_original)^(du_original/252) da fórmula estendida pede du_original.",
    ]
    return "\n".join(lines)


def ref_swaps() -> str:
    """Texto de referência rápida sobre swaps usuais no Brasil."""
    return "\n".join([
        "=== Referência — swaps ===",
        "",
        "1) Swap pré × CDI",
        "   Pontas: ativa/passiva conforme contrato (recebe pré ou recebe CDI).",
        "   Pré: exponencial 252 du — (1 + i_pré)^(du/252).",
        "   CDI: acumulado do período — (1 + CDI_acum).",
        "   Uso típico: trocar exposição CDI por taxa fixa ou o inverso; hedge de funding.",
        "",
        "2) Swap DI × dólar (cambial)",
        "   Pontas: perna cambial (cupom linear 360 dc sobre USD indexada ao câmbio) vs pré em BRL.",
        "   Cambial: nocional em USD ajustado por PTAX e fator (1 + cupom×dc/360).",
        "   Pré: BRL com (1 + pré)^(du/252), usualmente ancorado em PTAX de entrada.",
        "   Uso típico: hedge cambial + juros; alinhar passivo em USD com ativo em CDI/pré.",
        "",
        "3) Swap DI × IPCA+",
        "   Pontas: CDI acumulado vs IPCA acumulado × (1 + taxa_real)^(du/252).",
        "   Convenções: real em 252 du; IPCA como fator de atualização do principal.",
        "   Uso típico: proteger ou assumir inflação vs CDI; dívida indexada.",
    ])


def register(mcp: "FastMCP") -> None:
    """Registra as ferramentas de swap no servidor FastMCP."""
    mcp.tool()(swap_pre_di)
    mcp.tool()(swap_cambial)
    mcp.tool()(swap_ipca)
    mcp.tool()(mtm_swap_pre)
    mcp.tool()(ref_swaps)
