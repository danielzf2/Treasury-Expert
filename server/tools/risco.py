"""
Ferramentas MCP para métricas de risco de renda fixa (duration, convexidade, DV01, hedge).
"""

from __future__ import annotations

import math
from typing import Any


def _parse_floats_csv(s: str) -> list[float]:
    """Converte string CSV em lista de floats."""
    parts = [p.strip() for p in s.split(",") if p.strip()]
    return [float(p) for p in parts]


def _parse_ints_csv(s: str) -> list[int]:
    """Converte string CSV em lista de inteiros (dias úteis)."""
    parts = [p.strip() for p in s.split(",") if p.strip()]
    return [int(float(p)) for p in parts]


def duration_macaulay(fluxos: str, taxa_aa: float, dus: str) -> str:
    """
    Calcula a duration de Macaulay a partir de fluxos e dias úteis.

    Premissas: taxa anual efetiva em %; desconto (1 + taxa/100)^(du/252); tempo em anos t = du/252.
    """
    fc = _parse_floats_csv(fluxos)
    du_list = _parse_ints_csv(dus)
    if len(fc) != len(du_list):
        return (
            "Erro: número de fluxos e de prazos (du) deve ser igual. "
            f"fluxos={len(fc)}, dus={len(du_list)}."
        )
    if not fc:
        return "Erro: nenhum fluxo informado."

    y = taxa_aa / 100.0
    if y <= -1:
        return "Erro: taxa resultaria em base (1+y) não positiva."

    lines: list[str] = []
    lines.append("## Duration de Macaulay")
    lines.append("")
    lines.append(f"- Taxa a.a. (efetiva): {taxa_aa:.6f}%")
    lines.append("")
    lines.append("| # | Fluxo (FC) | du | t (anos) | PV | Peso | t × PV (contrib.) |")
    lines.append("|---:|---:|---:|---:|---:|---:|---:|")

    pv_list: list[float] = []
    t_list: list[float] = []
    for i, (fci, dui) in enumerate(zip(fc, du_list), start=1):
        ti = dui / 252.0
        disc = math.pow(1.0 + y, ti)
        pvi = fci / disc
        pv_list.append(pvi)
        t_list.append(ti)

    pv_total = sum(pv_list)
    if pv_total == 0:
        return "Erro: soma dos valores presentes é zero."

    d_mac = 0.0
    for i, (fci, dui, ti, pvi) in enumerate(
        zip(fc, du_list, t_list, pv_list), start=1
    ):
        peso = pvi / pv_total
        contrib = ti * pvi
        d_mac += contrib
        lines.append(
            f"| {i} | {fci:.6f} | {dui} | {ti:.6f} | {pvi:.6f} | {peso:.6f} | {contrib:.6f} |"
        )

    d_mac /= pv_total
    lines.append("")
    lines.append(f"- **Soma PV** = {pv_total:.6f}")
    lines.append(
        f"- **D (Macaulay)** = Σ(tᵢ × PVᵢ) / Σ(PVᵢ) = **{d_mac:.6f}** anos"
    )
    return "\n".join(lines)


def duration_modificada(dur_mac: float, taxa_aa: float) -> str:
    """
    Duration modificada sob convenções usuais em tesouraria.

    Forma simples (solicitada): Dmod = D_mac / (1 + taxa/100).
    """
    y = taxa_aa / 100.0
    lines: list[str] = []
    lines.append("## Duration modificada")
    lines.append("")
    lines.append(f"- D (Macaulay): {dur_mac:.6f} anos")
    lines.append(f"- Taxa a.a. (efetiva, em %): {taxa_aa:.6f}%")
    lines.append("")
    lines.append("### Convenções")
    lines.append("")
    lines.append(
        "- **Simples / composto anual efetivo (base principal):** "
        "`Dmod = D_mac / (1 + taxa/100)`."
    )
    lines.append(
        "- **Taxa contínua já embutida na duration:** se `D_mac` já for "
        "\"modificada\" no seu modelo, use `Dmod = D_mac`."
    )
    lines.append(
        "- **Ajuste diário (252 du):** às vezes usa-se "
        "`Dmod = D_mac / (1 + taxa/100)^(1/252)` para alinhar choques de 1 du; "
        "depende da convenção interna do sistema."
    )
    lines.append("")
    if y <= -1:
        return "\n".join(lines) + "\n\nErro: (1 + taxa/100) deve ser > 0."

    dmod_simples = dur_mac / (1.0 + y)
    dmod_diario = dur_mac / math.pow(1.0 + y, 1.0 / 252.0)
    lines.append("### Resultados numéricos")
    lines.append("")
    lines.append(f"| Métrica | Valor |")
    lines.append("|---|---:|")
    lines.append(f"| Dmod (simples: ÷ (1+y)) | **{dmod_simples:.6f}** |")
    lines.append(f"| Dmod (÷ (1+y)^(1/252)) | {dmod_diario:.6f} |")
    lines.append("")
    lines.append(
        "Use a linha **simples** como referência principal, salvo se o seu "
        "manual de risco pedir o ajuste diário."
    )
    return "\n".join(lines)


