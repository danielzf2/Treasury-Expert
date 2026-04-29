"""
Ferramentas MCP para contrato DI1 (DI Futuro) — PU, taxa implícita, ajuste, carry, hedge e referência.
"""

from __future__ import annotations

import math

VF = 100_000.0
DU_ANO = 252


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


def _pu_from_taxa_decimal(taxa_aa_pct: float, du: int) -> float:
    """PU com taxa em % a.a. e expoente du/252."""
    if du <= 0:
        return VF
    y = taxa_aa_pct / 100.0
    return VF / math.pow(1.0 + y, du / DU_ANO)


def pu_di(taxa_aa: float, du: int) -> str:
    """
    Calcula o PU do DI1 a partir da taxa % a.a. (base 252, capitalização exponencial)
    e dos dias úteis até o vencimento.

    Fórmula: PU = 100.000 / (1 + taxa/100)^(du/252), VF = R$ 100.000.
    """
    lines = [
        "DI1 — PU a partir da taxa",
        "",
        "Premissas:",
        f"  • Taxa (% a.a., base {DU_ANO} du, exponencial): {_fmt_num(taxa_aa, 4)}%",
        f"  • Dias úteis até vencimento (du): {du}",
        f"  • Valor de face (VF): {_fmt_brl(VF, 2)}",
        "",
        "Passo 1 — Converter taxa para decimal anual:",
        f"  y = taxa / 100 = {_fmt_num(taxa_aa / 100.0, 6)}",
        "",
        "Passo 2 — Expoente:",
        f"  du / {DU_ANO} = {du} / {DU_ANO} = {_fmt_num(du / DU_ANO, 6)}",
        "",
        "Passo 3 — Fator de desconto:",
    ]
    if du <= 0:
        lines.append(f"  du ≤ 0 → PU = VF = {_fmt_brl(VF, 2)}")
        pu = VF
    else:
        y = taxa_aa / 100.0
        fator = math.pow(1.0 + y, du / DU_ANO)
        lines.append(f"  (1 + y)^(du/{DU_ANO}) = (1 + {_fmt_num(y, 6)})^{_fmt_num(du / DU_ANO, 6)} = {_fmt_num(fator, 6)}")
        lines.append("")
        lines.append("Passo 4 — PU:")
        pu = VF / fator
        lines.append(f"  PU = VF / fator = {_fmt_num(VF, 2)} / {_fmt_num(fator, 6)} = {_fmt_num(pu, 6)}")
    lines.extend(["", f"Resultado: PU = {_fmt_brl(pu, 2)}"])
    return "\n".join(lines)


def taxa_di(pu: float, du: int) -> str:
    """
    Calcula a taxa % a.a. (base 252, exponencial) implícita no PU do DI1.

    taxa = ((100.000/PU)^(252/du) - 1) × 100.
    """
    lines = [
        "DI1 — Taxa implícita a partir do PU",
        "",
        "Premissas:",
        f"  • PU: {_fmt_brl(pu, 6)}",
        f"  • Dias úteis (du): {du}",
        "",
    ]
    if pu <= 0:
        lines.append("Erro: PU deve ser positivo.")
        return "\n".join(lines)
    if du <= 0:
        lines.append("Erro: du deve ser positivo para inferir taxa com esta fórmula.")
        return "\n".join(lines)

    ratio = VF / pu
    exp = DU_ANO / du
    base_pow = math.pow(ratio, exp)
    taxa = (base_pow - 1.0) * 100.0

    lines.extend([
        "Passo 1 — Razão VF/PU:",
        f"  100.000 / PU = {_fmt_num(VF, 2)} / {_fmt_num(pu, 6)} = {_fmt_num(ratio, 6)}",
        "",
        f"Passo 2 — Expoente 252/du:",
        f"  {DU_ANO} / {du} = {_fmt_num(exp, 6)}",
        "",
        "Passo 3 — Elevar a razão ao expoente:",
        f"  (VF/PU)^(252/du) = {_fmt_num(base_pow, 6)}",
        "",
        "Passo 4 — Taxa % a.a.:",
        f"  taxa = (valor acima - 1) × 100 = {_fmt_num(taxa, 6)}%",
        "",
        f"Resultado: taxa = {_fmt_num(taxa, 4)}% a.a. (base {DU_ANO} du, exponencial)",
    ])
    return "\n".join(lines)


