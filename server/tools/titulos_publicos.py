"""
Precificação de títulos públicos conforme Metodologia ANBIMA (nov/2023).
Truncamentos, arredondamentos e convenções exatas da metodologia oficial.
"""

from __future__ import annotations

import math
from datetime import date
from typing import TYPE_CHECKING

from tools.dias_uteis import _parse_date, _count_business_days

if TYPE_CHECKING:
    from fastmcp import FastMCP


# ── Helpers ANBIMA ────────────────────────────────────────────────────────────

def _trunc(x: float, decimals: int) -> float:
    """Trunca (não arredonda) para N casas decimais — regra ANBIMA 'T-N'."""
    factor = 10 ** decimals
    return math.trunc(x * factor) / factor


def _round(x: float, decimals: int) -> float:
    """Arredonda para N casas decimais — regra ANBIMA 'A-N'."""
    return round(x, decimals)


def _fmt(n: float, dec: int = 6) -> str:
    """Formata número com vírgula decimal estilo BR."""
    neg = n < 0
    x = abs(n)
    s = f"{x:.{dec}f}"
    intp, frac = s.split(".")
    out_i: list[str] = []
    for i, c in enumerate(reversed(intp)):
        if i and i % 3 == 0:
            out_i.append(".")
        out_i.append(c)
    int_br = "".join(reversed(out_i))
    res = f"{int_br},{frac}"
    return f"-{res}" if neg else res


def _exp_trunc14(base: float, expoente: float) -> float:
    """(1 + base)^expoente truncado a 14 casas — regra ANBIMA T-14 para exponenciais."""
    return _trunc(base ** expoente, 14)


def _parse_dus(s: str) -> list[int]:
    parts = [p.strip() for p in s.split(",") if p.strip()]
    return sorted(int(p) for p in parts)


def _generate_coupon_dates(data_liquidacao: date, data_vencimento: date) -> list[date]:
    """Gera datas de cupom semestrais retroagindo 6 meses a partir do vencimento.
    Retorna apenas datas posteriores à liquidação, em ordem crescente."""
    dates: list[date] = []
    d = data_vencimento
    while d > data_liquidacao:
        dates.append(d)
        m = d.month - 6
        y = d.year
        if m <= 0:
            m += 12
            y -= 1
        d = date(y, m, d.day)
    return sorted(dates)


def _compute_dus(data_liquidacao: date, coupon_dates: list[date]) -> list[int]:
    """Calcula DU (ANBIMA) da liquidação até cada data de cupom."""
    return [
        _count_business_days(data_liquidacao, cd, start_inclusive=True, end_inclusive=False)
        for cd in coupon_dates
    ]


# ── Constantes ────────────────────────────────────────────────────────────────

_VN = 1000.0
_NTNF_CUPOM_AA = 10.0  # edital padrão
_NTNB_CUPOM_AA = 6.0   # edital padrão


# ── LTN ───────────────────────────────────────────────────────────────────────

