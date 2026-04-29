"""
Cálculo de dias úteis conforme convenção ANBIMA.
Feriados carregados de server/data/feriados_anbima.json (2001–2099).

Convenção ANBIMA para títulos públicos:
  DU = dias úteis entre a data de LIQUIDAÇÃO (inclusive) e a data de vencimento (exclusive)
  Liquidação pode ser D+0 (à vista) ou D+1 (a termo), conforme a negociação.
"""

from __future__ import annotations

import json
from datetime import date, timedelta
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from fastmcp import FastMCP

_DATA_DIR = Path(__file__).resolve().parent.parent / "data"
_HOLIDAYS: set[date] | None = None


def _load_holidays() -> set[date]:
    global _HOLIDAYS
    if _HOLIDAYS is not None:
        return _HOLIDAYS
    path = _DATA_DIR / "feriados_anbima.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    _HOLIDAYS = {date.fromisoformat(d) for d in data["dates"]}
    return _HOLIDAYS


def _is_business_day(d: date) -> bool:
    if d.weekday() >= 5:
        return False
    return d not in _load_holidays()


def _count_business_days(start: date, end: date, start_inclusive: bool = True, end_inclusive: bool = False) -> int:
    """Conta dias úteis entre duas datas.
    Padrão ANBIMA: start inclusive, end exclusive."""
    if start > end:
        return -_count_business_days(end, start, start_inclusive=not end_inclusive, end_inclusive=not start_inclusive)
    count = 0
    d = start
    while d < end:
        if _is_business_day(d):
            count += 1
        d += timedelta(days=1)
    if end_inclusive and d == end and _is_business_day(d):
        count += 1
    if not start_inclusive and _is_business_day(start):
        count -= 1
    return count


def _next_business_day(d: date) -> date:
    d = d + timedelta(days=1)
    while not _is_business_day(d):
        d += timedelta(days=1)
    return d


def _prev_business_day(d: date) -> date:
    d = d - timedelta(days=1)
    while not _is_business_day(d):
        d -= timedelta(days=1)
    return d


def _parse_date(s: str) -> date:
    s = s.strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%d-%m-%Y"):
        try:
            return date.fromisoformat(s) if fmt == "%Y-%m-%d" else date(*[int(x) for x in (s.split("/") if "/" in s else s.split("-"))][::-1])
        except (ValueError, IndexError):
            continue
    raise ValueError(f"Data inválida: {s}. Use YYYY-MM-DD ou DD/MM/YYYY.")


# ── MCP Tools ─────────────────────────────────────────────────────────────────

def dias_uteis_entre(data_inicio: str, data_fim: str) -> str:
    """Calcula dias úteis entre duas datas (calendário ANBIMA).
    Convenção padrão: data_inicio inclusive, data_fim exclusive.
    Aceita formatos YYYY-MM-DD ou DD/MM/YYYY."""

    d1 = _parse_date(data_inicio)
    d2 = _parse_date(data_fim)
    du = _count_business_days(d1, d2, start_inclusive=True, end_inclusive=False)

    dc = (d2 - d1).days

    lines = [
        "## Dias Úteis (calendário ANBIMA)",
        "",
        f"- Data início: {d1.strftime('%d/%m/%Y')} ({'du' if _is_business_day(d1) else 'não-útil'}) — **inclusive**",
        f"- Data fim: {d2.strftime('%d/%m/%Y')} ({'du' if _is_business_day(d2) else 'não-útil'}) — **exclusive**",
        f"- Dias corridos: {dc}",
        f"- **Dias úteis: {du}**",
        "",
        "Convenção: ANBIMA padrão (início inclusive, fim exclusive).",
    ]
    return "\n".join(lines)


def dias_uteis_anbima(data_liquidacao: str, data_vencimento: str) -> str:
    """Calcula DU para precificação de títulos públicos conforme ANBIMA.
    DU = dias úteis entre a data de liquidação (inclusive) e a data de vencimento (exclusive).
    A data de liquidação depende da negociação: D+0 (à vista) ou D+1 (a termo).
    A planilha ANBIMA de taxas indicativas usa liquidação à vista (D+0)."""

    liq = _parse_date(data_liquidacao)
    venc = _parse_date(data_vencimento)
    du = _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)
    dc = (venc - liq).days

    lines = [
        "## DU ANBIMA — Títulos Públicos",
        "",
        f"- Data liquidação: {liq.strftime('%d/%m/%Y')} — **inclusive**",
        f"- Data vencimento: {venc.strftime('%d/%m/%Y')} — **exclusive**",
        "",
        f"- Dias corridos: {dc}",
        f"- **DU = {du}**",
    ]
    return "\n".join(lines)


