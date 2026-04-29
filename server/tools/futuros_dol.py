"""
Ferramentas MCP para futuros de dólar DOL e mini WDO — ajuste, simulação, pontos à frente e referência.
"""

from __future__ import annotations

MULT_DOL = 50
MULT_WDO = 10


def _fmt_num(x: float, dec: int = 2) -> str:
    """Formata número com separadores de milhares no padrão brasileiro (1.234,56)."""
    neg = x < 0
    x = abs(float(x))
    if dec == 0:
        s = f"{x:,.0f}"
    else:
        s = f"{x:,.{dec}f}"
    s = s.replace(",", "X").replace(".", ",").replace("X", ".")
    return ("-" if neg else "") + s


def _fmt_brl(x: float, dec: int = 2) -> str:
    return "R$ " + _fmt_num(x, dec)


def _multiplier(mini: bool) -> int:
    return MULT_WDO if mini else MULT_DOL


def ajuste_dol(
    preco_op: float,
    preco_ajuste: float,
    qtd: int,
    mini: bool = False,
) -> str:
    """
    Ajuste financeiro em futuro de dólar.

    Preços em R$ por US$ 1.000,00 (pontos do contrato).
    DOL: AJ = (PA - PO) × qtd × 50. WDO (mini): AJ = (PA - PO) × qtd × 10.
    qtd > 0 comprado; qtd < 0 vendido.
    """
    mult = _multiplier(mini)
    contrato = "WDO (mini)" if mini else "DOL"
    po = preco_op
    pa = preco_ajuste
    diff = pa - po
    aj = diff * qtd * mult

    lines = [
        f"{contrato} — Ajuste diário",
        "",
        "Premissas:",
        f"  • Preço da operação / anterior (PO): {_fmt_num(po, 2)} (R$/US$ mil)",
        f"  • Preço de ajuste (PA): {_fmt_num(pa, 2)} (R$/US$ mil)",
        f"  • Quantidade (qtd): {qtd}",
        f"  • Multiplicador do contrato: {mult} (R$ por ponto por contrato)",
        "",
        "Passo 1 — Variação de preço (pontos R$/US$ mil):",
        f"  PA - PO = {_fmt_num(pa, 2)} - {_fmt_num(po, 2)} = {_fmt_num(diff, 2)}",
        "",
        "Passo 2 — Ajuste em R$:",
        f"  AJ = (PA - PO) × qtd × multiplicador",
        f"  AJ = {_fmt_num(diff, 2)} × {qtd} × {mult} = {_fmt_num(aj, 2)}",
        "",
        f"Resultado: AJ = {_fmt_brl(aj, 2)}",
    ]
    return "\n".join(lines)


def simular_posicao_dol(
    preco_entrada: float,
    precos_ajuste: str,
    qtd: int,
    mini: bool = False,
) -> str:
    """
    Simula ajustes diários com lista de preços de ajuste (PA) separados por vírgula.

    O primeiro ajuste usa PO = preco_entrada; nos dias seguintes, PO = PA do dia anterior.
    Acumula o ajuste diário e o total corrido.
    """
    mult = _multiplier(mini)
    contrato = "WDO (mini)" if mini else "DOL"
    raw = precos_ajuste.replace(";", ",")
    partes = [p.strip() for p in raw.split(",") if p.strip()]
    lines = [
        f"{contrato} — Simulação de ajustes",
        "",
        "Premissas:",
        f"  • PO inicial (preço de entrada): {_fmt_num(preco_entrada, 2)}",
        f"  • Lista de PAs (R$/US$ mil): {precos_ajuste}",
        f"  • qtd: {qtd}",
        f"  • Multiplicador: {mult}",
        "",
    ]
    if not partes:
        lines.append("Erro: informe ao menos um preço de ajuste (separados por vírgula).")
        return "\n".join(lines)

    try:
        precos = [float(x) for x in partes]
    except ValueError:
        lines.append("Erro: não foi possível interpretar todos os valores como números.")
        return "\n".join(lines)

    po = preco_entrada
    total = 0.0
    lines.append("| Dia | PO | PA | PA-PO | AJ do dia | AJ acumulado |")
    lines.append("|-----|-----|-----|-------|-----------|--------------|")

    for i, pa in enumerate(precos, start=1):
        diff = pa - po
        aj = diff * qtd * mult
        total += aj
        lines.append(
            f"| {i} | {_fmt_num(po, 2)} | {_fmt_num(pa, 2)} | {_fmt_num(diff, 2)} | {_fmt_brl(aj, 2)} | {_fmt_brl(total, 2)} |"
        )
        po = pa

    lines.extend(["", f"Total de ajustes: {_fmt_brl(total, 2)}"])
    return "\n".join(lines)