def precificar_ltn(taxa_aa: float, data_liquidacao: str, data_vencimento: str) -> str:
    """Precifica LTN conforme metodologia ANBIMA.
    PU = VN / (1 + Taxa)^(du/252), truncado 6 casas.
    data_liquidacao e data_vencimento em DD/MM/YYYY ou YYYY-MM-DD.
    DU calculado internamente (liquidação inclusive, vencimento exclusive)."""

    liq = _parse_date(data_liquidacao)
    venc = _parse_date(data_vencimento)
    du = _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)

    r = taxa_aa / 100.0
    expo = du / 252.0
    fator = _exp_trunc14(1.0 + r, expo)
    pu_raw = _VN / fator
    pu = _trunc(pu_raw, 6)

    lines = [
        "## LTN — Precificação ANBIMA",
        "",
        "**Premissas**",
        "",
        f"- VN (valor nominal no vencimento): R$ {_fmt(_VN, 2)}",
        f"- Taxa efetiva anual: {_fmt(taxa_aa, 4)}% a.a.",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')}",
        f"- Data vencimento: {venc.strftime('%d/%m/%Y')}",
        f"- DU (liquidação inclusive até vencimento exclusive): {du}",
        "",
        "**Regras ANBIMA aplicadas**",
        "",
        "- Exponencial `(1+r)^(du/252)`: truncado 14 casas (T-14)",
        "- PU final: truncado 6 casas (T-6)",
        "",
        "**Cálculo**",
        "",
        "```",
        "PU = VN / (1 + Taxa)^(du/252)",
        "```",
        "",
        f"1) r = {_fmt(taxa_aa, 4)} / 100 = {_fmt(r, 8)}",
        f"2) expoente = {du} / 252 = {_fmt(expo, 6)}",
        f"3) (1 + r)^(du/252) = {_fmt(1.0 + r, 8)}^{_fmt(expo, 6)} = {_fmt(fator, 14)} (T-14)",
        f"4) PU = {_fmt(_VN, 2)} / {_fmt(fator, 14)} = {_fmt(pu_raw, 10)} → **{_fmt(pu, 6)}** (T-6)",
        "",
        "**Resultado**",
        "",
        f"| Métrica | Valor |",
        f"|---|---|",
        f"| PU (ANBIMA) | **{_fmt(pu, 6)}** |",
        f"| Taxa → PU | {_fmt(taxa_aa, 4)}% → {_fmt(pu, 6)} |",
    ]
    return "\n".join(lines)


# ── NTN-F ─────────────────────────────────────────────────────────────────────

def precificar_ntnf(taxa_aa: float, data_liquidacao: str, data_vencimento: str, vn: float = 1000.0) -> str:
    """Precifica NTN-F conforme metodologia ANBIMA.
    Cupom 10% a.a. = 4,88088% semestral (arredondado).
    Fluxos descontados arredondados. PU truncado 6 casas.
    data_liquidacao e data_vencimento em DD/MM/YYYY ou YYYY-MM-DD.
    Datas de cupom e DUs calculados internamente a partir do vencimento."""

    liq = _parse_date(data_liquidacao)
    venc = _parse_date(data_vencimento)
    coupon_dates = _generate_coupon_dates(liq, venc)
    dus = _compute_dus(liq, coupon_dates)

    if not dus:
        return "Erro: nenhum fluxo encontrado entre liquidação e vencimento."

    cupom_sem_raw = (1.0 + _NTNF_CUPOM_AA / 100.0) ** 0.5 - 1.0
    cupom_pct = _round(cupom_sem_raw * 100, 6)
    cupom_sem = cupom_pct / 100.0

    r = taxa_aa / 100.0
    last_du = dus[-1]
    dus_str = ",".join(str(d) for d in dus)

    lines = [
        "## NTN-F — Precificação ANBIMA",
        "",
        "**Premissas**",
        "",
        f"- VN: R$ {_fmt(vn, 2)}",
        f"- Cupom edital: {_fmt(_NTNF_CUPOM_AA, 1)}% a.a.",
        f"- Cupom semestral (A-6): (1 + {_fmt(_NTNF_CUPOM_AA/100, 2)})^0,5 - 1 = {_fmt(cupom_pct, 6)}% → decimal {_fmt(cupom_sem, 8)}",
        f"- TIR (taxa de desconto): {_fmt(taxa_aa, 4)}% a.a.",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')}",
        f"- Data vencimento: {venc.strftime('%d/%m/%Y')}",
        f"- Fluxos: {len(dus)} cupons",
        f"- DU dos cupons: {dus_str}",
        "",
        "**Regras ANBIMA aplicadas**",
        "",
        "- Cupom semestral: arredondado 6 casas no % (A-6)",
        "- Exponencial: truncado 14 casas (T-14)",
        "- Fluxos descontados: arredondados 9 casas (A-9)",
        "- PU: truncado 6 casas (T-6)",
        "",
        "**Cálculo**",
        "",
        "```",
        "PU = Σ [Cupom × VN / (1 + TIR)^(dui/252)] + VN / (1 + TIR)^(dun/252)",
        "```",
        "",
        "| # | DU | Data cupom | Evento | Nominal (R$) | (1+TIR)^(du/252) T-14 | PV (R$) |",
        "|---|---|---|---|---|---|---|",
    ]

    pu_total = 0.0
    for idx, (du, cd) in enumerate(zip(dus, coupon_dates), 1):
        expo = du / 252.0
        fator = _exp_trunc14(1.0 + r, expo)
        if du == last_du:
            nominal = vn * cupom_sem + vn
            evento = "cupom + principal"
        else:
            nominal = vn * cupom_sem
            evento = "cupom"
        pv = _round(nominal / fator, 9)
        pu_total += pv
        lines.append(
            f"| {idx} | {du} | {cd.strftime('%d/%m/%Y')} | {evento} | {_fmt(nominal, 7)} | {_fmt(fator, 14)} | {_fmt(pv, 9)} |"
        )

    pu = _trunc(pu_total, 6)
    lines += [
        "",
        f"Soma dos PV = {_fmt(pu_total, 10)}",
        f"PU (T-6) = **{_fmt(pu, 6)}**",
        "",
        "**Resultado**",
        "",
        f"| Métrica | Valor |",
        f"|---|---|",
        f"| PU (ANBIMA) | **{_fmt(pu, 6)}** |",
        f"| Cupom semestral | {_fmt(cupom_pct, 5)}% |",
        f"| Número de fluxos | {len(dus)} |",
    ]
    return "\n".join(lines)


