"""
Inflação implícita (BEIR), operações casadas e spread DI × título.

Metodologias baseadas em:
- Araújo & Vicente (2017) — Estimação da Inflação Implícita de Curto Prazo
- Val & Araujo (2019) — Breakeven Inflation Rate Estimation
- Silva & Holland — Liquidez de Mercado, Curva de DI Futuro e Taxa de Juros
"""

from __future__ import annotations

import math
from typing import TYPE_CHECKING

from tools.dias_uteis import _parse_date, _count_business_days
from tools.titulos_publicos import _fmt, _trunc

if TYPE_CHECKING:
    from fastmcp import FastMCP


_CUPOM_SEM_NTNB = 2.956301  # (1,06)^(6/12) - 1 em %, arredondado 6 casas


# ── BEIR via NTN-B ───────────────────────────────────────────────────────────

def inflacao_implicita_ntnb(
    pu_ntnb: float,
    taxa_nominal_aa: float,
    vna_ultimo_conhecido: float,
    data_liquidacao: str,
    data_vencimento_ntnb: str,
) -> str:
    """Extrai a inflação implícita (BEIR) de uma NTN-B sem pagamentos intermediários.
    Trata a defasagem de indexação de 15 dias corridos.
    pu_ntnb = preço unitário da NTN-B (ANBIMA).
    taxa_nominal_aa = taxa prefixada % a.a. até o vencimento (curva LTN/NTN-F).
    vna_ultimo_conhecido = VNA do último dia 15 com IPCA divulgado.
    data_liquidacao e data_vencimento_ntnb em DD/MM/YYYY ou YYYY-MM-DD.

    Fórmula (Eq. 4 de Araújo & Vicente, 2017):
    II = [PU × (1 + R)^(du/252)] / [VNA_t* × (1 + 2,956301%)] - 1"""

    liq = _parse_date(data_liquidacao)
    venc = _parse_date(data_vencimento_ntnb)
    du = _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)

    r = taxa_nominal_aa / 100.0
    fator_pre = (1.0 + r) ** (du / 252.0)
    cupom_fator = 1.0 + _CUPOM_SEM_NTNB / 100.0

    numerador = pu_ntnb * fator_pre
    denominador = vna_ultimo_conhecido * cupom_fator
    beir = numerador / denominador - 1.0
    beir_pct = beir * 100.0

    lines = [
        "## Inflação Implícita (BEIR) — via NTN-B",
        "",
        "**Premissas**",
        "",
        f"- PU NTN-B (ANBIMA): {_fmt(pu_ntnb, 6)}",
        f"- Taxa nominal (pré): {_fmt(taxa_nominal_aa, 4)}% a.a.",
        f"- VNA último conhecido (dia 15): {_fmt(vna_ultimo_conhecido, 6)}",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')}",
        f"- Data vencimento: {venc.strftime('%d/%m/%Y')}",
        f"- DU até vencimento: {du}",
        "",
        "**Fórmula**",
        "",
        "```",
        "II = [PU × (1 + R)^(du/252)] / [VNA_t* × (1 + 2,956301%)] - 1",
        "```",
        "",
        "**Cálculo**",
        "",
        f"1) Fator pré = (1 + {_fmt(r, 6)})^({du}/252) = {_fmt(fator_pre, 8)}",
        f"2) Numerador = {_fmt(pu_ntnb, 6)} × {_fmt(fator_pre, 8)} = {_fmt(numerador, 6)}",
        f"3) Denominador = {_fmt(vna_ultimo_conhecido, 6)} × {_fmt(cupom_fator, 8)} = {_fmt(denominador, 6)}",
        f"4) BEIR = {_fmt(numerador, 6)} / {_fmt(denominador, 6)} - 1 = {_fmt(beir_pct, 4)}%",
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| BEIR (período) | **{_fmt(beir_pct, 4)}%** |",
        f"| DU | {du} |",
    ]
    return "\n".join(lines)


# ── BEIR via DAP ─────────────────────────────────────────────────────────────