def ajuste_di(
    pu_anterior: float,
    pu_ajuste: float,
    qtd: int,
    cdi_dia: float = 0.0,
) -> str:
    """
    Ajuste financeiro (AJ) de posição em DI1.

    • D0 (cdi_dia = 0): AJ = (PA - PO) × qtd, com PO = pu_anterior e PA = pu_ajuste.
    • D+n: AJ = (PA - PO × fator_CDI) × qtd, com fator_CDI = (1 + cdi_dia/100)^(1/252).

    Convenção: qtd > 0 comprado PU (vendido taxa); qtd < 0 vendido PU (comprado taxa).
    """
    po = pu_anterior
    pa = pu_ajuste
    lines = [
        "DI1 — Ajuste (AJ)",
        "",
        "Premissas:",
        f"  • PU posição / anterior (PO): {_fmt_brl(po, 6)}",
        f"  • PU de ajuste de hoje (PA): {_fmt_brl(pa, 6)}",
        f"  • Quantidade de contratos (qtd): {qtd}",
        f"  • CDI do dia (% a.d., informado): {_fmt_num(cdi_dia, 4)}% — se 0, tratado como operação D0",
        "",
    ]
    if cdi_dia == 0.0:
        aj = (pa - po) * qtd
        lines.extend([
            "Modo: D0 (sem correção CDI sobre PU anterior).",
            "",
            "Passo 1 — Variação de PU:",
            f"  PA - PO = {_fmt_num(pa, 6)} - {_fmt_num(po, 6)} = {_fmt_num(pa - po, 6)}",
            "",
            "Passo 2 — Ajuste:",
            f"  AJ = (PA - PO) × qtd = {_fmt_num(pa - po, 6)} × {qtd} = {_fmt_num(aj, 2)}",
            "",
            f"Resultado: AJ = {_fmt_brl(aj, 2)}",
        ])
    else:
        fator = math.pow(1.0 + cdi_dia / 100.0, 1.0 / DU_ANO)
        po_corr = po * fator
        diff = pa - po_corr
        aj = diff * qtd
        lines.extend([
            "Modo: D+n (PU anterior corrigido pelo CDI do dia).",
            "",
            "Passo 1 — Fator CDI diário (um dia útil):",
            f"  fator_CDI = (1 + CDI_dia/100)^(1/{DU_ANO})",
            f"  fator_CDI = (1 + {_fmt_num(cdi_dia / 100.0, 6)})^(1/{DU_ANO}) = {_fmt_num(fator, 8)}",
            "",
            "Passo 2 — PU anterior corrigido:",
            f"  PO × fator_CDI = {_fmt_num(po, 6)} × {_fmt_num(fator, 8)} = {_fmt_num(po_corr, 6)}",
            "",
            "Passo 3 — Comparar com PA:",
            f"  PA - (PO × fator_CDI) = {_fmt_num(pa, 6)} - {_fmt_num(po_corr, 6)} = {_fmt_num(diff, 6)}",
            "",
            "Passo 4 — Ajuste:",
            f"  AJ = diferença × qtd = {_fmt_num(diff, 6)} × {qtd} = {_fmt_num(aj, 2)}",
            "",
            f"Resultado: AJ = {_fmt_brl(aj, 2)}",
        ])
    return "\n".join(lines)


def carry_di(taxa_aa: float, du: int, cdi_aa: float, dias: int) -> str:
    """
    Simulação simplificada de carry de posição em DI1 por N dias úteis.

    Mantém a taxa implícita constante, reduz du em 1 por dia, aplica correção CDI
    diária constante derivada de cdi_aa (% a.a.) e mostra PU, componentes e P&L diário
    por contrato (qtd = 1).
    """
    lines = [
        "DI1 — Simulação de carry (taxa constante, CDI constante)",
        "",
        "Premissas:",
        f"  • Taxa DI mantida: {_fmt_num(taxa_aa, 4)}% a.a.",
        f"  • du inicial: {du}",
        f"  • CDI: {_fmt_num(cdi_aa, 4)}% a.a. → fator diário (1 du) = (1 + CDI_aa/100)^(1/{DU_ANO})",
        f"  • Horizonte: {dias} dia(s) útil(is)",
        f"  • Quantidade na tabela: 1 contrato",
        "",
    ]
    if dias < 0:
        lines.append("Erro: dias não pode ser negativo.")
        return "\n".join(lines)
    if du < 0:
        lines.append("Erro: du inicial negativo não é válido para esta simulação.")
        return "\n".join(lines)

    fator_cdi = math.pow(1.0 + cdi_aa / 100.0, 1.0 / DU_ANO)
    lines.append(f"Fator CDI por dia útil: {_fmt_num(fator_cdi, 8)}")
    lines.append("")

    pu_antes = _pu_from_taxa_decimal(taxa_aa, du)
    lines.append(f"PU no dia 0 (du={du}): {_fmt_brl(pu_antes, 6)}")
    lines.append("")
    lines.append("| Dia | du | PU mercado | PO×CDI (carry) | P&L dia (×1) |")
    lines.append("|-----|----|------------|----------------|--------------|")

    total_pl = 0.0
    for d in range(1, dias + 1):
        du_hoje = du - d
        if du_hoje < 0:
            lines.append("")
            lines.append(f"Observação: a partir do dia {d}, du ficaria negativo; simulação interrompida.")
            break
        pu_hoje = _pu_from_taxa_decimal(taxa_aa, du_hoje)
        po_corr = pu_antes * fator_cdi
        pl_dia = pu_hoje - po_corr
        total_pl += pl_dia
        lines.append(
            f"| {d} | {du_hoje} | {_fmt_num(pu_hoje, 4)} | {_fmt_num(po_corr, 4)} | {_fmt_brl(pl_dia, 2)} |"
        )
        pu_antes = pu_hoje

    lines.extend(["", f"P&L acumulado (1 contrato): {_fmt_brl(total_pl, 2)}"])
    return "\n".join(lines)