# ── NTN-B ─────────────────────────────────────────────────────────────────────

def precificar_ntnb(
    taxa_real_aa: float,
    vna: float,
    data_liquidacao: str,
    data_vencimento: str,
    cupom_aa: float = 6.0,
) -> str:
    """Precifica NTN-B conforme metodologia ANBIMA.
    Separa Cotação (truncada 4 casas) e PU = Cotação × VNA (truncado 6 casas).
    VNA deve ser informado já truncado a 6 casas.
    data_liquidacao e data_vencimento em DD/MM/YYYY ou YYYY-MM-DD.
    Datas de cupom e DUs calculados internamente a partir do vencimento."""

    liq = _parse_date(data_liquidacao)
    venc = _parse_date(data_vencimento)
    coupon_dates = _generate_coupon_dates(liq, venc)
    dus = _compute_dus(liq, coupon_dates)

    if not dus:
        return "Erro: nenhum fluxo encontrado entre liquidação e vencimento."

    vna = _trunc(vna, 6)

    cupom_sem_raw = (1.0 + cupom_aa / 100.0) ** (6.0 / 12.0) - 1.0
    cupom_sem_pct = _round(cupom_sem_raw * 100, 6)
    cupom_sem = cupom_sem_pct / 100.0

    r = taxa_real_aa / 100.0
    last_du = dus[-1]
    dus_str = ",".join(str(d) for d in dus)

    lines = [
        "## NTN-B — Precificação ANBIMA",
        "",
        "**Premissas**",
        "",
        f"- VNA (truncado 6 casas): {_fmt(vna, 6)}",
        f"- Cupom edital: {_fmt(cupom_aa, 1)}% a.a.",
        f"- Cupom semestral: [(1 + {_fmt(cupom_aa/100, 2)})^(6/12) - 1] × 100 = {_fmt(cupom_sem_pct, 6)}%",
        f"- TIR (taxa real): {_fmt(taxa_real_aa, 4)}% a.a.",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')}",
        f"- Data vencimento: {venc.strftime('%d/%m/%Y')}",
        f"- Fluxos: {len(dus)} cupons",
        f"- DU dos cupons: {dus_str}",
        "",
        "**Regras ANBIMA aplicadas**",
        "",
        "- VNA: truncado 6 casas (T-6)",
        "- Cupom semestral em cotação: arredondado 6 casas (A-6)",
        "- Exponencial: truncado 14 casas (T-14)",
        "- Fluxos descontados (cotação): arredondados 10 casas (A-10)",
        "- Cotação (soma dos fluxos % do VNA): truncada 4 casas (T-4)",
        "- PU = Cotação × VNA: truncado 6 casas (T-6)",
        "",
        "**Cálculo — Cotação (em % do VNA)**",
        "",
        "```",
        "Cotação = Σ [Cupom% / (1+TIR)^(dui/252)] + 100 / (1+TIR)^(dun/252)",
        "```",
        "",
        "| # | DU | Data cupom | Evento | Fluxo (% VNA) | (1+TIR)^(du/252) T-14 | PV (% VNA) |",
        "|---|---|---|---|---|---|---|",
    ]

    cotacao_total = 0.0
    for idx, (du, cd) in enumerate(zip(dus, coupon_dates), 1):
        expo = du / 252.0
        fator = _exp_trunc14(1.0 + r, expo)
        if du == last_du:
            fluxo_pct = cupom_sem_pct + 100.0
            evento = "cupom + principal"
        else:
            fluxo_pct = cupom_sem_pct
            evento = "cupom"
        pv_pct = _round(fluxo_pct / fator, 10)
        cotacao_total += pv_pct
        lines.append(
            f"| {idx} | {du} | {cd.strftime('%d/%m/%Y')} | {evento} | {_fmt(fluxo_pct, 6)} | {_fmt(fator, 14)} | {_fmt(pv_pct, 10)} |"
        )

    cotacao_pct = _trunc(cotacao_total, 4)
    cotacao_dec = cotacao_pct / 100.0
    pu_raw = cotacao_dec * vna
    pu = _trunc(pu_raw, 6)

    lines += [
        "",
        f"Soma dos PV (% VNA) = {_fmt(cotacao_total, 10)}",
        f"Cotação = {_fmt(cotacao_total, 10)} → **{_fmt(cotacao_pct, 4)}%** (T-4)",
        f"Cotação decimal = {_fmt(cotacao_pct, 4)} / 100 = {_fmt(cotacao_dec, 6)}",
        "",
        "**Cálculo — PU**",
        "",
        "```",
        "PU = (Cotação / 100) × VNA",
        "```",
        "",
        f"PU = ({_fmt(cotacao_pct, 4)} / 100) × {_fmt(vna, 6)} = {_fmt(pu_raw, 10)} → **{_fmt(pu, 6)}** (T-6)",
        "",
        "**Resultado**",
        "",
        f"| Métrica | Valor |",
        f"|---|---|",
        f"| Cotação (T-4) | **{_fmt(cotacao_pct, 4)}%** |",
        f"| VNA (T-6) | {_fmt(vna, 6)} |",
        f"| PU (T-6) | **{_fmt(pu, 6)}** |",
        f"| Cupom semestral (A-6) | {_fmt(cupom_sem_pct, 6)}% |",
    ]
    return "\n".join(lines)


