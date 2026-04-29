"""
Ferramentas MCP para DAP (cupom IPCA futuro).
Precificação em base exponencial 252 dias úteis e face R$ 100.000.
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


def pu_dap(cupom_ipca_aa: float, du: int) -> str:
    """
    Calcula o PU do DAP a partir do cupom IPCA % a.a. (base 252, exponencial).

    PU = 100.000 / (1 + cupom/100)^(du/252)
    """
    if du < 0:
        return "Erro: du não pode ser negativo."
    base = 1.0 + cupom_ipca_aa / 100.0
    if base <= 0:
        return "Erro: (1 + cupom/100) deve ser positivo."
    expo = du / 252.0
    fator = math.pow(base, expo)
    pu = 100_000.0 / fator
    lines = [
        "DAP — PU a partir do cupom IPCA (% a.a., base 252 du, exponencial)",
        "",
        "Passo 1 — Parâmetros",
        f"  Face (VN): R$ 100.000,00",
        f"  Cupom IPCA (a.a.): {_fmt_num(cupom_ipca_aa, 6)}%",
        f"  Prazo: {du} du",
        "",
        "Passo 2 — Fator de desconto",
        f"  base = 1 + cupom/100 = 1 + ({_fmt_num(cupom_ipca_aa, 6)} / 100) = {_fmt_num(base, 8)}",
        f"  expoente = du/252 = {du}/252 = {_fmt_num(expo, 8)}",
        f"  fator = base^expoente = {_fmt_num(fator, 8)}",
        "",
        "Passo 3 — PU",
        f"  PU = 100.000 / fator = 100.000 / {_fmt_num(fator, 8)}",
        f"  PU = {_fmt_num(pu, 6)}",
    ]
    return "\n".join(lines)


def taxa_dap(pu: float, du: int) -> str:
    """
    Cupom IPCA implícito % a.a. a partir do PU (inverso de pu_dap, base 252).

    cupom = ((100.000/PU)^(252/du) - 1) × 100
    """
    if du <= 0:
        return "Erro: du deve ser positivo para inverter a taxa."
    if pu <= 0:
        return "Erro: PU deve ser positivo."
    razao = 100_000.0 / pu
    expo = 252.0 / du
    base = math.pow(razao, expo)
    cupom = (base - 1.0) * 100.0
    lines = [
        "DAP — Cupom IPCA implícito a partir do PU",
        "",
        "Passo 1 — Parâmetros",
        f"  PU: {_fmt_num(pu, 6)}",
        f"  Prazo: {du} du",
        "",
        "Passo 2 — Razão e expoente",
        f"  100.000/PU = 100.000 / {_fmt_num(pu, 6)} = {_fmt_num(razao, 8)}",
        f"  expoente = 252/du = 252/{du} = {_fmt_num(expo, 8)}",
        "",
        "Passo 3 — Cupom % a.a.",
        f"  (100.000/PU)^(252/du) = {_fmt_num(base, 8)}",
        f"  cupom = (base - 1) × 100 = {_fmt_num(cupom, 6)}% a.a. (base 252, exponencial)",
    ]
    return "\n".join(lines)


def ajuste_dap(
    pu_anterior: float,
    pu_ajuste: float,
    cdi_dia: float,
    ipca_dia: float,
    qtd: int,
) -> str:
    """
    Ajuste financeiro do DAP: corrige o PA anterior por CDI/IPCA e compara ao PA de ajuste.

    PA_corrigido = PA_anterior × (1+CDI)^(1/252) / (1+IPCA_dia)
    AJ = (PA_ajuste - PA_corrigido) × qtd
    """
    if pu_anterior <= 0 or pu_ajuste <= 0:
        return "Erro: PU anterior e PU de ajuste devem ser positivos."
    if 1.0 + ipca_dia == 0:
        return "Erro: (1 + IPCA_dia) não pode ser zero."
    fator_cdi = math.pow(1.0 + cdi_dia, 1.0 / 252.0)
    pa_corrigido = pu_anterior * fator_cdi / (1.0 + ipca_dia)
    aj = (pu_ajuste - pa_corrigido) * qtd
    lines = [
        "DAP — Ajuste (correção CDI/IPCA e variação × quantidade)",
        "",
        "Passo 1 — Entradas (PA = preço de ajuste / PU do contrato)",
        f"  PA_anterior: {_fmt_num(pu_anterior, 6)}",
        f"  PA_ajuste (do dia): {_fmt_num(pu_ajuste, 6)}",
        f"  CDI (taxa em decimal para (1+CDI)^(1/252)): {_fmt_num(cdi_dia, 8)}",
        f"  IPCA_dia (variação em decimal, denominador 1+IPCA_dia): {_fmt_num(ipca_dia, 8)}",
        f"  Quantidade (contratos/lotes): {qtd}",
        "",
        "Passo 2 — Fator CDI em 1 du",
        f"  (1 + CDI)^(1/252) = (1 + {_fmt_num(cdi_dia, 8)})^(1/252) = {_fmt_num(fator_cdi, 8)}",
        "",
        "Passo 3 — PA corrigido",
        f"  PA_corrigido = PA_anterior × (1+CDI)^(1/252) / (1+IPCA_dia)",
        f"  PA_corrigido = {_fmt_num(pu_anterior, 6)} × {_fmt_num(fator_cdi, 8)} / (1 + {_fmt_num(ipca_dia, 8)})",
        f"  PA_corrigido = {_fmt_num(pa_corrigido, 6)}",
        "",
        "Passo 4 — Ajuste financeiro",
        f"  AJ = (PA_ajuste - PA_corrigido) × qtd",
        f"  AJ = ({_fmt_num(pu_ajuste, 6)} - {_fmt_num(pa_corrigido, 6)}) × {qtd}",
        f"  AJ = {_fmt_num(aj, 2)} (mesma unidade monetária do PA × qtd)",
    ]
    return "\n".join(lines)


def ref_dap() -> str:
    """Texto de referência rápida sobre o contrato DAP."""
    return "\n".join([
        "DAP — referência",
        "",
        "• Objeto: exposição ao cupom de IPCA implícito (taxa real forward) via contrato futuro.",
        "• Cotação: taxa % a.a., convenção exponencial, base 252 dias úteis.",
        "• Valor de face de referência: R$ 100.000,00 por contrato (PU derivado dessa base).",
        "• VNA: indexador IPCA (título/âncora conceitual alinhado à NTN-B).",
        "• Vencimento: em geral dia 15 do mês de vencimento (calendário B3; conferir série).",
        "• Ajuste diário: PA corrigido por arbitragem CDI vs IPCA — acréscimo CDI em 1 du e",
        "  deflator do IPCA no denominador (1+IPCA_dia), conforme especificação da bolsa.",
        "• Relação com NTN-B: o DAP negocia o cupom/coupon implícito associado à curva IPCA;",
        "  hedge e direcional costumam usar NTN-B (ou duration da carteira) contra posição em DAP.",
    ])


def register(mcp: "FastMCP") -> None:
    """Registra as ferramentas deste módulo no servidor FastMCP."""

    mcp.tool(name="pu_dap")(pu_dap)
    mcp.tool(name="taxa_dap")(taxa_dap)
    mcp.tool(name="ajuste_dap")(ajuste_dap)
    mcp.tool(name="ref_dap")(ref_dap)
