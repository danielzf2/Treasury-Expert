"""
ANBIMA daily bond pricing service.

Fetches and parses the daily TXT file from ANBIMA with indicative rates
and PUs for all federal government bonds (LTN, LFT, NTN-B, NTN-F, NTN-C).

Uses lazy in-memory cache: fetches on first request of the day, serves
from cache for subsequent requests. No cron needed.

URL pattern: https://www.anbima.com.br/informacoes/merc-sec/arqs/ms{YYMMDD}.txt
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass
from datetime import date, timedelta
from typing import Any

import httpx

from tools.dias_uteis import _is_business_day

log = logging.getLogger("anbima-service")

MONTH_LABELS = {
    1: "jan", 2: "fev", 3: "mar", 4: "abr", 5: "mai", 6: "jun",
    7: "jul", 8: "ago", 9: "set", 10: "out", 11: "nov", 12: "dez",
}


@dataclass
class AnbimaBond:
    type: str
    reference_date: str
    selic_code: str
    emission_date: str
    maturity: str
    maturity_label: str
    buy_rate: float | None
    sell_rate: float | None
    indicative_rate: float | None
    pu: float | None
    std_dev: float | None
    criterion: str


_cache: dict[str, Any] = {"date": None, "data": None}


def _parse_br_float(s: str) -> float | None:
    s = s.strip()
    if not s:
        return None
    cleaned = s.replace(".", "").replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None


def _format_date_iso(yyyymmdd: str) -> str:
    return f"{yyyymmdd[:4]}-{yyyymmdd[4:6]}-{yyyymmdd[6:8]}"


def _maturity_label(iso_date: str) -> str:
    parts = iso_date.split("-")
    month = int(parts[1])
    year = parts[0]
    return f"{MONTH_LABELS.get(month, parts[1])}/{year}"


def _resolve_reference_date() -> date:
    d = date.today() - timedelta(days=1)
    for _ in range(10):
        if _is_business_day(d):
            return d
        d -= timedelta(days=1)
    return d


def _build_url(ref: date) -> str:
    yy = str(ref.year)[2:]
    mm = f"{ref.month:02d}"
    dd = f"{ref.day:02d}"
    return f"https://www.anbima.com.br/informacoes/merc-sec/arqs/ms{yy}{mm}{dd}.txt"


def _parse_line(parts: list[str]) -> AnbimaBond | None:
    if len(parts) < 9:
        return None

    tipo = parts[0].strip()
    ref_date = parts[1].strip()
    selic_code = parts[2].strip()
    emission_raw = parts[3].strip()
    maturity_raw = parts[4].strip()

    maturity_iso = _format_date_iso(maturity_raw)

    emission_iso = ""
    if len(emission_raw) == 8 and emission_raw.isdigit():
        emission_iso = _format_date_iso(emission_raw)
    else:
        emission_iso = emission_raw

    return AnbimaBond(
        type=tipo,
        reference_date=_format_date_iso(ref_date),
        selic_code=selic_code,
        emission_date=emission_iso,
        maturity=maturity_iso,
        maturity_label=_maturity_label(maturity_iso),
        buy_rate=_parse_br_float(parts[5]) if len(parts) > 5 else None,
        sell_rate=_parse_br_float(parts[6]) if len(parts) > 6 else None,
        indicative_rate=_parse_br_float(parts[7]) if len(parts) > 7 else None,
        pu=_parse_br_float(parts[8]) if len(parts) > 8 else None,
        std_dev=_parse_br_float(parts[9]) if len(parts) > 9 else None,
        criterion=parts[14].strip() if len(parts) > 14 else "",
    )


async def _fetch_and_parse(ref: date) -> list[AnbimaBond]:
    url = _build_url(ref)
    log.info("Fetching ANBIMA file: %s", url)

    async with httpx.AsyncClient(timeout=15.0) as client:
        resp = await client.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/plain,*/*",
            "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
        })
        resp.raise_for_status()

    text = resp.text
    lines = [l for l in text.split("\n") if l.strip()]

    if len(lines) < 3:
        raise ValueError(f"ANBIMA file for {ref} has fewer than 3 lines")

    bonds: list[AnbimaBond] = []
    for line in lines[2:]:
        parts = line.split("@")
        bond = _parse_line(parts)
        if bond:
            bonds.append(bond)

    log.info("Parsed %d bonds from ANBIMA file for %s", len(bonds), ref)
    return bonds


async def get_anbima_bonds(force_refresh: bool = False) -> dict[str, Any]:
    today = date.today()

    if not force_refresh and _cache["date"] == today and _cache["data"] is not None:
        return _cache["data"]

    last_error = None
    ref = _resolve_reference_date()

    for attempt in range(5):
        try:
            bonds = await _fetch_and_parse(ref)
            result = {
                "reference_date": ref.isoformat(),
                "bonds": [_bond_to_dict(b) for b in bonds],
            }
            _cache["date"] = today
            _cache["data"] = result
            return result
        except Exception as e:
            last_error = e
            log.warning("ANBIMA fetch failed for %s (attempt %d): %s", ref, attempt + 1, e)
            ref -= timedelta(days=1)
            while not _is_business_day(ref):
                ref -= timedelta(days=1)

    raise RuntimeError(f"Could not fetch ANBIMA data after 5 attempts: {last_error}")


def _bond_to_dict(b: AnbimaBond) -> dict[str, Any]:
    return {
        "type": b.type,
        "maturity": b.maturity,
        "maturity_label": b.maturity_label,
        "selic_code": b.selic_code,
        "emission_date": b.emission_date,
        "indicative_rate": b.indicative_rate,
        "pu": b.pu,
        "buy_rate": b.buy_rate,
        "sell_rate": b.sell_rate,
        "std_dev": b.std_dev,
        "criterion": b.criterion,
    }


# ── VNA (Valor Nominal Atualizado) ──────────────────────────────────────────
# Source: brasilindicadores.com.br (server-rendered HTML, no auth required)

VNA_URL = "https://brasilindicadores.com.br/titulos-publicos/vna/"

_vna_cache: dict[str, Any] = {"date": None, "data": None}

_H2_TO_TYPE: dict[str, str] = {
    "NTN-B": "NTN-B",
    "NTN-C": "NTN-C",
    "LFT": "LFT",
}

_SECTION_RE = re.compile(
    r"<h2>(.*?)</h2>.*?<tbody>(.*?)</tbody>",
    re.DOTALL,
)

_TD_RE = re.compile(r"<td[^>]*>(.*?)</td>", re.DOTALL)


def _clean_html(s: str) -> str:
    s = s.strip()
    s = s.replace("&#xF3;", "ó").replace("&#xEA;", "ê")
    s = s.replace("&#xE1;", "á").replace("&#x2B;", "+")
    s = re.sub(r"<[^>]+>", "", s)
    return s.strip()


def _parse_vna_value(s: str) -> float | None:
    s = s.replace("R$", "").strip()
    return _parse_br_float(s)


def _parse_index_field(raw: str) -> dict[str, Any]:
    projected = "projetado" in raw.lower()
    pct_match = re.search(r"([\d.,]+)%", raw)
    value = _parse_br_float(pct_match.group(1)) if pct_match else None
    return {"value": value, "projected": projected, "raw": raw}


async def _fetch_vna_page() -> str:
    async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
        resp = await client.get(VNA_URL, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "text/html,*/*",
            "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8",
        })
        resp.raise_for_status()
    return resp.text


def _parse_vna_html(html: str) -> tuple[dict[str, float], dict[str, Any]]:
    vna_flat: dict[str, float] = {}
    entries: dict[str, Any] = {}

    for section in _SECTION_RE.finditer(html):
        h2 = _clean_html(section.group(1))
        tbody = section.group(2)

        bond_type: str | None = None
        for prefix, btype in _H2_TO_TYPE.items():
            if prefix in h2:
                bond_type = btype
                break
        if not bond_type:
            continue

        tds = [_clean_html(td.group(1)) for td in _TD_RE.finditer(tbody)]
        if len(tds) < 3:
            continue

        vna_val = _parse_vna_value(tds[2])
        entry: dict[str, Any] = {
            "selic_code": tds[0],
            "reference_date": tds[1],
            "vna": vna_val,
        }

        if bond_type in ("NTN-B", "NTN-C") and len(tds) >= 5:
            idx = _parse_index_field(tds[3])
            entry["index_name"] = "IPCA" if bond_type == "NTN-B" else "IGP-M"
            entry["index_value"] = idx["value"]
            entry["index_projected"] = idx["projected"]
            entry["index_raw"] = idx["raw"]
            entry["valid_from"] = tds[4]
        elif bond_type == "LFT" and len(tds) >= 4:
            idx = _parse_index_field(tds[3])
            entry["index_name"] = "SELIC"
            entry["index_value"] = idx["value"]
            entry["index_projected"] = idx.get("projected", False)
            entry["index_raw"] = idx["raw"]

        entries[bond_type] = entry
        if vna_val is not None:
            vna_flat[bond_type] = vna_val

    return vna_flat, entries


async def get_vna(force_refresh: bool = False) -> dict[str, Any]:
    today = date.today()

    if not force_refresh and _vna_cache["date"] == today and _vna_cache["data"] is not None:
        return _vna_cache["data"]

    try:
        html = await _fetch_vna_page()
        vna_flat, entries = _parse_vna_html(html)

        if not vna_flat:
            raise ValueError("Could not parse any VNA values from brasilindicadores")

        ref_date = next(
            (e["reference_date"] for e in entries.values() if "reference_date" in e),
            today.isoformat(),
        )

        result: dict[str, Any] = {
            "reference_date": ref_date,
            "vna": vna_flat,
            "entries": entries,
        }

        _vna_cache["date"] = today
        _vna_cache["data"] = result
        log.info("Fetched VNA from brasilindicadores: %s", vna_flat)
        return result

    except Exception as e:
        if _vna_cache["data"] is not None:
            log.warning("VNA fetch failed, using cached data: %s", e)
            return _vna_cache["data"]
        raise RuntimeError(f"Could not fetch VNA: {e}")