# ── LFT ───────────────────────────────────────────────────────────────────────

def precificar_lft(agio_desagio_bps: float, data_liquidacao: str, data_vencimento: str, vna_selic: float) -> str:
    """Precifica LFT conforme metodologia ANBIMA.
    Cotação truncada 4 casas. VNA truncado 6 casas. PU truncado 6 casas.
    Rentabilidade em % a.a.; bps positivo = deságio, negativo = ágio.
    data_liquidacao e data_vencimento em DD/MM/YYYY ou YYYY-MM-DD.
    DU calculado internamente (liquidação inclusive, vencimento exclusive)."""

    liq = _parse_date(data_liquidacao)
    venc = _parse_date(data_vencimento)
    du = _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)

    vna_selic = _trunc(vna_selic, 6)
    rent_aa = agio_desagio_bps / 100.0

    r = rent_aa / 100.0
    expo = du / 252.0
    fator = _exp_trunc14(1.0 + r, expo)
    cotacao_pct = 100.0 / fator
    cotacao_pct_trunc = _trunc(cotacao_pct, 4)
    cotacao_dec = cotacao_pct_trunc / 100.0
    pu_raw = cotacao_dec * vna_selic
    pu = _trunc(pu_raw, 6)

    lines = [
        "## LFT — Precificação ANBIMA",
        "",
        "**Premissas**",
        "",
        f"- VNA Selic (truncado 6 casas): {_fmt(vna_selic, 6)}",
        f"- Rentabilidade (ágio/deságio): {_fmt(agio_desagio_bps, 2)} bps = {_fmt(rent_aa, 4)}% a.a.",
        f"- Convenção: bps > 0 = deságio, bps < 0 = ágio",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')}",
        f"- Data vencimento: {venc.strftime('%d/%m/%Y')}",
        f"- DU: {du}",
        "",
        "**Regras ANBIMA aplicadas**",
        "",
        "- Exponencial: truncado 14 casas (T-14)",
        "- Cotação: truncada 4 casas no percentual (T-4)",
        "- VNA: truncado 6 casas (T-6)",
        "- PU: truncado 6 casas (T-6)",
        "",
        "**Cálculo**",
        "",
        "```",
        "Cotação(%) = 100 / (1 + Rentabilidade/100)^(du/252)",
        "PU = (Cotação / 100) × VNA",
        "```",
        "",
        f"1) Rentabilidade decimal = {_fmt(rent_aa, 4)} / 100 = {_fmt(r, 8)}",
        f"2) (1 + r)^(du/252) = {_fmt(fator, 14)} (T-14)",
        f"3) Cotação = 100 / {_fmt(fator, 14)} = {_fmt(cotacao_pct, 10)}% → **{_fmt(cotacao_pct_trunc, 4)}%** (T-4)",
        f"4) PU = ({_fmt(cotacao_pct_trunc, 4)} / 100) × {_fmt(vna_selic, 6)} = {_fmt(pu_raw, 10)} → **{_fmt(pu, 6)}** (T-6)",
        "",
        "**Resultado**",
        "",
        f"| Métrica | Valor |",
        f"|---|---|",
        f"| Cotação (T-4) | **{_fmt(cotacao_pct_trunc, 4)}%** |",
        f"| VNA Selic (T-6) | {_fmt(vna_selic, 6)} |",
        f"| PU (T-6) | **{_fmt(pu, 6)}** |",
    ]
    return "\n".join(lines)