def inflacao_implicita_dap(
    pu_dap: float,
    taxa_nominal_aa: float,
    vna_anbima_hoje: float,
    vna_ultimo_conhecido: float,
    data_liquidacao: str,
    data_vencimento_dap: str,
) -> str:
    """Extrai a inflação implícita (BEIR) de contratos DAP com tratamento de lag.
    pu_dap = PU de ajuste do contrato DAP.
    taxa_nominal_aa = taxa prefixada % a.a. até o vencimento.
    vna_anbima_hoje = VNA projetado pela ANBIMA para a data corrente.
    vna_ultimo_conhecido = VNA do último dia 15 com IPCA divulgado.
    data_liquidacao e data_vencimento_dap em DD/MM/YYYY ou YYYY-MM-DD.

    Metodologia: Seção 3.3 de Araújo & Vicente (2017).
    II_lag = VNA_anbima / VNA_t* - 1
    VNA_t*_dap = 100.000 / (1 + II_lag)
    II = [PU_dap × (1 + R)^(du/252)] / VNA_t*_dap - 1"""

    liq = _parse_date(data_liquidacao)
    venc = _parse_date(data_vencimento_dap)
    du = _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)

    ii_lag = vna_anbima_hoje / vna_ultimo_conhecido - 1.0
    ii_lag_pct = ii_lag * 100.0
    vna_dap = 100_000.0 / (1.0 + ii_lag)

    r = taxa_nominal_aa / 100.0
    fator_pre = (1.0 + r) ** (du / 252.0)

    numerador = pu_dap * fator_pre
    beir = numerador / vna_dap - 1.0
    beir_pct = beir * 100.0

    lines = [
        "## Inflação Implícita (BEIR) — via DAP",
        "",
        "**Premissas**",
        "",
        f"- PU DAP (ajuste): {_fmt(pu_dap, 2)}",
        f"- Taxa nominal (pré): {_fmt(taxa_nominal_aa, 4)}% a.a.",
        f"- VNA ANBIMA (projetado hoje): {_fmt(vna_anbima_hoje, 6)}",
        f"- VNA último conhecido (dia 15): {_fmt(vna_ultimo_conhecido, 6)}",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')}",
        f"- Data vencimento DAP: {venc.strftime('%d/%m/%Y')}",
        f"- DU até vencimento: {du}",
        "",
        "**Cálculo — Inflação do lag**",
        "",
        "```",
        "II_lag = VNA_anbima / VNA_t* - 1",
        "```",
        "",
        f"- II_lag = {_fmt(vna_anbima_hoje, 6)} / {_fmt(vna_ultimo_conhecido, 6)} - 1 = {_fmt(ii_lag_pct, 6)}%",
        f"- VNA_t*_dap = 100.000 / (1 + {_fmt(ii_lag_pct, 6)}%) = {_fmt(vna_dap, 6)}",
        "",
        "**Cálculo — BEIR**",
        "",
        "```",
        "II = [PU_dap × (1 + R)^(du/252)] / VNA_t*_dap - 1",
        "```",
        "",
        f"1) Fator pré = (1 + {_fmt(r, 6)})^({du}/252) = {_fmt(fator_pre, 8)}",
        f"2) Numerador = {_fmt(pu_dap, 2)} × {_fmt(fator_pre, 8)} = {_fmt(numerador, 2)}",
        f"3) BEIR = {_fmt(numerador, 2)} / {_fmt(vna_dap, 6)} - 1 = {_fmt(beir_pct, 4)}%",
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| Inflação lag (já ocorrida) | {_fmt(ii_lag_pct, 6)}% |",
        f"| VNA_t* do DAP | {_fmt(vna_dap, 6)} |",
        f"| BEIR (período) | **{_fmt(beir_pct, 4)}%** |",
        f"| DU | {du} |",
    ]
    return "\n".join(lines)


# ── Distribuição mensal ──────────────────────────────────────────────────────

