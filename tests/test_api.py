"""Integration via FastAPI TestClient para /sim/* endpoints.

Testa shape e consistencia dos endpoints:
- GET  /sim/presets
- POST /sim/process
- POST /sim/mtm-table
- POST /sim/charts/{curve, pnl-bars, pnl-consolidated, pnl-per-leg}
- GET  /sim/tickers/{instrument}

Usa o mock de market_snap via conftest._patch_market_cache.
"""

from __future__ import annotations

import json

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.simulator import router as sim_router

from tests.conftest import DATA_NEG_STR, SPOT
from tests.presets import PRESETS_INPUT, PRESET_NAMES


@pytest.fixture(scope="session")
def client(market_snap):
    """FastAPI TestClient com sim_router e market mockado."""
    app = FastAPI()
    app.include_router(sim_router, prefix="/sim")
    return TestClient(app)


# ============================================================================
# 1. GET /sim/presets
# ============================================================================

def test_get_presets(client):
    resp = client.get("/sim/presets")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # Todos os 8 presets esperados
    for name in PRESET_NAMES:
        assert name in data
        assert isinstance(data[name], list)
        assert len(data[name]) == len(PRESETS_INPUT[name])


# ============================================================================
# 2. POST /sim/process
# ============================================================================

@pytest.mark.parametrize("preset_name", PRESET_NAMES)
def test_process_preset(client, market_snap, preset_name):
    """POST /sim/process retorna JSON valido com legs, strategy, total_dv01."""
    payload = {
        "legs": PRESETS_INPUT[preset_name],
        "data_neg": DATA_NEG_STR,
        "spot": SPOT,
        "di1": market_snap.di1,
        "dap": market_snap.dap,
    }
    resp = client.post("/sim/process", json=payload)
    assert resp.status_code == 200, resp.text
    data = resp.json()

    # Shape
    assert "legs" in data
    assert "strategy" in data
    assert "risk_factors" in data
    assert "total_corr" in data
    assert "total_corr_bps" in data
    assert "total_dv01" in data
    assert "total_fin" in data
    assert "hedge" in data

    # Legs count
    assert len(data["legs"]) == len(PRESETS_INPUT[preset_name])

    # Cada perna tem campos esperados
    for leg in data["legs"]:
        assert "instrument" in leg
        assert "pu" in leg
        assert "du" in leg
        assert "dc" in leg
        assert "fin" in leg
        assert "noc" in leg
        assert "d_mac" in leg
        assert "dv01_unit" in leg
        assert "dv01_total" in leg

    # Strategy nao vazia
    assert isinstance(data["strategy"], dict)
    assert "result" in data["strategy"] or "type" in data["strategy"]

    # Risk factors nao vazio
    assert len(data["risk_factors"]) > 0


def test_process_no_legs_returns_400(client, market_snap):
    """POST /sim/process com legs vazias retorna 400."""
    payload = {
        "legs": [],
        "data_neg": DATA_NEG_STR,
        "spot": SPOT,
        "di1": market_snap.di1,
        "dap": market_snap.dap,
    }
    resp = client.post("/sim/process", json=payload)
    assert resp.status_code == 400


@pytest.mark.parametrize("preset_name", ["Casada NTN-F+DI1", "Casada NTN-B+DAP"])
def test_process_includes_hedge_for_coupon(client, market_snap, preset_name):
    """Presets com TPF cupom devem retornar hedge nao-None."""
    payload = {
        "legs": PRESETS_INPUT[preset_name],
        "data_neg": DATA_NEG_STR,
        "spot": SPOT,
        "di1": market_snap.di1,
        "dap": market_snap.dap,
    }
    resp = client.post("/sim/process", json=payload)
    assert resp.status_code == 200
    data = resp.json()

    assert data["hedge"] is not None
    assert "n_at_duration" in data["hedge"]
    assert "n_at_maturity" in data["hedge"]
    assert "strip" in data["hedge"]


# ============================================================================
# 3. POST /sim/mtm-table
# ============================================================================