def forward_points(spot: float, futuro: float) -> str:
    """
    Pontos à frente: diferença entre futuro e spot em R$ por US$ 1.000,00.

    Também exibe a mesma diferença como percentual do spot.
    """
    pts = futuro - spot

    lines = [
        "Dólar — Pontos à frente (futuro vs spot)",
        "",
        "Premissas (R$/US$ 1.000,00):",
        f"  • Spot: {_fmt_num(spot, 2)}",
        f"  • Futuro: {_fmt_num(futuro, 2)}",
        "",
        "Passo 1 — Pontos absolutos:",
        f"  Pontos = futuro - spot = {_fmt_num(futuro, 2)} - {_fmt_num(spot, 2)} = {_fmt_num(pts, 2)}",
        "",
    ]
    if spot == 0:
        lines.append("Percentual sobre spot indefinido (spot = 0).")
        lines.append("")
        lines.append(f"Resultado: {_fmt_num(pts, 2)} pontos.")
    else:
        pct = pts / spot * 100.0
        lines.extend([
            "Passo 2 — Percentual sobre o spot:",
            f"  % = (pontos / spot) × 100 = ({_fmt_num(pts, 4)} / {_fmt_num(spot, 4)}) × 100 = {_fmt_num(pct, 4)}%",
            "",
            f"Resultado: {_fmt_num(pts, 2)} pontos ({_fmt_num(pct, 4)}% do spot).",
        ])
    return "\n".join(lines)


def ref_dol() -> str:
    """Referência para futuro DOL e mini WDO."""
    return "\n".join([
        "Referência — DOL e WDO (futuros de taxa de câmbio)",
        "",
        "DOL (contrato cheio):",
        f"  • Tamanho: US$ 50.000,00 por contrato (notional em dólar).",
        f"  • Multiplicador: {MULT_DOL} (R$ por variação de 1 ponto no preço cotado).",
        "  • Cotação: em R$ por US$ 1.000,00 (preço do contrato expresso como pontos R$/mil USD).",
        "",
        "WDO (mini):",
        f"  • Tamanho: US$ 10.000,00 por contrato.",
        f"  • Multiplicador: {MULT_WDO}.",
        "  • Mesma convenção de cotação em R$ por US$ 1.000,00.",
        "",
        "Vencimento:",
        "  Primeiro dia útil do mês de vencimento; sem entrega física de moeda — liquidação financeira.",
        "",
        "Ajuste diário:",
        "  AJ = (PA - PO) × N × multiplicador,",
        "  onde N é a quantidade de contratos (positiva se comprado, negativa se vendido),",
        "  PA e PO são preços de ajuste em R$/US$ 1.000,00.",
        "",
        "Observação:",
        "  Conferir manual e circulares B3 para detalhes de margem, horários, último dia de negociação e reajustes de especificação.",
    ])


def register(mcp) -> None:
    """Registra as ferramentas deste módulo no servidor FastMCP."""
    mcp.tool()(ajuste_dol)
    mcp.tool()(simular_posicao_dol)
    mcp.tool()(forward_points)
    mcp.tool()(ref_dol)
