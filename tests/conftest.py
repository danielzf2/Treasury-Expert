"""Fixtures principais para a suite de testes.

Tres camadas de fixtures:
1. Datas: data_neg fixa em 29/04/2026 (terca, DU), liq = 30/04/2026 (D+1)
2. Mercado mockado: curvas DI/DAP/FRC/DDI/DOL determinísticas
3. Pernas processadas: invoca _process_raw_legs + _expand_hedge_legs
"""

from __future__ import annotations

from datetime import date

import pytest

# Imports do app
from lib.market_data import MarketSnapshot
from lib.calendar import default_liq_date, parse_ticker
from api import simulator as sim_api
from api.simulator import _process_raw_legs, _expand_hedge_legs

from tests.presets import PRESETS_INPUT


# ----------------------------------------------------------------------------
# Tolerancias globais (documentadas no plano)
# ----------------------------------------------------------------------------

TOL_PU = 1e-3        # PU em R$ (acomoda T-6 ANBIMA, zero-coupon e exp252)
TOL_PU_NTNB = 1.0    # PU NTN-B (cot T-4 x VNA T-6 acumula ~0.5 R$)
TOL_PU_LFT = 1.0     # PU LFT (cot T-4 x VNA T-6)
TOL_COTACAO = 1e-4   # cotacao em % (acomoda T-4)
TOL_DURATION = 1e-6  # duration em anos
TOL_DV01_REL = 1e-6  # rel tolerance DV01
TOL_PNL = 0.01       # P&L em R$
TOL_CUPOM = 1e-4     # cupom cambial implicito %


# ----------------------------------------------------------------------------
# Datas e spot
# ----------------------------------------------------------------------------

DATA_NEG_STR = "2026-04-29"
DATA_NEG = date(2026, 4, 29)
LIQ_DATE = default_liq_date(DATA_NEG)  # 30/04/2026 (DU seguinte)

SPOT = 4.9724


@pytest.fixture(scope="session")
def data_neg_str() -> str:
    return DATA_NEG_STR


@pytest.fixture(scope="session")
def data_neg() -> date:
    return DATA_NEG


@pytest.fixture(scope="session")
def liq_date() -> date:
    return LIQ_DATE


@pytest.fixture(scope="session")
def spot() -> float:
    return SPOT


# ----------------------------------------------------------------------------
# Mercado mockado: curvas determinísticas com tickers usados pelos presets
# ----------------------------------------------------------------------------

# Tickers e taxas DI1 — escolhidos para cobrir os presets
# Formato {symb, vcto (YYYY-MM-DD), last, ajuste}
def _di1_curve() -> list[dict]:
    """Curva DI1 sintetica cobrindo K26, F28, F31, F32 + vertices intermediarios."""
    return [
        {"symb": "DI1K26", "vcto": "2026-05-04", "last": 14.500, "ajuste": 14.500},
        {"symb": "DI1N26", "vcto": "2026-07-01", "last": 14.550, "ajuste": 14.550},
        {"symb": "DI1V26", "vcto": "2026-10-01", "last": 14.480, "ajuste": 14.480},
        {"symb": "DI1F27", "vcto": "2027-01-04", "last": 14.350, "ajuste": 14.350},
        {"symb": "DI1N27", "vcto": "2027-07-01", "last": 14.100, "ajuste": 14.100},
        {"symb": "DI1F28", "vcto": "2028-01-03", "last": 13.900, "ajuste": 13.900},
        {"symb": "DI1N28", "vcto": "2028-07-03", "last": 13.800, "ajuste": 13.800},
        {"symb": "DI1F29", "vcto": "2029-01-02", "last": 13.750, "ajuste": 13.750},
        {"symb": "DI1F30", "vcto": "2030-01-02", "last": 13.700, "ajuste": 13.700},
        {"symb": "DI1F31", "vcto": "2031-01-02", "last": 13.680, "ajuste": 13.680},
        {"symb": "DI1F32", "vcto": "2032-01-02", "last": 13.650, "ajuste": 13.650},
        {"symb": "DI1F33", "vcto": "2033-01-03", "last": 13.640, "ajuste": 13.640},
        {"symb": "DI1F35", "vcto": "2035-01-02", "last": 13.620, "ajuste": 13.620},
    ]


def _dap_curve() -> list[dict]:
    """Curva DAP sintetica para NTN-B+DAP (N29 etc)."""
    return [
        {"symb": "DAPK26", "vcto": "2026-05-04", "last": 7.800, "ajuste": 7.800},
        {"symb": "DAPN26", "vcto": "2026-07-01", "last": 7.750, "ajuste": 7.750},
        {"symb": "DAPN27", "vcto": "2027-07-01", "last": 7.600, "ajuste": 7.600},
        {"symb": "DAPN28", "vcto": "2028-07-03", "last": 7.500, "ajuste": 7.500},
        {"symb": "DAPN29", "vcto": "2029-07-02", "last": 7.400, "ajuste": 7.400},
        {"symb": "DAPN30", "vcto": "2030-07-01", "last": 7.380, "ajuste": 7.380},
        {"symb": "DAPN32", "vcto": "2032-07-01", "last": 7.350, "ajuste": 7.350},
        {"symb": "DAPN35", "vcto": "2035-07-02", "last": 7.300, "ajuste": 7.300},
    ]


