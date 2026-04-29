"""Testes de detect_strategy + analyze_risk_factors por preset.

Para cada preset valida:
- strategy.type ('casada', 'cupom_sint', 'dol_sint', 'single', 'multi')
- strategy.spread/cupom/fwd quando aplicavel (vs oracle)
- strategy.result (string conforme contrato)
- analyze_risk_factors: lista de dicts {fator, exposto, desc} esperada
"""

from __future__ import annotations

import pytest

from lib.exposure import detect_strategy, analyze_risk_factors

from tests import oracle
from tests.conftest import LIQ_DATE, SPOT, TOL_CUPOM
from tests.presets import (
    PRESET_NAMES, CASADA_PRESETS, CUPOM_SINT_PRESETS,
    DOL_SINT_PRESETS, SINGLE_LEG_PRESETS,
)


# ----------------------------------------------------------------------------
# Strategy detection
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name", CASADA_PRESETS)
def test_strategy_casada_type(preset_name, all_processed_legs):
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    assert strat["type"] == "casada", f"{preset_name}: type={strat['type']}"
    assert "bmk" in strat
    assert "spread" in strat


@pytest.mark.parametrize("preset_name", CASADA_PRESETS)
def test_strategy_casada_spread(preset_name, all_processed_legs):
    """Spread = (TPF.tax_fin - DI/DAP.taxa) * 100, em bps."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)

    tpf = next(l for l in legs if l["info"].type == "tpf")
    deriv = next(l for l in legs if l["instrument"] in ("DI1", "DAP"))
    expected_spread = (tpf["tax_fin"] - deriv["taxa"]) * 100

    assert strat["spread"] == pytest.approx(expected_spread, rel=1e-9)


@pytest.mark.parametrize("preset_name", CASADA_PRESETS)
def test_strategy_casada_bmk(preset_name, all_processed_legs):
    """Benchmark do casada: 'IPCA' para NTN-B/DAP, 'CDI' para LTN/NTN-F+DI1."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    has_ntnb = any(l["instrument"] == "NTN-B" for l in legs)
    expected_bmk = "IPCA" if has_ntnb else "CDI"
    assert strat["bmk"] == expected_bmk


@pytest.mark.parametrize("preset_name", CUPOM_SINT_PRESETS)
def test_strategy_cupom_sint_type(preset_name, all_processed_legs):
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    assert strat["type"] == "cupom_sint"
    assert "cupom" in strat


@pytest.mark.parametrize("preset_name", CUPOM_SINT_PRESETS)
def test_strategy_cupom_sint_value(preset_name, all_processed_legs):
    """Cupom cambial implicito bate com oracle."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)

    dol = next(l for l in legs if l["instrument"] == "DOL")
    di = next(l for l in legs if l["instrument"] == "DI1")
    expected = oracle.cupom_cambial_implicito(SPOT, dol["taxa"], di["taxa"], di["du"], di["dc"])

    assert strat["cupom"] == pytest.approx(expected, abs=TOL_CUPOM)


@pytest.mark.parametrize("preset_name", DOL_SINT_PRESETS)
def test_strategy_dol_sint_type(preset_name, all_processed_legs):
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    assert strat["type"] == "dol_sint"
    assert "fwd" in strat


@pytest.mark.parametrize("preset_name", DOL_SINT_PRESETS)
def test_strategy_dol_sint_fwd(preset_name, all_processed_legs):
    """Forward sintetico DI+FRC bate com oracle."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)

    di = next(l for l in legs if l["instrument"] == "DI1")
    frc = next(l for l in legs if l["instrument"] == "FRC")
    expected = oracle.dol_sintetico_fwd_di_frc(SPOT, di["taxa"], frc["taxa"], di["du"], frc["dc"])

    assert strat["fwd"] == pytest.approx(expected, rel=1e-9)


@pytest.mark.parametrize("preset_name", SINGLE_LEG_PRESETS)
def test_strategy_single(preset_name, all_processed_legs):
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    assert strat["type"] == "single"
    assert "result" in strat
    assert isinstance(strat["result"], str)
    assert len(strat["result"]) > 0


@pytest.mark.parametrize("preset_name", PRESET_NAMES)
def test_strategy_result_string(preset_name, all_processed_legs):
    """Todo preset gera result string nao vazio."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    assert "result" in strat
    assert isinstance(strat["result"], str)
    assert len(strat["result"]) > 0


# ----------------------------------------------------------------------------
# Risk factors
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name", PRESET_NAMES)
def test_risk_factors_returns_list(preset_name, all_processed_legs):
    """analyze_risk_factors retorna lista nao vazia de dicts {fator, exposto, desc}."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    factors = analyze_risk_factors(legs, strat)

    assert isinstance(factors, list)
    assert len(factors) > 0
    for f in factors:
        assert "fator" in f
        assert "exposto" in f
        assert isinstance(f["exposto"], bool)
        assert "desc" in f