def distribuir_inflacao_mensal(
    inflacao_acumulada_pct: float,
    expectativas_mensais: str,
) -> str:
    """Distribui a inflação implícita acumulada entre meses proporcionalmente a pesos.
    inflacao_acumulada_pct = inflação acumulada do período em %.
    expectativas_mensais = expectativas Focus (ou pesos) por mês, separadas por vírgula, em %.

    Converte para taxa contínua, distribui pelo peso de cada mês, reconverte para discreta.
    Metodologia: Seção 4 de Araújo & Vicente (2017)."""

    pesos_raw = [float(p.strip()) for p in expectativas_mensais.split(",") if p.strip()]
    if not pesos_raw:
        return "Erro: informe ao menos uma expectativa mensal."

    soma_pesos = sum(pesos_raw)
    pesos_norm = [p / soma_pesos for p in pesos_raw]

    ii_continua = math.log(1.0 + inflacao_acumulada_pct / 100.0) * 100.0

    lines = [
        "## Distribuição Mensal da Inflação Implícita",
        "",
        "**Premissas**",
        "",
        f"- Inflação acumulada (discreta): {_fmt(inflacao_acumulada_pct, 4)}%",
        f"- Inflação acumulada (contínua): {_fmt(ii_continua, 4)}%",
        f"- Expectativas mensais: {expectativas_mensais.strip()}",
        f"- Número de meses: {len(pesos_raw)}",
        "",
        "**Distribuição**",
        "",
        "| Mês | Expectativa | Peso | II contínua | II discreta |",
        "|---|---|---|---|---|",
    ]

    for i, (exp, peso) in enumerate(zip(pesos_raw, pesos_norm), 1):
        ii_cont_mes = peso * ii_continua
        ii_disc_mes = (math.exp(ii_cont_mes / 100.0) - 1.0) * 100.0
        lines.append(
            f"| {i} | {_fmt(exp, 2)}% | {_fmt(peso * 100, 2)}% | {_fmt(ii_cont_mes, 4)}% | {_fmt(ii_disc_mes, 4)}% |"
        )

    lines += [
        "",
        f"Soma dos pesos: 100,00%",
        f"Soma das II contínuas: {_fmt(ii_continua, 4)}%",
    ]
    return "\n".join(lines)


# ── Casada de inflação (NTN-B + LTN) ────────────────────────────────────────

def casada_inflacao(
    taxa_ntnb_aa: float,
    taxa_pre_aa: float,
    data_liquidacao: str,
    data_vencimento: str,
) -> str:
    """Inflação implícita via operação casada NTN-B + LTN.
    Compra NTN-B (recebe IPCA + cupom real) + vende LTN (paga pré) = posição comprada em inflação.
    taxa_ntnb_aa = cupom de IPCA em % a.a.
    taxa_pre_aa = taxa prefixada (LTN) em % a.a.
    data_liquidacao e data_vencimento em DD/MM/YYYY ou YYYY-MM-DD.

    II_periodo = [(1 + taxa_pre)^(du/252) / (1 + taxa_ntnb)^(du/252)] - 1
    II_aa = (1 + II_periodo)^(252/du) - 1"""

    liq = _parse_date(data_liquidacao)
    venc = _parse_date(data_vencimento)
    du = _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)

    r_pre = taxa_pre_aa / 100.0
    r_real = taxa_ntnb_aa / 100.0

    fator_pre = (1.0 + r_pre) ** (du / 252.0)
    fator_real = (1.0 + r_real) ** (du / 252.0)

    ii_periodo = fator_pre / fator_real - 1.0
    ii_periodo_pct = ii_periodo * 100.0
    ii_aa = (1.0 + ii_periodo) ** (252.0 / du) - 1.0
    ii_aa_pct = ii_aa * 100.0

    spread_bps = (taxa_pre_aa - taxa_ntnb_aa) * 100.0

    lines = [
        "## Casada de Inflação — NTN-B + LTN",
        "",
        "**Operação**: compra NTN-B + vende LTN (ou DI) = comprado em inflação",
        "",
        "**Premissas**",
        "",
        f"- Cupom IPCA (NTN-B): {_fmt(taxa_ntnb_aa, 4)}% a.a.",
        f"- Taxa pré (LTN): {_fmt(taxa_pre_aa, 4)}% a.a.",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')}",
        f"- Data vencimento: {venc.strftime('%d/%m/%Y')}",
        f"- DU: {du}",
        f"- Spread nominal (pré - real): {_fmt(spread_bps, 2)} bps",
        "",
        "**Cálculo**",
        "",
        "```",
        "II_periodo = (1 + taxa_pre)^(du/252) / (1 + cupom_IPCA)^(du/252) - 1",
        "II_aa = (1 + II_periodo)^(252/du) - 1",
        "```",
        "",
        f"1) Fator pré = (1 + {_fmt(r_pre, 6)})^({du}/252) = {_fmt(fator_pre, 8)}",
        f"2) Fator real = (1 + {_fmt(r_real, 6)})^({du}/252) = {_fmt(fator_real, 8)}",
        f"3) II período = {_fmt(fator_pre, 8)} / {_fmt(fator_real, 8)} - 1 = {_fmt(ii_periodo_pct, 4)}%",
        f"4) II anualizada = (1 + {_fmt(ii_periodo_pct, 4)}%)^(252/{du}) - 1 = {_fmt(ii_aa_pct, 4)}%",
        "",
        "**Resultado**",
        "",
        "| Métrica | Valor |",
        "|---|---|",
        f"| Inflação implícita (período) | **{_fmt(ii_periodo_pct, 4)}%** |",
        f"| Inflação implícita (a.a.) | **{_fmt(ii_aa_pct, 4)}%** |",
        f"| Spread pré - real | {_fmt(spread_bps, 2)} bps |",
        "",
        "**Interpretação**",
        "",
        "- Se comprado nessa casada e a inflação realizada for **maior** que a implícita → ganho",
        "- Se a inflação realizada for **menor** → perda",
    ]
    return "\n".join(lines)