def _frc_curve() -> list[dict]:
    """Curva FRC sintetica."""
    return [
        {"symb": "FRCK26", "vcto": "2026-05-04", "last": 5.150, "ajuste": 5.150},
        {"symb": "FRCN26", "vcto": "2026-07-01", "last": 5.120, "ajuste": 5.120},
        {"symb": "FRCV26", "vcto": "2026-10-01", "last": 5.080, "ajuste": 5.080},
        {"symb": "FRCF27", "vcto": "2027-01-04", "last": 5.060, "ajuste": 5.060},
        {"symb": "FRCF28", "vcto": "2028-01-03", "last": 5.060, "ajuste": 5.060},
        {"symb": "FRCF29", "vcto": "2029-01-02", "last": 5.040, "ajuste": 5.040},
    ]


def _ddi_curve() -> list[dict]:
    """Curva DDI sintetica."""
    return [
        {"symb": "DDIK26", "vcto": "2026-05-04", "last": 5.150, "ajuste": 5.150},
        {"symb": "DDIN26", "vcto": "2026-07-01", "last": 5.120, "ajuste": 5.120},
        {"symb": "DDIF27", "vcto": "2027-01-04", "last": 5.080, "ajuste": 5.080},
    ]


def _dol_curve() -> list[dict]:
    """Curva DOL sintetica (cotacao em pontos = R$/1000USD)."""
    return [
        {"symb": "DOLK26", "vcto": "2026-05-04", "last": 4976.5, "ajuste": 4976.5},
        {"symb": "DOLM26", "vcto": "2026-06-01", "last": 5005.0, "ajuste": 5005.0},
        {"symb": "DOLN26", "vcto": "2026-07-01", "last": 5035.0, "ajuste": 5035.0},
        {"symb": "DOLU26", "vcto": "2026-09-01", "last": 5095.0, "ajuste": 5095.0},
    ]


@pytest.fixture(scope="session")
def market_snap() -> MarketSnapshot:
    """Snapshot de mercado mockado, deterministico."""
    snap = MarketSnapshot()
    snap.timestamp = "29/04/2026 10:00:00"
    snap.cdi_over_dia = 0.05103  # ~13.65% a.a.
    snap.cdi_aa = 13.65
    snap.ptax = 4.9724
    snap.spot_usd = 4.9724
    snap.di1 = _di1_curve()
    snap.dap = _dap_curve()
    snap.frc = _frc_curve()
    snap.ddi = _ddi_curve()
    snap.dol = _dol_curve()
    return snap


@pytest.fixture(scope="session")
def di1_curve() -> list[dict]:
    return _di1_curve()


@pytest.fixture(scope="session")
def dap_curve() -> list[dict]:
    return _dap_curve()


@pytest.fixture(scope="session")
def frc_curve() -> list[dict]:
    return _frc_curve()


@pytest.fixture(autouse=True)
def _patch_market_cache(market_snap, monkeypatch):
    """Patch sim_api._market_cache para evitar HTTP em fetch_all()."""
    monkeypatch.setitem(sim_api._market_cache, "snap", market_snap)
    monkeypatch.setitem(sim_api._market_cache, "ts", 1e18)  # never expires
    yield


# ----------------------------------------------------------------------------
# Pernas processadas (factory por preset)
# ----------------------------------------------------------------------------

def _enrich_legs_with_venc(legs: list[dict]) -> list[dict]:
    """Adiciona campo 'venc' (date) extraido de parsed.date para uso pelo oracle."""
    for l in legs:
        parsed = l.get("parsed") or {}
        if isinstance(parsed, dict):
            l["venc"] = parsed.get("date")
    return legs


@pytest.fixture(scope="session")
def processed_legs_factory(market_snap):
    """Factory que processa pernas de um preset, retornando lista enriquecida."""

    def _factory(preset_name: str, hedge_mode: str | None = None) -> list[dict]:
        legs_input = [dict(leg) for leg in PRESETS_INPUT[preset_name]]
        if hedge_mode:
            for leg in legs_input:
                leg["hedge_mode"] = hedge_mode
        valid = _process_raw_legs(legs_input, DATA_NEG_STR, SPOT)
        valid = _expand_hedge_legs(valid, market_snap.di1, market_snap.dap, DATA_NEG_STR, SPOT)
        return _enrich_legs_with_venc(valid)

    return _factory


@pytest.fixture(scope="session")
def all_processed_legs(processed_legs_factory):
    """Mapa preset_name -> lista de pernas processadas (sem hedge auto)."""
    return {name: processed_legs_factory(name) for name in PRESETS_INPUT}