@pytest.mark.parametrize("preset_name", PRESET_NAMES)
def test_mtm_table_endpoint(client, market_snap, preset_name):
    """POST /sim/mtm-table retorna table com 13 linhas."""
    # Primeiro processa as legs
    proc_payload = {
        "legs": PRESETS_INPUT[preset_name],
        "data_neg": DATA_NEG_STR,
        "spot": SPOT,
        "di1": market_snap.di1,
        "dap": market_snap.dap,
    }
    proc = client.post("/sim/process", json=proc_payload).json()

    payload = {
        "legs": proc["legs"],
        "scenario_key": "bear_par",
        "magnitude": 10.0,
        "di1": market_snap.di1,
        "dap": market_snap.dap,
    }
    resp = client.post("/sim/mtm-table", json=payload)
    assert resp.status_code == 200, resp.text
    data = resp.json()
    assert "table" in data
    assert len(data["table"]) == 13
    assert "total_pnl" in data
    assert "flow_pnl" in data


# ============================================================================
# 4. POST /sim/charts/*
# ============================================================================

CHART_ENDPOINTS = ["curve", "pnl-bars", "pnl-consolidated", "pnl-per-leg"]


@pytest.mark.parametrize("chart", CHART_ENDPOINTS)
@pytest.mark.parametrize("preset_name", ["Casada LTN+DI1", "DOL+DI1 (cupom sint.)"])
def test_chart_endpoint_returns_plotly_json(client, market_snap, chart, preset_name):
    """POST /sim/charts/{chart} retorna JSON Plotly valido."""
    proc_payload = {
        "legs": PRESETS_INPUT[preset_name],
        "data_neg": DATA_NEG_STR,
        "spot": SPOT,
        "di1": market_snap.di1,
        "dap": market_snap.dap,
    }
    proc = client.post("/sim/process", json=proc_payload).json()

    payload = {
        "legs": proc["legs"],
        "scenario_key": "bear_par",
        "magnitude": 10.0,
        "di1": market_snap.di1,
        "dap": market_snap.dap,
    }
    resp = client.post(f"/sim/charts/{chart}", json=payload)
    assert resp.status_code == 200, resp.text
    data = resp.json()
    # Plotly figure JSON tem 'data' e 'layout'
    assert "data" in data
    assert "layout" in data
    assert isinstance(data["data"], list)


# ============================================================================
# 5. GET /sim/tickers/{instrument}
# ============================================================================

@pytest.mark.parametrize("instrument", ["DI1", "DAP", "FRC", "DDI", "DOL"])
def test_tickers_endpoint(client, instrument):
    """GET /sim/tickers/{inst} retorna tickers do market mockado."""
    resp = client.get(f"/sim/tickers/{instrument}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["instrument"] == instrument
    assert isinstance(data["tickers"], list)
    # market_snap tem ao menos 1 contrato pra cada
    assert len(data["tickers"]) >= 1


@pytest.mark.parametrize("instrument", ["LTN", "NTN-F", "NTN-B", "LFT"])
def test_tickers_tpf(client, instrument):
    """GET /sim/tickers/{tpf} retorna lista (vencimentos hardcoded)."""
    resp = client.get(f"/sim/tickers/{instrument}")
    assert resp.status_code == 200
    data = resp.json()
    assert data["instrument"] == instrument
    assert isinstance(data["tickers"], list)


# ============================================================================
# 6. Cross-validation: process + mtm-table consistente com calculo direto
# ============================================================================

@pytest.mark.parametrize("preset_name", ["Casada LTN+DI1", "LTN direcional"])
def test_process_mtm_consistency(client, market_snap, preset_name):
    """total_pnl da MtM em delta=0 deve ser ~0 R$."""
    proc_payload = {
        "legs": PRESETS_INPUT[preset_name],
        "data_neg": DATA_NEG_STR,
        "spot": SPOT,
        "di1": market_snap.di1,
        "dap": market_snap.dap,
    }
    proc = client.post("/sim/process", json=proc_payload).json()

    payload = {
        "legs": proc["legs"],
        "scenario_key": "bear_par",
        "magnitude": 0.0,
        "di1": market_snap.di1,
        "dap": market_snap.dap,
    }
    resp = client.post("/sim/mtm-table", json=payload)
    data = resp.json()

    # Linha delta=0 deve dar P&L 0
    zero = next(r for r in data["table"] if r["delta"] == 0)
    assert zero["total"] == pytest.approx(0.0, abs=0.05)
    assert data["total_pnl"] == pytest.approx(0.0, abs=0.05)