def convexidade(fluxos: str, taxa_aa: float, dus: str) -> str:
    """
    Convexidade (versão compatível com desconto em potências de (1+y)^(du/252)).

    C = Σ(tᵢ(tᵢ + 1/252) × PVᵢ) / (PV × (1+y)²), com y = taxa/100.
    """
    fc = _parse_floats_csv(fluxos)
    du_list = _parse_ints_csv(dus)
    if len(fc) != len(du_list):
        return (
            "Erro: número de fluxos e de prazos (du) deve ser igual. "
            f"fluxos={len(fc)}, dus={len(du_list)}."
        )
    if not fc:
        return "Erro: nenhum fluxo informado."

    y = taxa_aa / 100.0
    if y <= -1:
        return "Erro: taxa resultaria em base (1+y) não positiva."

    lines: list[str] = []
    lines.append("## Convexidade")
    lines.append("")
    lines.append(f"- Taxa a.a. (efetiva): {taxa_aa:.6f}% → y = {y:.6f}")
    lines.append("")
    lines.append("| # | FC | du | t | PVᵢ | t(t+1/252)PVᵢ |")
    lines.append("|---:|---:|---:|---:|---:|---:|")

    pv_list: list[float] = []
    numer_terms: list[float] = []
    inv252 = 1.0 / 252.0

    for i, (fci, dui) in enumerate(zip(fc, du_list), start=1):
        ti = dui / 252.0
        pvi = fci / math.pow(1.0 + y, ti)
        pv_list.append(pvi)
        term = ti * (ti + inv252) * pvi
        numer_terms.append(term)
        lines.append(
            f"| {i} | {fci:.6f} | {dui} | {ti:.6f} | {pvi:.6f} | {term:.6f} |"
        )

    pv_total = sum(pv_list)
    if pv_total == 0:
        return "Erro: soma dos valores presentes é zero."

    numer = sum(numer_terms)
    denom = pv_total * (1.0 + y) ** 2
    c_main = numer / denom

    # Forma simplificada pedida: (1/PV) × Σ(FCᵢ × tᵢ² / (1+y)^tᵢ)
    c_simp = 0.0
    for fci, dui in zip(fc, du_list):
        ti = dui / 252.0
        c_simp += fci * (ti**2) / math.pow(1.0 + y, ti)
    c_simp /= pv_total

    lines.append("")
    lines.append(f"- **PV** = Σ PVᵢ = {pv_total:.6f}")
    lines.append(f"- **Numerador** Σ tᵢ(tᵢ+1/252)PVᵢ = {numer:.6f}")
    lines.append(f"- **(1+y)²** = {(1.0 + y) ** 2:.6f}")
    lines.append(f"- **C (fórmula principal)** = {c_main:.6f}")
    lines.append("")
    lines.append("### Forma simplificada (referência)")
    lines.append("")
    lines.append(
        "`C_simpl = (1/PV) × Σ(FCᵢ × tᵢ² / (1+y)^tᵢ)` "
        f"= **{c_simp:.6f}** (pode diferir da principal conforme a convenção)."
    )
    return "\n".join(lines)


def dv01(dmod: float, valor_mercado: float) -> str:
    """
    DV01 aproximado: variação de valor em moeda para movimento de 1 bp na taxa.
    """
    dv = dmod * valor_mercado * 0.0001
    lines = [
        "## DV01",
        "",
        f"- Dmod: {dmod:.6f}",
        f"- Valor de mercado (PV/notional marcado): {valor_mercado:,.2f}",
        "",
        "`DV01 = Dmod × PV × 0,0001` (com `dy = 1 bp = 0,0001`).",
        "",
        f"| Métrica | Valor |",
        f"|---|---:|",
        f"| **DV01** | **{dv:,.6f}** (moeda por +1 bp) |",
        "",
        "**Interpretação:** se a taxa sobe 1 bp e a duration modificada for a métrica "
        "adequada ao seu modelo, a variação aproximada de valor é **-DV01** (posição "
        "longa em taxa / long duration) ou **+DV01** conforme o sinal do risco.",
    ]
    return "\n".join(lines)