# ── Fluxo de caixa ────────────────────────────────────────────────────────────

def fluxo_caixa_titulo(tipo: str, taxa_aa: float, du_total: int, vn: float = 1000.0) -> str:
    """Tabela de fluxos para LTN, NTN-F ou NTN-B com regras ANBIMA (truncamentos)."""

    t = tipo.strip().upper().replace(" ", "-")
    r = taxa_aa / 100.0

    flows: list[tuple[int, float, str]] = []

    if t == "LTN":
        titulo = "LTN"
        flows.append((du_total, vn, "principal"))
    elif t in ("NTN-F", "NTNF"):
        titulo = "NTN-F"
        cupom_sem = _round((1.0 + _NTNF_CUPOM_AA / 100.0) ** 0.5 - 1.0, 8)
        dus = _gerar_cupom_dates(du_total)
        last = dus[-1]
        for du in dus:
            if du == last:
                flows.append((du, vn * cupom_sem + vn, "cupom+principal"))
            else:
                flows.append((du, vn * cupom_sem, "cupom"))
    elif t in ("NTN-B", "NTNB"):
        titulo = "NTN-B"
        cupom_sem_pct = _round(((1.0 + _NTNB_CUPOM_AA / 100.0) ** 0.5 - 1.0) * 100, 6)
        cupom_sem = cupom_sem_pct / 100.0
        dus = _gerar_cupom_dates(du_total)
        last = dus[-1]
        for du in dus:
            if du == last:
                flows.append((du, vn * (1.0 + cupom_sem), "cupom+principal"))
            else:
                flows.append((du, vn * cupom_sem, "cupom"))
    else:
        return f'Erro: tipo deve ser "LTN", "NTN-F" ou "NTN-B" (recebido: {tipo}).'

    lines = [
        f"## Fluxo de Caixa — {titulo} (regras ANBIMA)",
        "",
        f"- Taxa de desconto: {_fmt(taxa_aa, 4)}% a.a.",
        f"- DU até vencimento: {du_total}",
        f"- VN/VNA: {_fmt(vn, 2)}",
        "",
        "| # | DU | Evento | Nominal (R$) | Fator (T-14) | PV (R$) T-6 |",
        "|---|---|---|---|---|---|",
    ]

    pv_sum = 0.0
    for idx, (du, nominal, ev) in enumerate(flows, 1):
        fator = _exp_trunc14(1.0 + r, du / 252.0)
        pv = _trunc(nominal / fator, 6)
        pv_sum += pv
        lines.append(f"| {idx} | {du} | {ev} | {_fmt(nominal, 6)} | {_fmt(fator, 14)} | {_fmt(pv, 6)} |")

    pu = _trunc(pv_sum, 6)
    lines += [
        "",
        f"**PU (T-6) = {_fmt(pu, 6)}**",
        f"Fluxos: {len(flows)}",
    ]
    return "\n".join(lines)


