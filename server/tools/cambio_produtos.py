"""
Produtos de câmbio: ACC, ACE, PPE, FINIMP, cotação cruzada.
Baseado na Apostila de Câmbio FX (Harion Camargo) e convenções de mercado.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP


def _fmt(v: float, dec: int = 2) -> str:
    neg = v < 0
    x = abs(v)
    s = f"{x:,.{dec}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"-{s}" if neg else s


def precificar_acc(
    principal_usd: float,
    taxa_aa: float,
    prazo_dias: int,
    ptax_contratacao: float,
    ptax_liquidacao: float = 0.0,
) -> str:
    """Calcula ACC/ACE (Adiantamento sobre Contrato de Câmbio / Cambiais Entregues).
    principal_usd = valor em USD do adiantamento.
    taxa_aa = custo total % a.a. (funding + spread), linear base 360.
    prazo_dias = prazo em dias corridos.
    ptax_contratacao = PTAX na data de contratação (para conversão em BRL).
    ptax_liquidacao = PTAX na liquidação (se 0, mostra apenas o custo em USD).

    Juros (deságio) = principal × (taxa/100) × (dias/360), linear base 360."""

    juros_usd = principal_usd * (taxa_aa / 100.0) * (prazo_dias / 360.0)
    total_usd = principal_usd + juros_usd
    recebido_brl = principal_usd * ptax_contratacao

    lines = [
        "## ACC/ACE — Cálculo de Juros e Deságio",
        "",
        "**Premissas**",
        "",
        f"- Principal: USD {_fmt(principal_usd)}",
        f"- Taxa: {_fmt(taxa_aa)}% a.a. (linear, base 360)",
        f"- Prazo: {prazo_dias} dias corridos",
        f"- PTAX contratação: R$ {_fmt(ptax_contratacao, 4)}",
        "",
        "**Fórmula**",
        "",
        "```",
        "Juros (deságio) = Principal × (taxa/100) × (dias/360)",
        "```",
        "",
        "**Cálculo**",
        "",
        f"1) Juros = USD {_fmt(principal_usd)} × ({_fmt(taxa_aa)}% / 100) × ({prazo_dias}/360)",
        f"   Juros = **USD {_fmt(juros_usd)}**",
        "",
        f"2) Recebido na contratação = USD {_fmt(principal_usd)} × R$ {_fmt(ptax_contratacao, 4)}",
        f"   Recebido = **R$ {_fmt(recebido_brl)}**",
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| Principal | USD {_fmt(principal_usd)} |",
        f"| Juros (deságio) | **USD {_fmt(juros_usd)}** |",
        f"| Total a pagar no vencimento | USD {_fmt(total_usd)} |",
        f"| Recebido em BRL (contratação) | R$ {_fmt(recebido_brl)} |",
    ]

    if ptax_liquidacao > 0:
        desagio_brl = juros_usd * ptax_liquidacao
        lines += [
            f"| PTAX liquidação | R$ {_fmt(ptax_liquidacao, 4)} |",
            f"| Deságio em BRL | R$ {_fmt(desagio_brl)} |",
        ]

    lines += [
        "",
        "**Operação**",
        "",
        "- ACC = adiantamento **pré-embarque** (exportador recebe BRL antes de embarcar)",
        "- ACE = adiantamento **pós-embarque** (exportador já embarcou, desconta cambial)",
        "- Juros pagos em USD no vencimento; deságio convertido em BRL pela PTAX do dia",
    ]
    return "\n".join(lines)


def precificar_finimp(
    principal_usd: float,
    libor_aa: float,
    spread_aa: float,
    comissao_aa: float,
    prazo_dias: int,
    ir_pct: float = 15.0,
    iof_pct: float = 0.38,
) -> str:
    """Calcula FINIMP (Financiamento de Importação) com Libor + spread + comissão.
    principal_usd = valor em USD.
    libor_aa = Libor % a.a. (ou SOFR/referência).
    spread_aa = spread do banco % a.a.
    comissao_aa = comissão do banco brasileiro % a.a.
    prazo_dias = prazo em dias corridos.
    ir_pct = alíquota IR sobre juros remetidos (default 15%).
    iof_pct = IOF sobre juros e comissões (default 0,38%).

    Juros = principal × (libor + spread) / 100 × dias/360, linear base 360."""

    taxa_total_juros = libor_aa + spread_aa
    juros_usd = principal_usd * (taxa_total_juros / 100.0) * (prazo_dias / 360.0)
    ir_usd = juros_usd * (ir_pct / 100.0)
    iof_juros_usd = juros_usd * (iof_pct / 100.0)

    comissao_usd = principal_usd * (comissao_aa / 100.0) * (prazo_dias / 360.0)
    iof_comissao_usd = comissao_usd * (iof_pct / 100.0)

    custo_total_usd = juros_usd + ir_usd + iof_juros_usd + comissao_usd + iof_comissao_usd
    custo_total_aa = (custo_total_usd / principal_usd) * (360.0 / prazo_dias) * 100.0

    lines = [
        "## FINIMP — Financiamento de Importação",
        "",
        "**Premissas**",
        "",
        f"- Principal: USD {_fmt(principal_usd)}",
        f"- Libor/SOFR: {_fmt(libor_aa)}% a.a.",
        f"- Spread banco: {_fmt(spread_aa)}% a.a.",
        f"- Taxa juros total: {_fmt(taxa_total_juros)}% a.a. (Libor + spread)",
        f"- Comissão banco BR: {_fmt(comissao_aa)}% a.a.",
        f"- Prazo: {prazo_dias} dias corridos",
        f"- IR: {_fmt(ir_pct)}%",
        f"- IOF: {_fmt(iof_pct)}%",
        "",
        "**Cálculo**",
        "",
        "```",
        "Juros = Principal × (Libor + Spread)/100 × dias/360",
        "IR = Juros × alíquota_IR",
        "IOF = (Juros + Comissão) × alíquota_IOF",
        "Comissão = Principal × comissão/100 × dias/360",
        "```",
        "",
        "| Componente | Valor (USD) |",
        "|---|---|",
        f"| Juros (Libor + spread) | {_fmt(juros_usd)} |",
        f"| IR sobre juros ({_fmt(ir_pct)}%) | {_fmt(ir_usd)} |",
        f"| IOF sobre juros ({_fmt(iof_pct)}%) | {_fmt(iof_juros_usd)} |",
        f"| Comissão banco BR | {_fmt(comissao_usd)} |",
        f"| IOF sobre comissão ({_fmt(iof_pct)}%) | {_fmt(iof_comissao_usd)} |",
        f"| **Custo total** | **USD {_fmt(custo_total_usd)}** |",
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| Custo total (período) | USD {_fmt(custo_total_usd)} |",
        f"| Custo total efetivo (a.a.) | **{_fmt(custo_total_aa)}% a.a.** |",
        f"| Total a pagar | USD {_fmt(principal_usd + custo_total_usd)} |",
    ]
    return "\n".join(lines)


def cotar_moeda_cruzada(
    dolar_brl: float,
    paridade: float,
    tipo: str = "A",
) -> str:
    """Cotação cruzada de moeda estrangeira contra BRL via dólar.
    dolar_brl = taxa USD/BRL (ex: 5.20).
    paridade = cotação da moeda contra USD (ex: EUR/USD = 1.08).
    tipo = 'A' (moedas fortes: EUR, GBP, AUD, NZD) ou 'B' (moedas fracas: JPY, CHF, CAD, MXN).

    Tipo A: taxa_brl = dolar_brl × paridade (moeda cotada em USD)
    Tipo B: taxa_brl = dolar_brl / paridade (moeda cotada por USD)"""

    t = tipo.strip().upper()

    if t == "A":
        taxa_brl = dolar_brl * paridade
        formula = f"{_fmt(dolar_brl, 4)} × {_fmt(paridade, 4)} = {_fmt(taxa_brl, 4)}"
        explicacao = "Moeda forte (cotada EM dólares): EUR, GBP, AUD, NZD"
    elif t == "B":
        taxa_brl = dolar_brl / paridade
        formula = f"{_fmt(dolar_brl, 4)} / {_fmt(paridade, 4)} = {_fmt(taxa_brl, 4)}"
        explicacao = "Moeda fraca (cotada POR dólar): JPY, CHF, CAD, MXN, CNH, TRY"
    else:
        return "Erro: tipo deve ser 'A' (forte) ou 'B' (fraca)."

    lines = [
        "## Cotação Cruzada de Moeda via USD",
        "",
        f"**Tipo {t}** — {explicacao}",
        "",
        "**Premissas**",
        "",
        f"- USD/BRL: R$ {_fmt(dolar_brl, 4)}",
        f"- Paridade (moeda/USD): {_fmt(paridade, 4)}",
        "",
        "**Cálculo**",
        "",
        f"- Taxa BRL = {formula}",
        "",
        "**Resultado**",
        "",
        f"| Taxa em BRL | **R$ {_fmt(taxa_brl, 4)}** |",
        "|---|---|",
        "",
        "**Convenção**",
        "",
        "| Tipo | Moedas | Cálculo |",
        "|---|---|---|",
        "| A (forte) | EUR, GBP, AUD, NZD | USD/BRL × paridade |",
        "| B (fraca) | JPY, CHF, CAD, MXN, CNH, TRY, HKD | USD/BRL / paridade |",
    ]
    return "\n".join(lines)


def ref_produtos_cambio() -> str:
    """Referência rápida sobre produtos de câmbio (trade finance)."""

    return """## Referência — Produtos de Câmbio (Trade Finance)