def hedge_di_futuro(dv01_carteira: float, dv01_contrato: float) -> str:
    """
    Número de contratos DI futuro para hedge de DV01 (aproximação linear).
    """
    if dv01_contrato == 0:
        return "Erro: DV01 do contrato não pode ser zero."

    q_raw = dv01_carteira / dv01_contrato
    q = int(round(q_raw))
    lines: list[str] = []
    lines.append("## Hedge com DI futuro (via DV01)")
    lines.append("")
    lines.append(f"- DV01 carteira: {dv01_carteira:,.6f}")
    lines.append(f"- DV01 por contrato (1 unidade): {dv01_contrato:,.6f}")
    lines.append("")
    lines.append("`Quantidade ≈ round(DV01_carteira / DV01_contrato)`.")
    lines.append("")
    lines.append(f"| Campo | Valor |")
    lines.append("|---|---:|")
    lines.append(f"| Razão bruta | {q_raw:.6f} |")
    lines.append(f"| **Contratos (arredondado)** | **{q}** |")
    lines.append("")
    lines.append("### Direção (intuição)")
    lines.append("")
    lines.append(
        "- Carteira **long duration** (perde quando a taxa **sobe**): para reduzir "
        "sensibilidade a alta de juros, busca-se **vender duration** no hedge."
    )
    lines.append(
        "- No **DI futuro**, **comprar taxa** (posição que ganha com alta de juros) "
        "associa-se a **vender PU** / entrar no lado que se beneficia quando a taxa "
        "implícita do contrato **sobe** — alinhe sempre ao manual do banco e ao sinal "
        "do DV01 do contrato que você estiver usando."
    )
    lines.append(
        "- Use o **sinal** do resultado: se a sua convenção de DV01 do DI tiver sinal "
        "oposto ao da carteira, inverta a perna (comprar/vender contratos)."
    )
    return "\n".join(lines)


def aproximar_variacao_preco(
    dmod: float, conv: float, delta_bps: float, valor_mercado: float
) -> str:
    """
    Aproximação de Taylor de 2ª ordem na variação relativa de preço.
    """
    dy = delta_bps / 10000.0
    rel1 = -dmod * dy
    rel2 = -dmod * dy + 0.5 * conv * (dy**2)
    dp1 = valor_mercado * rel1
    dp2 = valor_mercado * rel2
    diff_rel = rel2 - rel1
    diff_abs = dp2 - dp1

    lines = [
        "## Aproximação de variação de preço (Taylor 2ª ordem)",
        "",
        f"- Dmod: {dmod:.6f}",
        f"- Convexidade C: {conv:.6f}",
        f"- Choque: **{delta_bps:+.2f} bps** → `dy = delta_bps/10000` = {dy:.8f}",
        f"- Valor de mercado: {valor_mercado:,.2f}",
        "",
        "`dP/P = -Dmod × dy + 0,5 × C × dy²`",
        "",
        "| Aproximação | dP/P | Δ Valor (moeda) |",
        "|---|---:|---:|",
        f"| **1ª ordem** (`-Dmod×dy`) | {rel1:.8f} | {dp1:,.6f} |",
        f"| **2ª ordem** (com convexidade) | {rel2:.8f} | {dp2:,.6f} |",
        "",
        "| Diferença | Valor |",
        "|---|---:|",
        f"| 2ª − 1ª (relativa) | {diff_rel:.8f} |",
        f"| 2ª − 1ª (moeda) | {diff_abs:,.6f} |",
    ]
    return "\n".join(lines)