def _gerar_cupom_dates(du_total: int, step: int = 126) -> list[int]:
    if du_total <= 0:
        return []
    out: list[int] = []
    d = step
    while d < du_total:
        out.append(d)
        d += step
    out.append(du_total)
    return sorted(set(out))


# ── Referência ────────────────────────────────────────────────────────────────

def ref_titulos_publicos() -> str:
    """Referência rápida: metodologia ANBIMA para cada título público federal."""

    return """## Referência — Títulos Públicos (Metodologia ANBIMA)

### Convenções gerais

- Base: 252 dias úteis, capitalização exponencial
- DU: liquidação (inclusive) até vencimento/pagamento (exclusive)
- Liquidação: D+0 (à vista) ou D+1 (a termo) conforme a negociação
- T = truncado, A = arredondado na casa indicada
- Cotação sempre em % — T-4 aplica-se ao valor percentual (ex: 99,6557%)

### Quadro de truncamentos/arredondamentos

| Variável | LTN | NTN-F | NTN-B | LFT |
|---|---|---|---|---|
| Exponencial | T-14 | T-14 | T-14 | T-14 |
| Cupom semestral | — | A-6 (10% a.a.) | A-6 (6% a.a.) | — |
| Fluxos descontados | — | A-9 | A-10 | — |
| Cotação (%) | — | — | T-4 | T-4 |
| VNA | — | — | T-6 | T-6 |
| PU | T-6 | T-6 | T-6 | T-6 |

### LTN (zero cupom prefixado)

```
PU = 1.000 / (1 + Taxa)^(du/252)   → T-6
```

### NTN-F (prefixado com cupom semestral)

```
Cupom_sem = (1,10)^0,5 - 1 = 4,880885% (A-6)
PU = Σ [Cupom × VN / (1+TIR)^(dui/252)] + VN / (1+TIR)^(dun/252)   → T-6
```
Fluxos descontados: A-9

### NTN-B (IPCA+ com cupom)

```
Cupom_sem = [(1,06)^(6/12) - 1] × 100 = 2,956301% (A-6)
Cotação(%) = Σ [Cupom% / (1+TIR)^(dui/252)] + 100 / (1+TIR)^(dun/252)   → T-4 (%)
PU = (Cotação / 100) × VNA   → T-6
```
Fluxos descontados: A-10

### LFT (Selic)

```
Cotação(%) = 100 / (1 + Rentabilidade/100)^(du/252)   → T-4 (%)
PU = (Cotação / 100) × VNA_Selic   → T-6
```

### Duration ANBIMA

```
Duration = Σ(dui × PUi) / Σ(PUi)
```
Em dias úteis (não em anos). PUi = valor presente do fluxo i."""


# ── VNA ───────────────────────────────────────────────────────────────────────