# ── Casada pré (LTN + DI futuro) ────────────────────────────────────────────

def casada_pre(
    taxa_ltn_aa: float,
    taxa_di_aa: float,
    data_liquidacao: str,
    data_vencimento: str,
) -> str:
    """Spread entre LTN e DI futuro de mesmo vencimento (LTN casada).
    Comprar LTN + vender DI futuro = CDI sintético (elimina risco pré).
    taxa_ltn_aa = taxa da LTN em % a.a.
    taxa_di_aa = taxa do DI futuro em % a.a.
    data_liquidacao e data_vencimento em DD/MM/YYYY ou YYYY-MM-DD.

    spread_bps = (taxa_ltn - taxa_di) × 100"""

    liq = _parse_date(data_liquidacao)
    venc = _parse_date(data_vencimento)
    du = _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)

    spread_bps = (taxa_ltn_aa - taxa_di_aa) * 100.0

    r_ltn = taxa_ltn_aa / 100.0
    r_di = taxa_di_aa / 100.0

    pu_ltn = 1_000.0 / (1.0 + r_ltn) ** (du / 252.0)
    pu_di = 100_000.0 / (1.0 + r_di) ** (du / 252.0)

    diff_financeira_por_100k = (1.0 / (1.0 + r_ltn) ** (du / 252.0) - 1.0 / (1.0 + r_di) ** (du / 252.0)) * 100_000.0

    lines = [
        "## Casada Pré — LTN + DI Futuro",
        "",
        "**Operação**: compra LTN + vende DI = CDI sintético",
        "",
        "**Premissas**",
        "",
        f"- Taxa LTN: {_fmt(taxa_ltn_aa, 4)}% a.a.",
        f"- Taxa DI futuro: {_fmt(taxa_di_aa, 4)}% a.a.",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')}",
        f"- Data vencimento: {venc.strftime('%d/%m/%Y')}",
        f"- DU: {du}",
        "",
        "**Spread**",
        "",
        f"- Spread = (LTN - DI) × 100 = ({_fmt(taxa_ltn_aa, 4)} - {_fmt(taxa_di_aa, 4)}) × 100 = **{_fmt(spread_bps, 2)} bps**",
        "",
        "**Preços**",
        "",
        "| Instrumento | VF | Taxa | PU |",
        "|---|---|---|---|",
        f"| LTN | R$ 1.000 | {_fmt(taxa_ltn_aa, 4)}% | {_fmt(pu_ltn, 6)} |",
        f"| DI futuro | R$ 100.000 | {_fmt(taxa_di_aa, 4)}% | {_fmt(pu_di, 2)} |",
        "",
        f"Diferença financeira (base 100k): {_fmt(diff_financeira_por_100k, 2)}",
        "",
        "**Interpretação**",
        "",
        "- Spread **positivo** (LTN > DI): título público paga mais que o derivativo — prêmio por carregar o papel",
        "- Spread **negativo** (LTN < DI): situação atípica, pode indicar demanda forte por LTN",
        "- A casada transforma a posição prefixada em pós-fixada (CDI sintético)",
        "- O ganho/perda da operação depende do spread no momento da montagem vs. desmontagem",
    ]
    return "\n".join(lines)


