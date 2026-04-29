"""
Ferramentas MCP para precificação de opções (Black-Scholes, gregas, vol implícita).
Usa apenas a biblioteca padrão `math`.
"""

from __future__ import annotations

import math
from typing import Any


def _norm_pdf(x: float) -> float:
    """Densidade da normal padrão em x."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def _norm_cdf(x: float) -> float:
    """
    CDF da normal padrão Φ(x) — aproximação tipo Abramowitz–Stegun (7.1.26 / 26.2.17).
    Precisão ~7 decimais para |x| típico em opções.
    """
    if x < 0:
        return 1.0 - _norm_cdf(-x)
    p = 0.2316419
    b1 = 0.319381530
    b2 = -0.356563782
    b3 = 1.781477937
    b4 = -1.821255978
    b5 = 1.330274429
    t = 1.0 / (1.0 + p * x)
    poly = t * (b1 + t * (b2 + t * (b3 + t * (b4 + t * b5))))
    return 1.0 - _norm_pdf(x) * poly


def _tipo_normalizado(tipo: str) -> str:
    t = tipo.strip().lower()
    if t in ("call", "c", "compra"):
        return "call"
    if t in ("put", "p", "venda"):
        return "put"
    raise ValueError(f"tipo inválido: {tipo!r} (use call ou put)")


def _param_bs(
    spot: float,
    strike: float,
    du: int,
    taxa_aa: float,
    vol_aa: float,
) -> tuple[float, float, float, float, float, float]:
    """Retorna (T, r, sigma, d1, d2, disc) ou levanta erro claro."""
    if spot <= 0 or strike <= 0:
        raise ValueError("spot e strike devem ser positivos.")
    if du < 0:
        raise ValueError("du não pode ser negativo.")
    if vol_aa <= 0:
        raise ValueError("vol_aa deve ser positiva (em % a.a.).")

    T = du / 252.0
    r = math.log(1.0 + taxa_aa / 100.0)
    sigma = vol_aa / 100.0

    if T <= 0:
        # Limite vencimento: intrínseco
        if sigma <= 0:
            raise ValueError("sigma deve ser positiva.")
        d1 = d2 = 0.0
    else:
        if sigma <= 0:
            raise ValueError("sigma deve ser positiva.")
        srt = sigma * math.sqrt(T)
        d1 = (math.log(spot / strike) + (r + 0.5 * sigma * sigma) * T) / srt
        d2 = d1 - srt

    disc = math.exp(-r * T)
    return T, r, sigma, d1, d2, disc


def _bs_price_call_put(
    spot: float,
    strike: float,
    du: int,
    taxa_aa: float,
    vol_aa: float,
    tipo: str,
) -> tuple[float, float, float, float, float, float, float, str]:
    T, r, sigma, d1, d2, disc = _param_bs(spot, strike, du, taxa_aa, vol_aa)
    kind = _tipo_normalizado(tipo)
    if T <= 0:
        if kind == "call":
            price = max(spot - strike, 0.0)
        else:
            price = max(strike - spot, 0.0)
        return T, r, sigma, d1, d2, disc, price, kind

    if kind == "call":
        price = spot * _norm_cdf(d1) - strike * disc * _norm_cdf(d2)
    else:
        price = strike * disc * _norm_cdf(-d2) - spot * _norm_cdf(-d1)
    return T, r, sigma, d1, d2, disc, price, kind


def black_scholes(
    spot: float,
    strike: float,
    du: int,
    taxa_aa: float,
    vol_aa: float,
    tipo: str = "call",
) -> str:
    """
    Preço Black-Scholes com convenção brasileira de tempo: T = du/252.

    Taxa em % a.a.: r contínuo = ln(1 + taxa/100). Vol em % a.a.: σ = vol_aa/100.
    """
    try:
        T, r, sigma, d1, d2, disc, price, kind = _bs_price_call_put(
            spot, strike, du, taxa_aa, vol_aa, tipo
        )
    except ValueError as e:
        return f"Erro: {e}"

    n_d1 = _norm_cdf(d1)
    n_d2 = _norm_cdf(d2)
    lines: list[str] = [
        "## Black-Scholes (T = du/252, r = ln(1+taxa/100))",
        "",
        f"- Spot S: {spot:.6f}",
        f"- Strike K: {strike:.6f}",
        f"- du: {du} → T = {T:.8f} anos",
        f"- Taxa a.a. (entrada %): {taxa_aa:.6f}% → r = {r:.8f}",
        f"- Vol a.a. (entrada %): {vol_aa:.6f}% → σ = {sigma:.8f}",
        f"- Tipo: **{kind}**",
        "",
        f"| Campo | Valor |",
        f"|---|---:|",
        f"| d1 | {d1:.8f} |",
        f"| d2 | {d2:.8f} |",
        f"| N(d1) | {n_d1:.8f} |",
        f"| N(d2) | {n_d2:.8f} |",
        f"| e^(-rT) | {disc:.8f} |",
        f"| **Prêmio** | **{price:.8f}** |",
        "",
    ]

    if T > 0:
        n1 = _norm_pdf(d1)
        sqrt_t = math.sqrt(T)
        gamma = n1 / (spot * sigma * sqrt_t)
        vega = spot * n1 * sqrt_t
        theta_call = (
            -spot * n1 * sigma / (2.0 * sqrt_t) - r * strike * disc * _norm_cdf(d2)
        )
        theta_put = (
            -spot * n1 * sigma / (2.0 * sqrt_t)
            + r * strike * disc * _norm_cdf(-d2)
        )
        rho_call = strike * T * disc * _norm_cdf(d2)
        rho_put = -strike * T * disc * _norm_cdf(-d2)
        delta_call = n_d1
        delta_put = n_d1 - 1.0

        if kind == "call":
            delta, theta, rho = delta_call, theta_call, rho_call
        else:
            delta, theta, rho = delta_put, theta_put, rho_put

        lines.extend(
            [
                "### Gregas (mesmo vencimento)",
                "",
                f"| Grega | Valor | Nota |",
                f"|---|---|---|",
                f"| Delta (∂V/∂S) | {delta:.8f} | |",
                f"| Gamma | {gamma:.8f} | igual call/put |",
                f"| Vega (∂V/∂σ, σ em decimal) | {vega:.8f} | por +100% vol; ÷100 para 1 p.p. |",
                f"| Theta (∂V/∂T, por ano) | {theta:.8f} | T em anos; ÷252 para por du |",
                f"| Rho (∂V/∂r, por unidade de r) | {rho:.8f} | ×0,01 para +1 p.p. a.a. |",
            ]
        )
    else:
        lines.append("_Gregas não definidas no vencimento (T=0)._")

    return "\n".join(lines)


def gregas(
    spot: float,
    strike: float,
    du: int,
    taxa_aa: float,
    vol_aa: float,
) -> str:
    """
    Delta, Gamma, Theta, Vega e Rho para call e put (Black-Scholes, mesmas convenções).
    """
    try:
        T, r, sigma, d1, d2, disc, _, _ = _bs_price_call_put(
            spot, strike, du, taxa_aa, vol_aa, "call"
        )
    except ValueError as e:
        return f"Erro: {e}"

    if T <= 0:
        return "Erro: du deve ser > 0 para calcular gregas."

    n_d1 = _norm_cdf(d1)
    n_d2 = _norm_cdf(d2)
    n1 = _norm_pdf(d1)
    sqrt_t = math.sqrt(T)
    gamma = n1 / (spot * sigma * sqrt_t)
    vega = spot * n1 * sqrt_t
    theta_call = (
        -spot * n1 * sigma / (2.0 * sqrt_t) - r * strike * disc * _norm_cdf(d2)
    )
    theta_put = (
        -spot * n1 * sigma / (2.0 * sqrt_t) + r * strike * disc * _norm_cdf(-d2)
    )
    rho_call = strike * T * disc * _norm_cdf(d2)
    rho_put = -strike * T * disc * _norm_cdf(-d2)

    dc = n_d1
    dp = n_d1 - 1.0
    lines = [
        "## Gregas — Call e Put",
        "",
        f"S={spot:.6f}, K={strike:.6f}, du={du}, taxa={taxa_aa:.4f}%, vol={vol_aa:.4f}%",
        f"d1={d1:.8f}, d2={d2:.8f}, T={T:.8f}",
        "",
        "| Grega | Call | Put |",
        "|---|---:|---:|",
        f"| Delta | {dc:.8f} | {dp:.8f} |",
        f"| Gamma | {gamma:.8f} | {gamma:.8f} |",
        f"| Vega (∂/∂σ, σ decimal) | {vega:.8f} | {vega:.8f} |",
        f"| Theta (∂/∂T, por ano) | {theta_call:.8f} | {theta_put:.8f} |",
        f"| Rho (∂/∂r) | {rho_call:.8f} | {rho_put:.8f} |",
        "",
        "**Theta por du:** dividir a linha Theta por 252.",
        "**Vega por 1 p.p. de vol:** dividir Vega por 100 (σ em decimal).",
        "**Rho por +1 p.p. a.a. na taxa:** multiplicar Rho por 0,01.",
    ]
    return "\n".join(lines)


def _vega_price(
    spot: float,
    strike: float,
    du: int,
    taxa_aa: float,
    sigma: float,
    kind: str,
) -> tuple[float, float]:
    """Preço e vega (∂V/∂σ) para σ em decimal; T>0."""
    T = du / 252.0
    if T <= 0:
        raise ValueError("du > 0 necessário.")
    r = math.log(1.0 + taxa_aa / 100.0)
    srt = sigma * math.sqrt(T)
    d1 = (math.log(spot / strike) + (r + 0.5 * sigma * sigma) * T) / srt
    d2 = d1 - srt
    disc = math.exp(-r * T)
    n1 = _norm_pdf(d1)
    vega = spot * n1 * math.sqrt(T)
    if kind == "call":
        price = spot * _norm_cdf(d1) - strike * disc * _norm_cdf(d2)
    else:
        price = strike * disc * _norm_cdf(-d2) - spot * _norm_cdf(-d1)
    return price, vega


def vol_implicita(
    premio: float,
    spot: float,
    strike: float,
    du: int,
    taxa_aa: float,
    tipo: str = "call",
) -> str:
    """
    Volatilidade implícita por Newton-Raphson sobre σ (decimal).

    Chute inicial 20% a.a.; tolerância 1e-6 no preço; até 100 iterações.
    """
    try:
        kind = _tipo_normalizado(tipo)
    except ValueError as e:
        return f"Erro: {e}"

    if du <= 0:
        return "Erro: du deve ser > 0."
    if spot <= 0 or strike <= 0:
        return "Erro: spot e strike positivos."

    sigma = 0.20
    tol = 1e-6
    max_it = 100

    for it in range(1, max_it + 1):
        try:
            p, vega = _vega_price(spot, strike, du, taxa_aa, sigma, kind)
        except ValueError as e:
            return f"Erro: {e}"

        diff = p - premio
        if abs(diff) < tol:
            return (
                "## Volatilidade implícita\n\n"
                f"- Tipo: **{kind}**\n"
                f"- Prêmio alvo: {premio:.8f}\n"
                f"- **σ implícita:** **{sigma * 100:.8f}%** a.a. ({sigma:.8f} em decimal)\n"
                f"- Preço BS na σ encontrada: {p:.8f}\n"
                f"- Iterações: {it}\n"
            )

        if vega < 1e-14:
            return (
                "Erro: Vega ~ 0; Newton não converge (prêmio fora de faixa ou "
                "parâmetros extremos)."
            )

        sigma -= diff / vega
        if sigma <= 0:
            sigma = 1e-6

    return (
        "Erro: não convergiu em 100 iterações. Ajuste prêmio ou parâmetros "
        "(ATM, prazo, taxa)."
    )


def ref_opcoes() -> str:
    """
    Texto de referência rápida: BS, Black-76, gregas, moneyness, decaimento.
    """
    return """## Referência — Opções

