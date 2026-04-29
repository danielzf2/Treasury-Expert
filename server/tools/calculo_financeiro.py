"""
Cálculos financeiros básicos: equivalência de prazos, PV/FV, CDI, amortização.
Taxas em percentual (%), capitalização exponencial em 252 du salvo indicação.
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


def taxa_equivalente(taxa: float, du_origem: int, du_destino: int) -> str:
    """
    Equivalência exponencial entre prazos em dias úteis:
    taxa_destino = ((1+taxa/100)^(du_destino/du_origem) - 1) × 100.
    """
    if du_origem == 0:
        return "Erro: du_origem não pode ser zero."
    base = 1.0 + taxa / 100.0
    if base <= 0:
        return "Erro: (1+taxa/100) deve ser positivo."
    exp = float(du_destino) / float(du_origem)
    taxa_dest = (math.pow(base, exp) - 1.0) * 100.0
    return "\n".join([
        "Taxa equivalente (mesma base exponencial, prazos em du)",
        "",
        f"  taxa referência = {_fmt_num(taxa, 6)}% no prazo {du_origem} du",
        f"  prazo destino = {du_destino} du",
        f"  taxa_dest = ((1+taxa/100)^(du_dest/du_orig) - 1) × 100",
        f"  taxa_destino = {_fmt_num(taxa_dest, 6)}%",
        "",
        "Exemplos úteis (du): anual 252 → mensal 21; diária 1; semestral 126.",
    ])


def valor_presente(fv: float, taxa_aa: float, du: int) -> str:
    """PV = FV / (1+taxa/100)^(du/252)."""
    base = 1.0 + taxa_aa / 100.0
    if base <= 0:
        return "Erro: (1+taxa/100) deve ser positivo."
    expo = du / 252.0
    fator = math.pow(base, expo)
    pv = fv / fator
    return "\n".join([
        "Valor presente (taxa % a.a., 252 du, exponencial)",
        "",
        f"  FV = {_fmt_num(fv, 2)}",
        f"  taxa a.a. = {_fmt_num(taxa_aa, 6)}%",
        f"  du = {du}",
        f"  desconto = (1+taxa/100)^(du/252) = {_fmt_num(fator, 8)}",
        f"  PV = FV / desconto = {_fmt_num(pv, 2)}",
    ])


def valor_futuro(pv: float, taxa_aa: float, du: int) -> str:
    """FV = PV × (1+taxa/100)^(du/252)."""
    base = 1.0 + taxa_aa / 100.0
    if base <= 0:
        return "Erro: (1+taxa/100) deve ser positivo."
    expo = du / 252.0
    fator = math.pow(base, expo)
    fv = pv * fator
    return "\n".join([
        "Valor futuro (taxa % a.a., 252 du, exponencial)",
        "",
        f"  PV = {_fmt_num(pv, 2)}",
        f"  taxa a.a. = {_fmt_num(taxa_aa, 6)}%",
        f"  du = {du}",
        f"  fator = (1+taxa/100)^(du/252) = {_fmt_num(fator, 8)}",
        f"  FV = PV × fator = {_fmt_num(fv, 2)}",
    ])


def acumular_cdi(taxas_diarias: str) -> str:
    """
    Acumula CDI dia a dia: cada entrada é % a.a. do CDI daquele dia;
    fator do dia i = (1 + taxa_i/100)^(1/252); fator acumulado = produto.
    """
    parts = [p.strip() for p in taxas_diarias.split(",") if p.strip()]
    if not parts:
        return "Erro: informe taxas separadas por vírgula (ex.: 13,65,13,65,13,70)."
    rates: list[float] = []
    for p in parts:
        try:
            rates.append(float(p))
        except ValueError:
            return f"Erro: valor não numérico na lista: {p!r} (use ponto como decimal, ex.: 13.65,13.70)"
    acum = 1.0
    lines: list[str] = [
        "Acumulação de CDI (cada taxa = % a.a.; fator do dia = (1+taxa/100)^(1/252))",
        "",
        f"{'Dia':>4}  {'Taxa % a.a.':>14}  {'Fator dia':>14}  {'Fator acum.':>16}",
    ]
    for i, r in enumerate(rates, start=1):
        fd = math.pow(1.0 + r / 100.0, 1.0 / 252.0)
        acum *= fd
        lines.append(
            f"{i:4d}  {_fmt_num(r, 4):>14}  {_fmt_num(fd, 10):>14}  {_fmt_num(acum, 10):>16}"
        )
    ret_pct = (acum - 1.0) * 100.0
    lines.extend([
        "",
        f"Fator final (produto) = {_fmt_num(acum, 10)}",
        f"Retorno acumulado no período = {_fmt_num(ret_pct, 6)}%",
    ])
    return "\n".join(lines)


def taxa_over_para_anual(taxa_over: float) -> str:
    """
    Over % (por dia útil, em taxa simples sobre 1 du) → % a.a. 252 du.
    taxa_anual = ((1 + taxa_over/100)^252 - 1) × 100.
    """
    base = 1.0 + taxa_over / 100.0
    if base <= 0:
        return "Erro: (1+taxa_over/100) deve ser positivo."
    anual = (math.pow(base, 252.0) - 1.0) * 100.0
    base_chk = 1.0 + anual / 100.0
    over_rev = (math.pow(base_chk, 1.0 / 252.0) - 1.0) * 100.0
    return "\n".join([
        "CDI over ↔ taxa % a.a. (252 capitalizações)",
        "",
        "Over → anual:",
        f"  taxa_over = {_fmt_num(taxa_over, 8)}%",
        f"  taxa_a.a. = ((1 + taxa_over/100)^252 - 1) × 100 = {_fmt_num(anual, 6)}%",
        "",
        "Conferência (anual → over):",
        f"  taxa_over = ((1 + taxa_a.a./100)^(1/252) - 1) × 100 = {_fmt_num(over_rev, 8)}%",
    ])


def amortizacao(pv: float, taxa_mensal: float, n: int, sistema: str = "price") -> str:
    """
    Tabela de amortização: Price (Sistema Francês) ou SAC.
    taxa_mensal em % ao mês; n = número de parcelas.
    """
    if pv <= 0 or n <= 0:
        return "Erro: PV e n devem ser positivos."
    sys_key = sistema.strip().lower()
    i = taxa_mensal / 100.0
    lines: list[str] = [
        f"Amortização — sistema {sistema!r}, taxa {_fmt_num(taxa_mensal, 4)}% a.m., n={n}",
        f"PV = {_fmt_num(pv, 2)}",
        "",
    ]
    if sys_key == "price":
        if i == 0:
            pmt = pv / float(n)
            saldo = pv
            lines.append(f"{'Parc':>4}  {'Prestação':>14}  {'Juros':>14}  {'Amort.':>14}  {'Saldo':>14}")
            for k in range(1, n + 1):
                juros = 0.0
                amort = pmt
                saldo -= amort
                lines.append(
                    f"{k:4d}  {_fmt_num(pmt, 2):>14}  {_fmt_num(juros, 2):>14}  {_fmt_num(amort, 2):>14}  {_fmt_num(max(saldo, 0.0), 2):>14}"
                )
        else:
            pow_term = math.pow(1.0 + i, float(n))
            pmt = pv * i * pow_term / (pow_term - 1.0)
            saldo = pv
            lines.append(f"{'Parc':>4}  {'Prestação':>14}  {'Juros':>14}  {'Amort.':>14}  {'Saldo':>14}")
            for k in range(1, n + 1):
                juros = saldo * i
                amort = pmt - juros
                saldo -= amort
                lines.append(
                    f"{k:4d}  {_fmt_num(pmt, 2):>14}  {_fmt_num(juros, 2):>14}  {_fmt_num(amort, 2):>14}  {_fmt_num(max(saldo, 0.0), 2):>14}"
                )
        lines.append("")
        lines.append(f"PMT (constante) = {_fmt_num(pmt, 2)}")
    elif sys_key == "sac":
        amort_const = pv / float(n)
        saldo = pv
        lines.append(f"{'Parc':>4}  {'Prestação':>14}  {'Juros':>14}  {'Amort.':>14}  {'Saldo':>14}")
        for k in range(1, n + 1):
            juros = saldo * i
            pmt = amort_const + juros
            saldo -= amort_const
            lines.append(
                f"{k:4d}  {_fmt_num(pmt, 2):>14}  {_fmt_num(juros, 2):>14}  {_fmt_num(amort_const, 2):>14}  {_fmt_num(max(saldo, 0.0), 2):>14}"
            )
        lines.append("")
        lines.append(f"Amortização constante = {_fmt_num(amort_const, 2)} por período")
    else:
        return "Erro: sistema deve ser 'price' ou 'sac'."
    return "\n".join(lines)


def ref_calculo_financeiro() -> str:
    """Texto de referência: juros, equivalência, CDI over, contagens de dias."""
    return "\n".join([
        "Referência — cálculo financeiro (visão geral)",
        "",
        "• Juros compostos (taxa em % a.a., base 252 du, exponencial):",
        "    FV = PV × (1 + r/100)^(du/252)  ;  PV = FV / (1 + r/100)^(du/252)",
        "",
        "• Juros simples (linear, exemplo base 360):",
        "    juros = principal × (taxa/100) × (dc/360)",
        "",
        "• Equivalência de taxas no mesmo regime composto:",
        "    (1 + r1)^(du1/252) = (1 + r2)^(du2/252)",
        "    ou, entre prazos em du: r2 = ((1+r1/100)^(du2/du1) - 1) × 100",
        "",
        "• CDI over (convenção de mercado): taxa over em % aplicada por dia útil;",
        "  acumulação: ∏(1 + over_i). Na prática de divulgação, o percentual over costuma ser",
        "  trabalhado com truncamento na 8ª casa decimal antes de compor (regra CETIP).",
        "",
        "• Contagem de dias: 252 du (padrão renda fixa BR), 360 (linear comercial comum),",
        "  365/366 (alguns contratos e cupons em dias corridos).",
    ])


def register(mcp: "FastMCP") -> None:
    """Registra as ferramentas deste módulo no servidor FastMCP."""

    @mcp.tool()
    def taxa_equivalente_tool(taxa: float, du_origem: int, du_destino: int) -> str:
        """Equivale taxa % entre prazos em du: ((1+taxa/100)^(du_dest/du_orig)-1)×100."""
        return taxa_equivalente(taxa, du_origem, du_destino)

    @mcp.tool()
    def valor_presente_tool(fv: float, taxa_aa: float, du: int) -> str:
        """PV = FV / (1+taxa/100)^(du/252)."""
        return valor_presente(fv, taxa_aa, du)

    @mcp.tool()
    def valor_futuro_tool(pv: float, taxa_aa: float, du: int) -> str:
        """FV = PV × (1+taxa/100)^(du/252)."""
        return valor_futuro(pv, taxa_aa, du)

    @mcp.tool()
    def acumular_cdi_tool(taxas_diarias: str) -> str:
        """Lista de CDI % a.a. por dia (vírgula); produto dos fatores (1+taxa/100)^(1/252)."""
        return acumular_cdi(taxas_diarias)

    @mcp.tool()
    def taxa_over_para_anual_tool(taxa_over: float) -> str:
        """Over % → % a.a. 252 du e volta; ((1+over/100)^252-1)×100."""
        return taxa_over_para_anual(taxa_over)

    @mcp.tool()
    def amortizacao_tool(pv: float, taxa_mensal: float, n: int, sistema: str = "price") -> str:
        """Tabela Price ou SAC; taxa mensal em %; sistema 'price' ou 'sac'."""
        return amortizacao(pv, taxa_mensal, n, sistema)

    @mcp.tool()
    def ref_calculo_financeiro_tool() -> str:
        """Referência: compostos, simples, equivalência, over CDI, bases 252/360/365."""
        return ref_calculo_financeiro()

    _ = (
        taxa_equivalente_tool,
        valor_presente_tool,
        valor_futuro_tool,
        acumular_cdi_tool,
        taxa_over_para_anual_tool,
        amortizacao_tool,
        ref_calculo_financeiro_tool,
    )