def duration_anbima(fluxos: str, taxa_aa: float, dus: str) -> str:
    """Duration ANBIMA: Σ(dui × PUi) / Σ(PUi), resultado em dias úteis (não em anos).
    Conforme Metodologia ANBIMA de Precificação de Títulos Públicos."""

    fc = _parse_floats_csv(fluxos)
    du_list = _parse_ints_csv(dus)
    if len(fc) != len(du_list):
        return f"Erro: fluxos ({len(fc)}) e dus ({len(du_list)}) devem ter mesmo tamanho."
    if not fc:
        return "Erro: nenhum fluxo informado."

    y = taxa_aa / 100.0
    if y <= -1:
        return "Erro: taxa resultaria em base não positiva."

    lines = [
        "## Duration ANBIMA (em dias úteis)",
        "",
        f"- Taxa a.a.: {taxa_aa:.4f}%",
        "- Fórmula: Duration = Σ(dui × PUi) / Σ(PUi)",
        "- Resultado em **dias úteis** (convenção ANBIMA), não em anos",
        "",
        "| # | FC | du | PV (FC descontado) | du × PV |",
        "|---|---|---|---|---|",
    ]

    pv_list = []
    du_pv_list = []
    for i, (fci, dui) in enumerate(zip(fc, du_list), 1):
        disc = math.pow(1.0 + y, dui / 252.0)
        pvi = fci / disc
        du_pv = dui * pvi
        pv_list.append(pvi)
        du_pv_list.append(du_pv)
        lines.append(f"| {i} | {fci:.2f} | {dui} | {pvi:.6f} | {du_pv:.6f} |")

    pv_total = sum(pv_list)
    du_pv_total = sum(du_pv_list)
    if pv_total == 0:
        return "Erro: soma dos PV é zero."

    duration_du = du_pv_total / pv_total
    duration_anos = duration_du / 252.0

    lines += [
        "",
        f"- Σ(PUi) = {pv_total:.6f}",
        f"- Σ(dui × PUi) = {du_pv_total:.6f}",
        f"- **Duration ANBIMA = {duration_du:.2f} dias úteis** ({duration_anos:.4f} anos)",
    ]
    return "\n".join(lines)


def carry_titulo(
    taxa_aa: float,
    du: int,
    valor_face: float = 1000.0,
) -> str:
    """Carry diário de título prefixado (ou DI futuro) com taxa constante.
    taxa_aa = taxa em % a.a. (exponencial, base 252).
    du = dias úteis restantes até o vencimento.
    valor_face = valor de resgate (1.000 para LTN, 100.000 para DI).

    PU_d0 = VF / (1 + taxa)^(du/252)
    PU_d1 = VF / (1 + taxa)^((du-1)/252)
    carry = PU_d1 - PU_d0"""

    r = taxa_aa / 100.0
    pu_d0 = valor_face / (1.0 + r) ** (du / 252.0)
    pu_d1 = valor_face / (1.0 + r) ** ((du - 1) / 252.0)
    carry_abs = pu_d1 - pu_d0
    carry_bps = (carry_abs / pu_d0) * 10000.0
    carry_aa_pct = ((pu_d1 / pu_d0) ** 252 - 1.0) * 100.0

    fmt = lambda v, d=6: f"{v:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".")

    lines = [
        "## Carry Diário — Título Prefixado",
        "",
        "**Premissas**",
        "",
        f"- Taxa: {fmt(taxa_aa, 4)}% a.a.",
        f"- DU restantes: {du}",
        f"- Valor de face: R$ {fmt(valor_face, 2)}",
        "",
        "**Fórmula**",
        "",
        "```",
        "PU_d0 = VF / (1 + taxa)^(du/252)",
        "PU_d1 = VF / (1 + taxa)^((du-1)/252)",
        "carry = PU_d1 - PU_d0",
        "```",
        "",
        "**Cálculo**",
        "",
        f"1) PU hoje (du={du}): {fmt(pu_d0)}",
        f"2) PU amanhã (du={du - 1}): {fmt(pu_d1)}",
        f"3) Carry 1 du: {fmt(pu_d1)} - {fmt(pu_d0)} = **R$ {fmt(carry_abs)}**",
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| PU hoje | {fmt(pu_d0)} |",
        f"| PU amanhã (taxa constante) | {fmt(pu_d1)} |",
        f"| Carry 1 du (R$) | **{fmt(carry_abs)}** |",
        f"| Carry 1 du (bps) | **{fmt(carry_bps, 2)} bps** |",
        f"| Carry anualizado | {fmt(carry_aa_pct, 4)}% a.a. |",
        "",
        "Se a taxa de mercado não muda, o título ganha esse carry por dia útil.",
    ]
    return "\n".join(lines)


def register(mcp: Any) -> None:
    """Registra todas as ferramentas de risco no servidor MCP (ex.: FastMCP)."""
    mcp.tool()(duration_macaulay)
    mcp.tool()(duration_modificada)
    mcp.tool()(duration_anbima)
    mcp.tool()(convexidade)
    mcp.tool()(dv01)
    mcp.tool()(hedge_di_futuro)
    mcp.tool()(aproximar_variacao_preco)
    mcp.tool()(carry_titulo)