def hedge_di(dv01_posicao: float, taxa_di_aa: float, du: int) -> str:
    """
    Quantidade de contratos DI1 para hedge de DV01 da posição.

    DV01 de 1 contrato = PU(taxa + 1 bp) - PU(taxa - 1 bp), com 1 bp = 0,01 p.p. na taxa %.
    Qtd ≈ DV01_posição / DV01_contrato.
    """
    lines = [
        "DI1 — Hedge por DV01",
        "",
        "Premissas:",
        f"  • DV01 da posição a neutralizar (R$/bp): {_fmt_brl(dv01_posicao, 2)}",
        f"  • Taxa de referência do contrato: {_fmt_num(taxa_di_aa, 4)}% a.a.",
        f"  • du: {du}",
        f"  • 1 bp na taxa = 0,01 p.p. (ex.: {_fmt_num(taxa_di_aa, 4)}% → {_fmt_num(taxa_di_aa + 0.01, 4)}%)",
        "",
    ]
    if du <= 0:
        lines.append("Aviso: du ≤ 0 implica PU = VF; DV01 do contrato será 0 — hedge indefinido.")
        return "\n".join(lines)

    pu_m = _pu_from_taxa_decimal(taxa_di_aa, du)
    pu_up = _pu_from_taxa_decimal(taxa_di_aa + 0.01, du)
    pu_down = _pu_from_taxa_decimal(taxa_di_aa - 0.01, du)
    dv01_contrato = pu_up - pu_down

    lines.extend([
        "Passo 1 — PU na taxa central:",
        f"  PU = {_fmt_brl(pu_m, 4)}",
        "",
        "Passo 2 — PU após +1 bp e -1 bp na taxa:",
        f"  PU(+1 bp) = {_fmt_brl(pu_up, 4)}",
        f"  PU(-1 bp) = {_fmt_brl(pu_down, 4)}",
        "",
        "Passo 3 — DV01 por contrato (definição solicitada):",
        f"  DV01_contrato = PU(+1 bp) - PU(-1 bp) = {_fmt_brl(dv01_contrato, 4)}",
        "",
    ])

    if abs(dv01_contrato) < 1e-12:
        lines.append("DV01 do contrato efetivamente zero — não é possível dividir.")
        return "\n".join(lines)

    qtd = dv01_posicao / dv01_contrato
    lines.extend([
        "Passo 4 — Número de contratos:",
        f"  Qtd = DV01_posição / DV01_contrato",
        f"  Qtd = {_fmt_num(dv01_posicao, 4)} / {_fmt_num(dv01_contrato, 6)} = {_fmt_num(qtd, 4)}",
        "",
        f"Resultado: aproximadamente {_fmt_num(qtd, 2)} contratos DI1 (ajuste de sinal conforme lado da posição).",
    ])
    return "\n".join(lines)


def ref_di1() -> str:
    """Referência resumida do contrato DI1 (DI futuro de taxa)."""
    return "\n".join([
        "Referência — DI1 (contrato futuro de juros DI)",
        "",
        "Objeto:",
        "  Taxa média dos depósitos interfinanceiros de um dia (DI), implicitamente negociada via PU.",
        "",
        "Cotação:",
        "  Taxa percentual ao ano, base 252 dias úteis, capitalização exponencial; também negociação por PU.",
        "",
        "Lote / valor de face:",
        "  R$ 100.000,00 por contrato ao vencimento (VF).",
        "",
        "Tick size:",
        "  Depende da regra da B3 vigente para o contrato; em taxa e em PU há mínimos de variação definidos no manual do produto.",
        "",
        "Liquidação financeira:",
        "  Ajuste diário; liquidação financeira do ajuste em D+1 (padrão mercado B3 — conferir circular vigente).",
        "",
        "Vencimento:",
        "  Em geral, primeiro dia útil do mês de vencimento do contrato (código DI1 + letra do mês/ano).",
        "",
        "PU (preço unitário):",
        "  PU = 100.000 / (1 + taxa/100)^(du/252), com du = dias úteis até o vencimento.",
        "",
        "Ajuste (conceito):",
        "  • Dia da operação (D0): AJ = (PA - PO) × qtd.",
        "  • Dias seguintes: AJ = (PA - PO_corrigido) × qtd, com PO_corrigido = PU anterior ajustado pelo CDI do dia",
        "    (fator diário típico (1 + CDI_dia/100)^(1/252)).",
        "",
        "Sinal da posição:",
        "  qtd > 0: comprado PU (vendido taxa); qtd < 0: vendido PU (comprado taxa).",
    ])


def register(mcp) -> None:
    """Registra as ferramentas deste módulo no servidor FastMCP."""
    mcp.tool()(pu_di)
    mcp.tool()(taxa_di)
    mcp.tool()(ajuste_di)
    mcp.tool()(carry_di)
    mcp.tool()(hedge_di)
    mcp.tool()(ref_di1)