### Black-Scholes (ação sem dividendos, r contínuo)
- **Call:** `C = S·N(d1) − K·e^(−rT)·N(d2)`
- **Put:** `P = K·e^(−rT)·N(−d2) − S·N(−d1)`
- **d1** = [ln(S/K) + (r + σ²/2)T] / (σ√T), **d2** = d1 − σ√T
- Com **252 du:** usar `T = du/252`. Se a taxa for efetiva anual em %, muitos modelos usam `r = ln(1 + taxa/100)`.

### Black-76 (opção sobre **futuro** F, desconto explícito)
- Substitui-se `S` por preço futuro **F** e o prêmio é PV de `e^(−rT) × [F·N(d1) − K·N(d2)]` (call), com d1,d2 usando **F** no lugar de S e sem termo de carry em S — a fórmula fechada usa `F` e `e^(−rT)` multiplicando o valor forward.

### Gregas — definições úteis
| Grega | Significado |
|---|---|
| **Delta** | Sensibilidade do prêmio ao spot (∂V/∂S). Call 0 a 1; put −1 a 0. |
| **Gamma** | Taxa de mudança do delta (∂²V/∂S²). Mesma para call e put (mesmos T,K,σ). |
| **Vega** | Sensibilidade a σ (∂V/∂σ). Positiva para long call e long put. |
| **Theta** | Sensibilidade ao passar o tempo (∂V/∂T com T tempo até venc). Em geral **negativa** para long opção (decaimento). |
| **Rho** | Sensibilidade à taxa livre de risco. Call costuma ter rho **positivo**; put **negativo** (padrão r sobre desconto do strike). |

### Long vs short (sinais)
- **Long call/put:** delta com sinal da opção; **short** inverte delta (e demais gregas em relação ao nominal da posição vendida).

### ITM / ATM / OTM (call)
- **ITM:** S > K | **ATM:** S ≈ K | **OTM:** S < K  
- Put: inverta a desigualdade (ITM quando S < K).

### Decaimento temporal (theta)
- Quanto mais perto do vencimento (T↓), para opções **OTM/ATM**, o valor temporal tende a se **esgotar mais rápido** (theta mais acentuado em módulo), salvo efeitos de vol/smile no mundo real.
"""


def register(mcp: Any) -> None:
    """Registra ferramentas de opções no servidor MCP (ex.: FastMCP)."""
    mcp.tool()(black_scholes)
    mcp.tool()(gregas)
    mcp.tool()(vol_implicita)
    mcp.tool()(ref_opcoes)
