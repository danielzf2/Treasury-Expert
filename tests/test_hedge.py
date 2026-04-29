"""Testes de suggest_hedge para presets com cupom (NTN-F, NTN-B).

Modos validados:
- maturity: 1 contrato no DU final
- duration: 1 contrato no DU = round(D_mac * 252)
- strip (hedge perfeito): 1 contrato por fluxo, casando DV01 fluxo a fluxo

Tambem valida _expand_hedge_legs (gera pernas auto DI1/DAP) bate
com suggest_hedge no count e no DV01 total.
"""

from __future__ import annotations

import pytest

from lib.exposure import suggest_hedge
from lib.instruments import dv01

from tests import oracle
from tests.conftest import LIQ_DATE, TOL_DURATION, TOL_DV01_REL
from tests.presets import COUPON_PRESETS


# ----------------------------------------------------------------------------
# Suggest hedge: shape + chaves
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_suggest_hedge_shape(preset_name, all_processed_legs):
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)
    assert hedge is not None
    assert "tpf" in hedge
    assert "hedge_instrument" in hedge
    assert "n_at_duration" in hedge
    assert "n_at_maturity" in hedge
    assert "dv01_at_duration" in hedge
    assert "dv01_at_maturity" in hedge
    assert "current_n" in hedge
    assert "dv01_residual" in hedge
    assert "strip" in hedge
    assert "n_strip_total" in hedge
    assert "du_duration" in hedge
    assert "du_maturity" in hedge


@pytest.mark.parametrize("preset_name,expected_inst", [
    ("Casada NTN-F+DI1", "DI1"),
    ("Casada NTN-B+DAP", "DAP"),
])
def test_suggest_hedge_instrument(preset_name, expected_inst, all_processed_legs):
    """NTN-F -> hedge com DI1; NTN-B -> hedge com DAP."""
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)
    assert hedge["hedge_instrument"] == expected_inst


@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_suggest_hedge_du_maturity(preset_name, all_processed_legs):
    """du_maturity = du do TPF; du_duration = round(D_mac * 252)."""
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)
    tpf = next(l for l in legs if l["info"].cup_sem > 0)
    assert hedge["du_maturity"] == tpf["du"]
    assert hedge["du_duration"] == round(tpf["d_mac"] * 252)


# ----------------------------------------------------------------------------
# DV01 calculations: at_duration e at_maturity
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_dv01_at_maturity(preset_name, all_processed_legs):
    """dv01_at_maturity = DV01 unitario do hedge instrument no DU final.

    DV01 hedge = D_mod * PU * 0.0001, com PU = 100k/(1+r)^(du/252) e r = di/dap rate.
    """
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)

    di_leg = next((l for l in legs if l["instrument"] in ("DI1", "DAP")), None)
    di_rate = di_leg["taxa"] if di_leg else 13.65

    # DV01 unitario teorico: D_mod * PU * 0.0001 com PU=DI1/DAP no du_maturity
    du_mat = hedge["du_maturity"]
    pu_di = oracle.pu_di1(di_rate, du_mat)  # mesma formula para DAP
    d_mac, d_mod = oracle.duration_zero_coupon(di_rate, du_mat)
    expected_dv01 = oracle.dv01_unit(d_mod, pu_di)

    assert hedge["dv01_at_maturity"] == pytest.approx(expected_dv01, rel=TOL_DV01_REL)


@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_dv01_at_duration(preset_name, all_processed_legs):
    """dv01_at_duration = DV01 unitario do hedge no DU = round(D_mac * 252)."""
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)

    di_leg = next((l for l in legs if l["instrument"] in ("DI1", "DAP")), None)
    di_rate = di_leg["taxa"] if di_leg else 13.65

    du_dur = hedge["du_duration"]
    pu_di = oracle.pu_di1(di_rate, du_dur)
    d_mac, d_mod = oracle.duration_zero_coupon(di_rate, du_dur)
    expected_dv01 = oracle.dv01_unit(d_mod, pu_di)

    assert hedge["dv01_at_duration"] == pytest.approx(expected_dv01, rel=TOL_DV01_REL)


# ----------------------------------------------------------------------------
# Numero de contratos: n_at_maturity e n_at_duration = round(DV01_TPF / DV01_hedge)
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_n_at_maturity(preset_name, all_processed_legs):
    """n_at_maturity = round(DV01_TPF_total / DV01_hedge_unit_at_maturity)."""
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)

    tpf = next(l for l in legs if l["info"].cup_sem > 0)
    expected_n = round(tpf["dv01_total"] / hedge["dv01_at_maturity"])
    assert hedge["n_at_maturity"] == expected_n


@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_n_at_duration(preset_name, all_processed_legs):
    """n_at_duration = round(DV01_TPF_total / DV01_hedge_unit_at_duration)."""
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)

    tpf = next(l for l in legs if l["info"].cup_sem > 0)
    expected_n = round(tpf["dv01_total"] / hedge["dv01_at_duration"])
    assert hedge["n_at_duration"] == expected_n


# ----------------------------------------------------------------------------
# DV01 residual e current_n
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_current_n_and_dv01_residual(preset_name, all_processed_legs):
    """current_n = qty da perna DI/DAP; dv01_residual = dv01_TPF - dv01_DI."""
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)

    tpf = next(l for l in legs if l["info"].cup_sem > 0)
    di_leg = next((l for l in legs if l["instrument"] in ("DI1", "DAP")), None)

    expected_current_n = di_leg["quantity"] if di_leg else 0
    expected_resid = tpf["dv01_total"] - (di_leg["dv01_total"] if di_leg else 0)

    assert hedge["current_n"] == expected_current_n
    assert hedge["dv01_residual"] == pytest.approx(expected_resid, rel=1e-9)