def proximo_dia_util(data: str) -> str:
    """Retorna o próximo dia útil a partir de uma data (calendário ANBIMA)."""
    d = _parse_date(data)
    if _is_business_day(d):
        nxt = _next_business_day(d)
        return f"{d.strftime('%d/%m/%Y')} já é dia útil.\nPróximo DU: {nxt.strftime('%d/%m/%Y')}"
    else:
        nxt = d
        while not _is_business_day(nxt):
            nxt += timedelta(days=1)
        return f"{d.strftime('%d/%m/%Y')} NÃO é dia útil.\nPróximo DU: {nxt.strftime('%d/%m/%Y')}"


def verificar_dia_util(data: str) -> str:
    """Verifica se uma data é dia útil no calendário ANBIMA."""
    d = _parse_date(data)
    holidays = _load_holidays()
    is_weekend = d.weekday() >= 5
    is_holiday = d in holidays

    status = "DIA ÚTIL" if _is_business_day(d) else "NÃO É DIA ÚTIL"
    motivo = ""
    if is_weekend:
        dias = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]
        motivo = f" ({dias[d.weekday()]})"
    elif is_holiday:
        motivo = " (feriado ANBIMA)"

    return f"{d.strftime('%d/%m/%Y')}: **{status}**{motivo}"


def listar_feriados_ano(ano: int) -> str:
    """Lista todos os feriados ANBIMA de um ano."""
    holidays = _load_holidays()
    year_holidays = sorted(d for d in holidays if d.year == ano)

    if not year_holidays:
        return f"Nenhum feriado ANBIMA encontrado para {ano}. Base cobre 2001–2099."

    dias_semana = ["seg", "ter", "qua", "qui", "sex", "sáb", "dom"]
    lines = [
        f"## Feriados ANBIMA — {ano} ({len(year_holidays)} feriados)",
        "",
        "| Data | Dia |",
        "|---|---|",
    ]
    for d in year_holidays:
        lines.append(f"| {d.strftime('%d/%m/%Y')} | {dias_semana[d.weekday()]} |")

    return "\n".join(lines)


def ref_dias_uteis() -> str:
    """Referência rápida: convenções de dias úteis ANBIMA."""
    return """## Referência — Dias Úteis (ANBIMA)

### Convenção para títulos públicos

```
DU = dias úteis entre liquidação (inclusive) e vencimento (exclusive)
```

- Liquidação = data em que ocorre a liquidação financeira
- À vista: liquidação = D+0 (mesmo dia da negociação)
- A termo: liquidação = D+1 (próximo dia útil)
- A planilha ANBIMA de taxas indicativas usa liquidação à vista (D+0)
- NÃO conta a data de vencimento/pagamento

### Calendário ANBIMA

- Feriados nacionais conforme Resolução 2.596/99 do CMN
- NÃO inclui feriados municipais
- NÃO inclui dias de eleição
- Último dia útil do ano: sem atendimento ao público (Res. 2.596/99)
- Base de dados: 2001 a 2099 (1.264 feriados)

### Convenções de contagem

| Base | Uso | Capitalização |
|---|---|---|
| 252 du | Taxas pré, DI, Selic | Exponencial |
| 360 dc | Cupom cambial, DDI, FRC | Linear |
| 365 dc | Algumas taxas internacionais | Linear |

### Exemplo (à vista)

Negociação/Liquidação: 15/01/2025 (quarta) — inclusive
Vencimento: 01/07/2025 (terça) — exclusive
DU = dias úteis de 15/01 a 01/07 (contando 15/01, sem contar 01/07)"""


def register(mcp: "FastMCP") -> None:
    mcp.tool()(dias_uteis_entre)
    mcp.tool()(dias_uteis_anbima)
    mcp.tool()(proximo_dia_util)
    mcp.tool()(verificar_dia_util)
    mcp.tool()(listar_feriados_ano)
    mcp.tool()(ref_dias_uteis)
