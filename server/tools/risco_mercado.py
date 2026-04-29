"""
Ferramentas de risco de mercado: VaR paramétrico e VaR de carteira.
Fórmulas baseadas em Derivativos Negociação e Precificação (cap 12.8)
e Cálculo Financeiro das Tesourarias (cap 13).
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


_Z_TABLE = {
    90.0: 1.282,
    95.0: 1.645,
    97.5: 1.960,
    99.0: 2.326,
    99.5: 2.576,
    99.9: 3.090,
}


def var_parametrico(
    valor_mercado: float,
    volatilidade_aa: float,
    holding_period_du: int = 1,
    confianca_pct: float = 95.0,
) -> str:
    """VaR paramétrico (normal) para posição com um fator de risco.
    valor_mercado = valor marcado a mercado (R$).
    volatilidade_aa = volatilidade dos retornos em % a.a., base 252 du.
    holding_period_du = horizonte de tempo em dias úteis (default 1).
    confianca_pct = nível de confiança em % (default 95).

    VaR = P × z × sigma × sqrt(n)
    sigma diário = sigma_aa / sqrt(252)"""

    z = _Z_TABLE.get(confianca_pct)
    if z is None:
        closest = min(_Z_TABLE.keys(), key=lambda k: abs(k - confianca_pct))
        z = _Z_TABLE[closest]
        nota_z = f"(aproximado, usando {closest}%)"
    else:
        nota_z = ""

    sigma_aa = volatilidade_aa / 100.0
    sigma_dia = sigma_aa / math.sqrt(252)
    sigma_periodo = sigma_dia * math.sqrt(holding_period_du)

    var_abs = valor_mercado * z * sigma_periodo
    var_pct = z * sigma_periodo * 100.0

    lines = [
        "## VaR Paramétrico",
        "",
        "**Premissas**",
        "",
        f"- Valor a mercado: R$ {_fmt(valor_mercado)}",
        f"- Volatilidade: {_fmt(volatilidade_aa)}% a.a. (base 252)",
        f"- Holding period: {holding_period_du} du",
        f"- Confiança: {_fmt(confianca_pct, 1)}%",
        f"- z crítico: {_fmt(z, 3)} {nota_z}",
        "",
        "**Fórmula**",
        "",
        "```",
        "VaR = P × z × sigma_diária × sqrt(n)",
        "sigma_diária = sigma_aa / sqrt(252)",
        "```",
        "",
        "**Cálculo**",
        "",
        f"1) sigma diária = {_fmt(sigma_aa, 6)} / sqrt(252) = {_fmt(sigma_dia, 6)}",
        f"2) sigma período = {_fmt(sigma_dia, 6)} × sqrt({holding_period_du}) = {_fmt(sigma_periodo, 6)}",
        f"3) VaR = {_fmt(valor_mercado)} × {_fmt(z, 3)} × {_fmt(sigma_periodo, 6)} = R$ {_fmt(var_abs)}",
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| VaR ({_fmt(confianca_pct, 1)}%, {holding_period_du} du) | **R$ {_fmt(var_abs)}** |",
        f"| VaR em % | **{_fmt(var_pct)}%** |",
        f"| Perda máx esperada | Em {_fmt(100 - confianca_pct, 1)}% dos dias a perda pode superar R$ {_fmt(var_abs)} |",
    ]
    return "\n".join(lines)


def var_carteira(
    var1: float,
    var2: float,
    correlacao: float,
) -> str:
    """VaR de carteira com 2 ativos considerando correlação.
    var1 = VaR do ativo 1 (R$).
    var2 = VaR do ativo 2 (R$).
    correlacao = coeficiente de correlação entre os retornos (-1 a 1).

    VaR_carteira = sqrt(VaR1² + VaR2² + 2 × rho × VaR1 × VaR2)"""

    if correlacao < -1.0 or correlacao > 1.0:
        return "Erro: correlação deve estar entre -1 e 1."

    var_soma = var1 + var2
    var_cart = math.sqrt(var1**2 + var2**2 + 2 * correlacao * var1 * var2)
    diversificacao = var_soma - var_cart
    div_pct = (diversificacao / var_soma * 100.0) if var_soma > 0 else 0.0

    lines = [
        "## VaR de Carteira (2 ativos)",
        "",
        "**Premissas**",
        "",
        f"- VaR ativo 1: R$ {_fmt(var1)}",
        f"- VaR ativo 2: R$ {_fmt(var2)}",
        f"- Correlação (rho): {_fmt(correlacao, 4)}",
        "",
        "**Fórmula**",
        "",
        "```",
        "VaR_cart = sqrt(VaR1² + VaR2² + 2 × rho × VaR1 × VaR2)",
        "```",
        "",
        "**Cálculo**",
        "",
        f"1) VaR1² = {_fmt(var1**2)}",
        f"2) VaR2² = {_fmt(var2**2)}",
        f"3) 2 × rho × VaR1 × VaR2 = 2 × {_fmt(correlacao, 4)} × {_fmt(var1)} × {_fmt(var2)} = {_fmt(2 * correlacao * var1 * var2)}",
        f"4) VaR_cart = sqrt({_fmt(var1**2 + var2**2 + 2 * correlacao * var1 * var2)}) = **R$ {_fmt(var_cart)}**",
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| VaR soma simples | R$ {_fmt(var_soma)} |",
        f"| VaR carteira | **R$ {_fmt(var_cart)}** |",
        f"| Benefício diversificação | R$ {_fmt(diversificacao)} ({_fmt(div_pct, 1)}%) |",
        "",
        "**Interpretação**",
        "",
        f"- rho = 1: sem diversificação (VaR = soma)",
        f"- rho = -1: máxima diversificação (VaR = |VaR1 - VaR2|)",
        f"- rho atual ({_fmt(correlacao, 2)}): diversificação reduz o risco em {_fmt(div_pct, 1)}%",
    ]
    return "\n".join(lines)


def register(mcp: "FastMCP") -> None:
    mcp.tool()(var_parametrico)
    mcp.tool()(var_carteira)