# ----------------------------------------------------------------------------
# Strip hedge: 1 contrato por fluxo
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_strip_count_matches_cashflows(preset_name, all_processed_legs):
    """strip[] tem 1 entrada por fluxo do TPF."""
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)
    tpf = next(l for l in legs if l["info"].cup_sem > 0)
    assert len(hedge["strip"]) == len(tpf["cashflows"]["flows"])


@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_strip_per_flow_dv01_and_n(preset_name, all_processed_legs):
    """Cada fluxo do strip:
    - du = du do fluxo
    - dv01_flow = D_mod_flow * PV_flow * 0.0001 * qty_TPF
    - hedge_n = round(dv01_flow / hedge_dv01_unit)
    """
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)

    tpf = next(l for l in legs if l["info"].cup_sem > 0)
    cashflows = tpf["cashflows"]["flows"]
    di_leg = next((l for l in legs if l["instrument"] in ("DI1", "DAP")), None)
    di_rate = di_leg["taxa"] if di_leg else 13.65
    tir = tpf["taxa"]

    for s, cf in zip(hedge["strip"], cashflows):
        # du
        assert s["du"] == cf["du"]
        assert s["hedge_du"] == cf["du"]

        # PV scaled (vna ja aplicado no cashflow)
        expected_pv = cf["pv"]
        assert s["pv_flow"] == pytest.approx(expected_pv, rel=1e-9)

        # DV01 do fluxo: D_mod_flow * pv * 0.0001 * qty
        t = cf["du"] / 252
        d_mod_flow = t / (1 + tir / 100)
        expected_flow_dv01 = d_mod_flow * expected_pv * 0.0001 * tpf["quantity"]
        assert s["dv01_flow"] == pytest.approx(expected_flow_dv01, rel=1e-9)

        # DV01 do contrato hedge no DU
        pu_h = oracle.pu_di1(di_rate, cf["du"])
        _, dmod_h = oracle.duration_zero_coupon(di_rate, cf["du"])
        expected_hedge_dv01 = oracle.dv01_unit(dmod_h, pu_h)
        assert s["hedge_dv01_unit"] == pytest.approx(expected_hedge_dv01, rel=TOL_DV01_REL)

        # Numero de contratos
        expected_n = round(expected_flow_dv01 / expected_hedge_dv01) if expected_hedge_dv01 else 0
        assert s["hedge_n"] == expected_n


@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_strip_total_dv01_matches_tpf(preset_name, all_processed_legs):
    """Soma dos DV01 dos fluxos = DV01 total do TPF (cada fluxo a sua duration_modificada).

    NOTA: Σ dv01_flow ≠ DV01_TPF necessariamente, pois o DV01 do TPF e via D_mac total,
    mas a soma de Dmod_i * PV_i = D_mod_total * PV_total (identidade aritmetica), entao
    soma DV01_flow = D_mac_TPF * PV_TPF * 0.0001 * qty (sem o /(1+r)).

    Vamos verificar a identidade certa:
    Σ (t_i / (1+r) * PV_i) * 0.0001 * qty = (1/(1+r)) * Σ(t_i * PV_i) * 0.0001 * qty
                                          = (1/(1+r)) * D_mac * Σ PV_i * 0.0001 * qty
                                          = D_mod * pu_total * 0.0001 * qty
                                          = DV01_TPF_total
    """
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)
    tpf = next(l for l in legs if l["info"].cup_sem > 0)

    sum_dv01_flow = sum(s["dv01_flow"] for s in hedge["strip"])
    assert sum_dv01_flow == pytest.approx(tpf["dv01_total"], rel=1e-6)


@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_strip_n_total_consistency(preset_name, all_processed_legs):
    """n_strip_total = soma de hedge_n dos fluxos (puro count check)."""
    legs = all_processed_legs[preset_name]
    hedge = suggest_hedge(legs)
    expected_total = sum(s["hedge_n"] for s in hedge["strip"])
    assert hedge["n_strip_total"] == expected_total


# ----------------------------------------------------------------------------
# _expand_hedge_legs: insercao automatica de pernas DI1/DAP por modo
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
@pytest.mark.parametrize("mode,n_extra_expected", [
    ("manual", 0),     # nenhuma perna automatica
    ("maturity", 1),   # 1 perna DI/DAP no vencimento
    ("duration", 1),   # 1 perna DI/DAP no duration
])
def test_expand_hedge_inserts_legs(preset_name, mode, n_extra_expected,
                                    processed_legs_factory):
    """_expand_hedge_legs adiciona ou nao perna auto."""
    legs = processed_legs_factory(preset_name, hedge_mode=mode)
    auto_legs = [l for l in legs if l.get("auto")]
    assert len(auto_legs) == n_extra_expected, \
        f"{preset_name}/{mode}: extra auto legs = {len(auto_legs)}"


@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
def test_expand_hedge_strip_inserts_per_flow(preset_name, processed_legs_factory):
    """Modo strip: insere 1 perna auto por fluxo do TPF (com hedge_n != 0)."""
    legs = processed_legs_factory(preset_name, hedge_mode="strip")

    tpf = next(l for l in legs if l["info"].cup_sem > 0 and not l.get("auto"))
    auto_legs = [l for l in legs if l.get("auto")]

    # n cap = num fluxos do TPF (alguns podem ter hedge_n=0 e ser filtrados)
    expected_max = len(tpf["cashflows"]["flows"])
    assert 1 <= len(auto_legs) <= expected_max