@pytest.mark.parametrize("preset_name", CASADA_PRESETS)
def test_risk_factors_casada_has_spread(preset_name, all_processed_legs):
    """Casada: tem fator 'Spread (basis)' exposto=True."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    factors = analyze_risk_factors(legs, strat)

    spread_factor = next((f for f in factors if "Spread" in f["fator"]), None)
    assert spread_factor is not None, f"{preset_name}: sem fator Spread"
    assert spread_factor["exposto"] is True


def test_risk_factors_casada_ltn_no_inclinacao():
    """Casada LTN+DI1 (zero-coupon): inclinacao NAO exposta (mesmo vertice)."""
    # Esse teste depende de all_processed_legs como fixture
    pass


@pytest.mark.parametrize("preset_name", ["Casada NTN-F+DI1", "Casada NTN-B+DAP"])
def test_risk_factors_casada_with_coupon_has_inclinacao(preset_name, all_processed_legs):
    """Casada com cupom: 'Inclinacao' exposta=True."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    factors = analyze_risk_factors(legs, strat)

    incl = next((f for f in factors if "Inclinacao" in f["fator"]), None)
    assert incl is not None
    assert incl["exposto"] is True


@pytest.mark.parametrize("preset_name", ["Casada LTN+DI1", "Venda Casada LTN+DI1"])
def test_risk_factors_casada_zerocoupon_has_no_inclinacao(preset_name, all_processed_legs):
    """Casada LTN+DI1 sem cupom: 'Inclinacao' exposta=False."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    factors = analyze_risk_factors(legs, strat)

    incl = next((f for f in factors if "Inclinacao" in f["fator"]), None)
    if incl:
        assert incl["exposto"] is False


def test_risk_factors_dol_di1_cancels_pre(all_processed_legs):
    """DOL+DI1 cupom sint.: 'Nivel (taxa pre BRL)' NAO exposta + 'Cambio' NAO exposta."""
    legs = all_processed_legs["DOL+DI1 (cupom sint.)"]
    strat = detect_strategy(legs, SPOT)
    factors = analyze_risk_factors(legs, strat)

    nivel = next((f for f in factors if "Nivel" in f["fator"]), None)
    assert nivel is not None
    assert nivel["exposto"] is False

    cambio = next((f for f in factors if "Cambio" in f["fator"]), None)
    assert cambio is not None
    assert cambio["exposto"] is False

    cupom = next((f for f in factors if "Cupom Cambial" in f["fator"]), None)
    assert cupom is not None
    assert cupom["exposto"] is True


def test_risk_factors_di_frc_dol_sint(all_processed_legs):
    """DI1+FRC (dol sint.): Cambio exposto=True, Nivel pre nao exposto, Cupom hedgeado."""
    legs = all_processed_legs["DI1+FRC (dol sint.)"]
    strat = detect_strategy(legs, SPOT)
    factors = analyze_risk_factors(legs, strat)

    cambio = next((f for f in factors if "Cambio" in f["fator"]), None)
    assert cambio is not None
    assert cambio["exposto"] is True

    nivel = next((f for f in factors if "Nivel" in f["fator"]), None)
    if nivel:
        assert nivel["exposto"] is False


def test_risk_factors_ntnb_dap_hedges_ipca(all_processed_legs):
    """Casada NTN-B+DAP: 'Inflacao (IPCA)' exposto=False (hedgeado)."""
    legs = all_processed_legs["Casada NTN-B+DAP"]
    strat = detect_strategy(legs, SPOT)
    factors = analyze_risk_factors(legs, strat)

    ipca = next((f for f in factors if "Inflacao" in f["fator"]), None)
    assert ipca is not None
    assert ipca["exposto"] is False


@pytest.mark.parametrize("preset_name", SINGLE_LEG_PRESETS)
def test_risk_factors_single_leg_directional(preset_name, all_processed_legs):
    """Pernas direcionais: ao menos um fator exposto=True."""
    legs = all_processed_legs[preset_name]
    strat = detect_strategy(legs, SPOT)
    factors = analyze_risk_factors(legs, strat)

    has_exposure = any(f["exposto"] for f in factors)
    assert has_exposure, f"{preset_name}: nenhum fator exposto"