# ── Spread DI × Título ───────────────────────────────────────────────────────

def spread_di_titulo(
    taxa_titulo_aa: float,
    taxa_di_aa: float,
    du: int,
) -> str:
    """Calcula o spread entre taxa do título público (LTN/NTN-F) e taxa DI futuro de mesma duration.
    taxa_titulo_aa = taxa do título em % a.a.
    taxa_di_aa = taxa do DI futuro em % a.a.
    du = dias úteis até o vencimento.

    No mercado brasileiro, DI futuro é benchmark: títulos costumam ter spread positivo sobre DI."""

    spread_bps = (taxa_titulo_aa - taxa_di_aa) * 100.0

    r_tit = taxa_titulo_aa / 100.0
    r_di = taxa_di_aa / 100.0

    fator_tit = (1.0 + r_tit) ** (du / 252.0)
    fator_di = (1.0 + r_di) ** (du / 252.0)

    pu_tit_100k = 100_000.0 / fator_tit
    pu_di_100k = 100_000.0 / fator_di
    diff_pu = pu_tit_100k - pu_di_100k

    lines = [
        "## Spread DI × Título Público",
        "",
        "**Premissas**",
        "",
        f"- Taxa título: {_fmt(taxa_titulo_aa, 4)}% a.a.",
        f"- Taxa DI futuro: {_fmt(taxa_di_aa, 4)}% a.a.",
        f"- DU: {du}",
        "",
        "**Spread**",
        "",
        f"- Spread = ({_fmt(taxa_titulo_aa, 4)} - {_fmt(taxa_di_aa, 4)}) × 100 = **{_fmt(spread_bps, 2)} bps**",
        "",
        "**Impacto em PU (base R$ 100.000)**",
        "",
        f"- PU título: {_fmt(pu_tit_100k, 2)}",
        f"- PU DI: {_fmt(pu_di_100k, 2)}",
        f"- Diferença: {_fmt(diff_pu, 2)}",
        "",
        "**Contexto**",
        "",
        "No Brasil, a curva de DI futuro é a referência (benchmark) para precificação de todos os ativos de renda fixa.",
        "Títulos públicos prefixados (LTN/NTN-F) costumam negociar com um spread positivo sobre o DI,",
        "refletindo diferenças de liquidez, microestrutura e custo de carregamento.",
        "Spread positivo = título paga mais que DI. Spread negativo = situação atípica.",
    ]
    return "\n".join(lines)


# ── Referência: Inflação Implícita ───────────────────────────────────────────