def calcular_vna_ntnb(
    vna_base_15: float,
    ipca_mes_pct: float,
    data_liquidacao: str,
) -> str:
    """Calcula VNA pro-rata da NTN-B entre dois dias 15 consecutivos.
    vna_base_15 = VNA no dia 15 do mês de referência (ex: 4632,489378)
    ipca_mes_pct = variação IPCA do mês (oficial ou projeção ANBIMA), em % (ex: 0,30)
    data_liquidacao = data de liquidação da operação (à vista D+0 ou a termo D+1)

    Metodologia ANBIMA: VNA = VNA_15 × (1 + IPCA)^(du1/du2)
    du1 = DU do dia 15 ajustado (incl) até liquidação (excl)
    du2 = DU do dia 15 ajustado (incl) até próximo dia 15 (excl)
    Quando o dia 15 não é DU, usa o próximo dia útil."""

    from tools.dias_uteis import _is_business_day, _next_business_day

    liq = _parse_date(data_liquidacao)

    if liq.day >= 15:
        d15_ref = date(liq.year, liq.month, 15)
        next_m = liq.month + 1 if liq.month < 12 else 1
        next_y = liq.year if liq.month < 12 else liq.year + 1
        d15_next = date(next_y, next_m, 15)
    else:
        prev_m = liq.month - 1 if liq.month > 1 else 12
        prev_y = liq.year if liq.month > 1 else liq.year - 1
        d15_ref = date(prev_y, prev_m, 15)
        d15_next = date(liq.year, liq.month, 15)

    d15_adj = d15_ref if _is_business_day(d15_ref) else _next_business_day(d15_ref)

    if liq <= d15_adj:
        vna = _trunc(vna_base_15, 6)
        return "\n".join([
            "## VNA NTN-B",
            "",
            f"Liquidação {liq.strftime('%d/%m/%Y')} coincide com (ou precede) o dia 15 ajustado ({d15_adj.strftime('%d/%m/%Y')}).",
            f"**VNA = {_fmt(vna, 6)}** (sem pro-rata)",
        ])

    du1 = _count_business_days(d15_adj, liq, start_inclusive=True, end_inclusive=False)
    du2 = _count_business_days(d15_adj, d15_next, start_inclusive=True, end_inclusive=False)

    fator_prorata = du1 / du2
    var = ipca_mes_pct / 100.0
    fator = _trunc((1.0 + var) ** fator_prorata, 14)

    vna_raw = vna_base_15 * fator
    vna = _trunc(vna_raw, 6)

    lines = [
        "## VNA NTN-B — Pro-rata IPCA",
        "",
        "**Premissas**",
        "",
        f"- VNA base (dia 15): {_fmt(vna_base_15, 6)}",
        f"- IPCA do mês: {_fmt(ipca_mes_pct, 2)}%",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')}",
        "",
        "**Datas de referência**",
        "",
        f"- Dia 15 referência: {d15_ref.strftime('%d/%m/%Y')}"
        + (f" → ajustado para {d15_adj.strftime('%d/%m/%Y')} (próx. DU)" if d15_adj != d15_ref else ""),
        f"- Próximo dia 15: {d15_next.strftime('%d/%m/%Y')}",
        "",
        "**Pro-rata**",
        "",
        "```",
        "VNA = VNA_15 × (1 + IPCA)^(du1/du2)",
        "```",
        "",
        f"- du1 = DU de {d15_adj.strftime('%d/%m/%Y')} (incl) a {liq.strftime('%d/%m/%Y')} (excl) = **{du1}**",
        f"- du2 = DU de {d15_adj.strftime('%d/%m/%Y')} (incl) a {d15_next.strftime('%d/%m/%Y')} (excl) = **{du2}**",
        f"- Fração pro-rata = {du1}/{du2} = {_fmt(fator_prorata, 14)}",
        f"- (1 + {_fmt(var, 4)})^({_fmt(fator_prorata, 8)}) = {_fmt(fator, 14)} (T-14)",
        "",
        f"VNA = {_fmt(vna_base_15, 6)} × {_fmt(fator, 14)} = {_fmt(vna_raw, 10)} → **{_fmt(vna, 6)}** (T-6)",
        "",
        "**Resultado**",
        "",
        f"| Métrica | Valor |",
        f"|---|---|",
        f"| VNA (T-6) | **{_fmt(vna, 6)}** |",
        f"| Pro-rata | {du1}/{du2} = {_fmt(fator_prorata * 100, 4)}% do mês |",
    ]
    return "\n".join(lines)


# ── Registro ──────────────────────────────────────────────────────────────────

def register(mcp: "FastMCP") -> None:
    """Registra as ferramentas de títulos públicos na instância FastMCP."""
    mcp.tool()(precificar_ltn)
    mcp.tool()(precificar_ntnf)
    mcp.tool()(precificar_ntnb)
    mcp.tool()(precificar_lft)
    mcp.tool()(fluxo_caixa_titulo)
    mcp.tool()(calcular_vna_ntnb)
    mcp.tool()(ref_titulos_publicos)