### ACC (Adiantamento sobre Contrato de Câmbio)

- Fase: **pré-embarque** (exportador recebe antes de embarcar)
- Prazo: até 360 dias antes do embarque
- Custo: taxa linear base 360 (funding USD + spread)
- Juros pagos em USD no vencimento (chamado **deságio**)
- Deságio convertido em BRL pela PTAX do dia
- Garantias: contrato de exportação, aval, fiança

```
Juros = Principal × (taxa/100) × (dias/360)
```

### ACE (Adiantamento sobre Cambiais Entregues)

- Fase: **pós-embarque** (exportador já embarcou)
- Prazo: até 360 dias após embarque (pode chegar a 390)
- Mesma fórmula de juros do ACC
- Documentos exigidos: conhecimento de embarque, fatura invoice

### PPE (Pré-Pagamento de Exportação)

- Financiamento externo para exportação (funding internacional)
- Prazo: mais longo que ACC/ACE (até 5+ anos com amortizações)
- Custo: Libor/SOFR + spread, linear base 360
- Amortizações casadas com fluxo de recebimento do importador
- Incide IR sobre juros remetidos + IOF

### FINIMP (Financiamento de Importação)

- Financiamento para importadores brasileiros
- Direto: banco local capta linha externa e repassa
- Indireto: banco estrangeiro financia diretamente
- Custo: Libor + spread + comissão banco BR + IR + IOF
- Prazo: tipicamente 180 dias a 5 anos
- Amortizações: bullet ou semestrais (SAC)

```
Custo total = Juros + IR + IOF_juros + Comissão + IOF_comissão
Juros = Principal × (Libor + spread)/100 × dias/360
```

### Loan 4131

- Empréstimo externo direto (Resolução 4131 do CMN)
- Registro no ROF (Registro de Operação Financeira)
- Custo: taxa internacional + spread + IR + IOF
- Usado para capital de giro ou investimento

### Cotação de moedas cruzadas

- **Tipo A** (fortes): EUR, GBP, AUD, NZD → `BRL = USD/BRL × paridade`
- **Tipo B** (fracas): JPY, CHF, CAD, MXN → `BRL = USD/BRL / paridade`

### Taxa casada (em câmbio)

No contexto de câmbio, "casada" significa usar a **mesma taxa** para operações simultâneas de entrada e saída de um mesmo cliente, com o trader ganhando no lado de maior volume."""


def register(mcp: "FastMCP") -> None:
    """Registra ferramentas de produtos de câmbio."""
    mcp.tool()(precificar_acc)
    mcp.tool()(precificar_finimp)
    mcp.tool()(cotar_moeda_cruzada)
    mcp.tool()(ref_produtos_cambio)