def ref_inflacao_implicita() -> str:
    """Referência rápida sobre inflação implícita (BEIR) no mercado brasileiro."""

    return """## Referência — Inflação Implícita (BEIR)

### O que é

A inflação implícita (breakeven inflation rate — BEIR) é a diferença entre as taxas de juros nominal e real extraída de instrumentos financeiros. Representa a expectativa de inflação do mercado no mundo neutro ao risco.

### Decomposição

```
Inflação Implícita = Expectativa de Inflação + Prêmio de Risco da Inflação - Prêmio de Liquidez + Convexidade
```

No curto prazo, o prêmio de risco e os termos de liquidez/convexidade são desprezíveis. Portanto, a BEIR de curto prazo é um bom estimador da inflação futura.

### Problema da defasagem de indexação

As NTN-Bs possuem defasagem de 15 dias corridos: o VNA do dia 15 de cada mês é atualizado pelo IPCA do mês anterior. Isso faz com que a taxa negociada (cupom de IPCA) não seja exatamente a taxa real.

```
1 + C_IPCA = (1 + r_real) × (1 + π(T-15,T)) / (1 + π(t-15,t))
```

Para prazos longos essa diferença é desprezível. Para curto prazo pode ser relevante (vários bps).

### Problema da sazonalidade

O IPCA tem forte sazonalidade mensal (início e fim de ano mais altos). A curva real herda essa sazonalidade, mas modelos como Svensson não a capturam bem.

### Como extrair a BEIR

**Via NTN-B sem cupons intermediários:**
```
II = [PU × (1 + R)^(du/252)] / [VNA_t* × (1 + 2,956301%)] - 1
```

**Via DAP (futuro de cupom IPCA):**
```
II_lag = VNA_anbima / VNA_t* - 1
VNA_t*_dap = 100.000 / (1 + II_lag)
II = [PU_dap × (1 + R)^(du/252)] / VNA_t*_dap - 1
```

**Via casada (NTN-B + LTN):**
```
II = (1 + taxa_pre)^(du/252) / (1 + cupom_IPCA)^(du/252) - 1
```

### Distribuição mensal

A BEIR acumulada deve ser distribuída entre meses usando pesos proporcionais às expectativas do Focus Top 5 Curto Prazo, em taxa contínua, para incorporar sazonalidade e informações correntes."""


# ── Referência: Casada ───────────────────────────────────────────────────────

def ref_casada() -> str:
    """Referência rápida sobre operações casadas no mercado brasileiro de renda fixa."""

    return """## Referência — Operações Casadas

### LTN Casada (LTN + DI Futuro)

Compra de LTN + venda de DI futuro de mesmo vencimento. A operação elimina o risco prefixado e transforma a posição em CDI sintético.

```
Resultado ≈ CDI + spread (LTN - DI)
```

O spread reflete o prêmio por carregar o título público vs. o derivativo. Tipicamente positivo (LTN > DI).

**Por que LTN > DI?**
- Título exige desembolso financeiro (reserva bancária); DI futuro exige apenas margem
- Liquidez do DI futuro é superior à do mercado secundário de LTN
- Contrapartida BM&F tem risco de crédito menor que o soberano (anomalia brasileira)

### NTN-B Casada (NTN-B + LTN)

Compra de NTN-B + venda de LTN (ou DI) = posição comprada em inflação.

```
Inflação implícita = (1 + taxa_pre)^(du/252) / (1 + cupom_IPCA)^(du/252) - 1
```

- Se inflação realizada > implícita: comprado ganha
- Se inflação realizada < implícita: comprado perde

### Compra/venda de inflação via DI + DAP

- Compra DI + venda DAP = comprado em inflação (via derivativos, sem título cash)
- Venda DI + compra DAP = vendido em inflação

### Por que DI futuro é benchmark no Brasil

No mercado brasileiro, a curva de DI futuro é a referência para precificação de todos os ativos de renda fixa — inversão da lógica dos mercados desenvolvidos, onde a curva de títulos públicos é o benchmark.

Fatores:
- DI futuro tem maior liquidez que o mercado secundário de títulos
- Menor custo de transação (margem vs. reserva bancária)
- BM&F como contraparte central reduz risco de crédito
- Taxa de juros de um dia muito elevada historicamente

O Tesouro Nacional alinhou vencimentos de LTN/NTN-F aos de DI futuro (jan, abr, jul, out) para facilitar a casada e aumentar liquidez dos títulos."""


# ── Registro ─────────────────────────────────────────────────────────────────

def register(mcp: "FastMCP") -> None:
    """Registra as ferramentas de inflação implícita e casadas."""
    mcp.tool()(inflacao_implicita_ntnb)
    mcp.tool()(inflacao_implicita_dap)
    mcp.tool()(distribuir_inflacao_mensal)
    mcp.tool()(casada_inflacao)
    mcp.tool()(casada_pre)
    mcp.tool()(spread_di_titulo)
    mcp.tool()(ref_inflacao_implicita)
    mcp.tool()(ref_casada)
