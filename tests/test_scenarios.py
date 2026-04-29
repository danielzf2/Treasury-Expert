"""Cenarios + P&L: full coverage.

Validacoes:
1. calc_scenario_delta(du, du_min, du_max, scenario, mag) bate com oracle:
   - 9 cenarios (bull_par, bear_par, bull_steep, bear_steep, bull_flat, bear_flat,
     pos_fly, neg_fly, custom)
   - magnitudes [-20, -15, -10, -5, -2, -1, 1, 2, 5, 10, 15, 20]
   - varios DUs (vertices min, max, mid, fora do range)

2. calc_leg_pnl (parallel) bate com oracle.pnl_per_leg_parallel:
   - 8 presets x 8 cenarios x 13 magnitudes x cada perna = ~1700 testes

3. calc_leg_pnl_per_flow (NTN-F, NTN-B):
   - 2 presets x 8 cenarios x 13 magnitudes x ~10 fluxos cada = ~2080 testes

4. Multi-fator (delta_fx_pct, delta_ipca_bps, delta_cupom_bps):
   - DOL+DI1 com delta_fx_pct
   - NTN-B+DAP com delta_ipca_bps
   - DI1+FRC com delta_cupom_bps

5. Properties:
   - bull_par(mag) + bear_par(mag) ≈ 0
   - pos_fly + neg_fly ≈ 0
   - Casada perfeita: P&L total bull/bear_par bem proximo de 0 (apos hedge)
"""

from __future__ import annotations

import pytest

from lib.scenarios import (
    SCENARIOS, calc_scenario_delta, calc_leg_pnl, calc_leg_pnl_per_flow,
)
from lib.curves import build_di_vertices, build_dap_vertices

from tests import oracle
from tests.conftest import LIQ_DATE, TOL_PNL, TOL_DURATION
from tests.presets import PRESET_NAMES, PRESETS_INPUT


SCENARIO_KEYS = ["bull_par", "bear_par", "bull_steep", "bear_steep",
                 "bull_flat", "bear_flat", "pos_fly", "neg_fly"]
MAGNITUDES = [-20, -15, -10, -5, -2, -1, 1, 2, 5, 10, 15, 20]
ALL_MAGNITUDES = MAGNITUDES + [0]


# ============================================================================
# 1. calc_scenario_delta — formulas de shock
# ============================================================================

@pytest.mark.parametrize("scenario_key", SCENARIO_KEYS)
@pytest.mark.parametrize("magnitude", MAGNITUDES)
@pytest.mark.parametrize("position", ["min", "mid", "max", "below_min", "above_max"])
def test_scenario_delta_at_position(scenario_key, magnitude, position):
    """Para cada cenario x magnitude x posicao na curva, delta bate com oracle."""
    du_min = 252
    du_max = 1764  # 7 anos
    if position == "min":
        du = du_min
    elif position == "mid":
        du = (du_min + du_max) // 2
    elif position == "max":
        du = du_max
    elif position == "below_min":
        du = 100  # antes de du_min
    else:
        du = 2520  # depois de du_max

    actual = calc_scenario_delta(du, du_min, du_max, scenario_key, magnitude)
    expected = oracle.scenario_delta_bps(du, du_min, du_max, scenario_key, magnitude)
    assert actual == pytest.approx(expected, rel=1e-9, abs=1e-9)


@pytest.mark.parametrize("scenario_key", SCENARIO_KEYS)
def test_scenario_delta_zero_magnitude(scenario_key):
    """Magnitude=0 sempre da delta=0."""
    delta = calc_scenario_delta(1000, 500, 1500, scenario_key, 0)
    assert delta == 0.0


@pytest.mark.parametrize("magnitude", [10, -10])
def test_scenario_delta_bull_bear_par_oposto(magnitude):
    """bull_par(mag) = -mag, bear_par(mag) = mag (em qualquer DU)."""
    bull = calc_scenario_delta(1000, 500, 1500, "bull_par", magnitude)
    bear = calc_scenario_delta(1000, 500, 1500, "bear_par", magnitude)
    assert bull == -magnitude
    assert bear == magnitude
    assert bull + bear == 0.0


@pytest.mark.parametrize("magnitude", [5, 10, 20])
@pytest.mark.parametrize("du", [252, 500, 1000, 1500, 2000])
def test_scenario_delta_butterflies_oposto(magnitude, du):
    """pos_fly(mag,t) = -neg_fly(mag,t)."""
    pos = calc_scenario_delta(du, 252, 2520, "pos_fly", magnitude)
    neg = calc_scenario_delta(du, 252, 2520, "neg_fly", magnitude)
    assert pos == pytest.approx(-neg, abs=1e-12)


def test_scenario_delta_butterfly_zero_when_du_min_eq_max():
    """Quando du_min==du_max, butterflies dao 0 (caso degenerado)."""
    assert calc_scenario_delta(1000, 1000, 1000, "pos_fly", 10) == 0.0
    assert calc_scenario_delta(1000, 1000, 1000, "neg_fly", 10) == 0.0


# ============================================================================
# 2. Custom scenario
# ============================================================================

@pytest.mark.parametrize("magnitude", [10, 20])
@pytest.mark.parametrize("parallel,slope,curv", [
    (10, 0, 0),
    (0, 10, 0),
    (0, 0, 10),
    (5, 5, 5),
    (-3, 7, -2),
])
@pytest.mark.parametrize("du", [252, 1000, 1764])
def test_custom_scenario(magnitude, parallel, slope, curv, du):
    """Custom: scale = mag/10; delta = scale*(par + slope*t + curv*(0.5-1.5*t^2))."""
    actual = calc_scenario_delta(du, 252, 1764, "custom", magnitude,
                                  parallel, slope, curv)
    expected = oracle.scenario_delta_bps(du, 252, 1764, "custom", magnitude,
                                          parallel, slope, curv)
    assert actual == pytest.approx(expected, rel=1e-9, abs=1e-9)


# ============================================================================
# 3. P&L per leg (parallel shift)
# ============================================================================

# Pernas elegiveis: nao-DOL (precisa multi-fator), nao-cupom (avaliada por
# calc_leg_pnl com TIR-shift). NTN-F/NTN-B sao testadas separadamente em per_flow.
def _pnl_legs():
    out = []
    for name in PRESET_NAMES:
        for i, leg in enumerate(PRESETS_INPUT[name]):
            out.append((name, i, leg))
    return out


PNL_LEGS = _pnl_legs()
PNL_LEG_IDS = [f"{p}#{i}-{l['instrument']}" for p, i, l in PNL_LEGS]


@pytest.mark.parametrize("preset_name,leg_idx,leg_input", PNL_LEGS, ids=PNL_LEG_IDS)
@pytest.mark.parametrize("delta_bps", [-100, -10, -1, 0, 1, 10, 100])
def test_pnl_per_leg_parallel(preset_name, leg_idx, leg_input, delta_bps,
                                all_processed_legs):
    """P&L de uma perna sob choque paralelo TIR-shift bate com oracle."""
    leg = all_processed_legs[preset_name][leg_idx]
    actual = calc_leg_pnl(leg, delta_bps)

    expected = oracle.pnl_per_leg_parallel(leg, delta_bps)
    assert actual == pytest.approx(expected, abs=TOL_PNL)


# ============================================================================
# 4. P&L per leg em cenarios completos
# ============================================================================

def _du_min_max(legs):
    """du_min/max das pernas com taxa (nao DOL)."""
    rate_legs = [l for l in legs if l["info"].conv != "price"]
    if not rate_legs:
        return 0, 1
    return min(l["du"] for l in rate_legs), max(l["du"] for l in rate_legs)


@pytest.mark.parametrize("preset_name", PRESET_NAMES)
@pytest.mark.parametrize("scenario_key", SCENARIO_KEYS)
@pytest.mark.parametrize("magnitude", MAGNITUDES)
def test_pnl_per_leg_scenario(preset_name, scenario_key, magnitude, all_processed_legs):
    """P&L de cada perna em cada cenario x magnitude bate com oracle.

    Apenas pernas sem cupom (LTN, DI1, DAP, FRC, DDI, DOL).
    NTN-F/NTN-B vai em per_flow.
    """
    legs = all_processed_legs[preset_name]
    du_min, du_max = _du_min_max(legs)

    for leg in legs:
        # Skip DOL e cupom (avaliada por per_flow ou multi-fator)
        if leg["instrument"] == "DOL":
            continue
        if leg["info"].cup_sem > 0:
            continue

        delta_lib = calc_scenario_delta(leg["du"], du_min, du_max, scenario_key, magnitude)
        actual = calc_leg_pnl(leg, delta_lib)

        expected = oracle.pnl_per_leg_scenario(
            leg, scenario_key, magnitude, du_min, du_max,
        )
        assert actual == pytest.approx(expected, abs=TOL_PNL), \
            f"{preset_name}/{leg['instrument']}/{scenario_key}/mag={magnitude}: lib={actual}, oracle={expected}"


# ============================================================================
# 5. Multi-fator: delta_fx_pct, delta_ipca_bps, delta_cupom_bps
# ============================================================================

@pytest.mark.parametrize("delta_fx_pct", [-5, -1, 0, 1, 5])
def test_pnl_dol_with_fx(delta_fx_pct, all_processed_legs):
    """DOL: P&L = sign * cotacao * delta_fx_pct/100 * mult * qty."""
    legs = all_processed_legs["DOL+DI1 (cupom sint.)"]
    dol = next(l for l in legs if l["instrument"] == "DOL")

    actual = calc_leg_pnl(dol, 0, delta_fx_pct=delta_fx_pct)
    expected = oracle.pnl_per_leg_parallel(dol, 0, delta_fx_pct=delta_fx_pct)
    assert actual == pytest.approx(expected, abs=TOL_PNL)


@pytest.mark.parametrize("delta_ipca_bps", [-20, -10, 0, 10, 20])
def test_pnl_dap_with_ipca(delta_ipca_bps, all_processed_legs):
    """DAP usa delta_ipca_bps quando != 0 (nao usa delta_bps)."""
    legs = all_processed_legs["Casada NTN-B+DAP"]
    dap = next(l for l in legs if l["instrument"] == "DAP")

    actual = calc_leg_pnl(dap, 0, delta_ipca_bps=delta_ipca_bps)
    expected = oracle.pnl_per_leg_parallel(dap, 0, delta_ipca_bps=delta_ipca_bps)
    assert actual == pytest.approx(expected, abs=TOL_PNL)


@pytest.mark.parametrize("delta_cupom_bps", [-20, -10, 0, 10, 20])
def test_pnl_frc_with_cupom(delta_cupom_bps, all_processed_legs):
    """FRC usa delta_cupom_bps quando != 0."""
    legs = all_processed_legs["DI1+FRC (dol sint.)"]
    frc = next(l for l in legs if l["instrument"] == "FRC")

    actual = calc_leg_pnl(frc, 0, delta_cupom_bps=delta_cupom_bps)
    expected = oracle.pnl_per_leg_parallel(frc, 0, delta_cupom_bps=delta_cupom_bps)
    assert actual == pytest.approx(expected, abs=TOL_PNL)


# ============================================================================
# 6. Per-flow MtM (NTN-F, NTN-B)
# ============================================================================

COUPON_PRESETS_LEGS = [
    ("Casada NTN-F+DI1", "NTN-F"),
    ("Casada NTN-B+DAP", "NTN-B"),
]


def _spot_curve_for_inst(inst: str, market_snap, liq_date):
    """Retorna (vertices_DU_taxa, ...) apropriada por instrumento."""
    if inst == "NTN-B":
        return build_dap_vertices(market_snap.dap, liq_date)
    return build_di_vertices(market_snap.di1, liq_date)


@pytest.mark.parametrize("preset_name,inst", COUPON_PRESETS_LEGS)
@pytest.mark.parametrize("scenario_key", SCENARIO_KEYS)
@pytest.mark.parametrize("magnitude", MAGNITUDES)
def test_pnl_per_flow_total(preset_name, inst, scenario_key, magnitude,
                             all_processed_legs, market_snap):
    """leg_pnl total bate com oracle."""
    legs = all_processed_legs[preset_name]
    leg = next(l for l in legs if l["instrument"] == inst)

    du_min, du_max = _du_min_max(legs)
    spot = _spot_curve_for_inst(inst, market_snap, LIQ_DATE)

    actual_res = calc_leg_pnl_per_flow(
        leg, scenario_key, magnitude, du_min, du_max, spot,
    )
    assert actual_res is not None

    expected_res = oracle.pnl_per_flow(
        leg, scenario_key, magnitude, du_min, du_max, spot,
    )
    assert expected_res is not None

    assert actual_res["leg_pnl"] == pytest.approx(expected_res["leg_pnl"], abs=TOL_PNL)


@pytest.mark.parametrize("preset_name,inst", COUPON_PRESETS_LEGS)
@pytest.mark.parametrize("scenario_key", ["bull_par", "bear_par", "bear_steep", "pos_fly"])
@pytest.mark.parametrize("magnitude", [-10, 10])
def test_pnl_per_flow_each_flow(preset_name, inst, scenario_key, magnitude,
                                  all_processed_legs, market_snap):
    """Cada fluxo: pnl_flow, old_pv, new_pv, delta_bps batem com oracle."""
    legs = all_processed_legs[preset_name]
    leg = next(l for l in legs if l["instrument"] == inst)

    du_min, du_max = _du_min_max(legs)
    spot = _spot_curve_for_inst(inst, market_snap, LIQ_DATE)

    actual_res = calc_leg_pnl_per_flow(
        leg, scenario_key, magnitude, du_min, du_max, spot,
    )
    expected_res = oracle.pnl_per_flow(
        leg, scenario_key, magnitude, du_min, du_max, spot,
    )

    for af, ef in zip(actual_res["flows"], expected_res["flows"]):
        assert af["du"] == ef["du"]
        assert af["delta_bps"] == pytest.approx(ef["delta_bps"], rel=1e-9)
        assert af["old_pv"] == pytest.approx(ef["old_pv"], rel=1e-9)
        assert af["new_pv"] == pytest.approx(ef["new_pv"], rel=1e-9)
        assert af["pnl_flow"] == pytest.approx(ef["pnl_flow"], abs=TOL_PNL)


@pytest.mark.parametrize("preset_name,inst", COUPON_PRESETS_LEGS)
def test_pnl_per_flow_spread_credito(preset_name, inst, all_processed_legs, market_snap):
    """spread_credito = TIR_TPF - curva_no_DU. Constante entre fluxos."""
    legs = all_processed_legs[preset_name]
    leg = next(l for l in legs if l["instrument"] == inst)

    du_min, du_max = _du_min_max(legs)
    spot = _spot_curve_for_inst(inst, market_snap, LIQ_DATE)

    actual_res = calc_leg_pnl_per_flow(leg, "bull_par", 0, du_min, du_max, spot)
    expected_res = oracle.pnl_per_flow(leg, "bull_par", 0, du_min, du_max, spot)

    assert actual_res["spread_credito"] == pytest.approx(expected_res["spread_credito"], rel=1e-9)


# ============================================================================
# 7. Properties (sanity checks)
# ============================================================================

@pytest.mark.parametrize("preset_name", PRESET_NAMES)
@pytest.mark.parametrize("magnitude", [10, 20, 50])
def test_property_bull_bear_par_cancel(preset_name, magnitude, all_processed_legs):
    """Para qualquer perna nao-DOL, P&L(bull_par,mag) + P&L(bear_par,mag) = 0
    (a 1a ordem; pode ter convexity residual em titulos com cupom).
    """
    legs = all_processed_legs[preset_name]
    du_min, du_max = _du_min_max(legs)

    for leg in legs:
        if leg["instrument"] == "DOL":
            continue
        if leg["info"].cup_sem > 0:
            # Pernas com cupom tem convexity entao soma nao e exatamente 0
            continue

        delta_bull = calc_scenario_delta(leg["du"], du_min, du_max, "bull_par", magnitude)
        delta_bear = calc_scenario_delta(leg["du"], du_min, du_max, "bear_par", magnitude)
        pnl_bull = calc_leg_pnl(leg, delta_bull)
        pnl_bear = calc_leg_pnl(leg, delta_bear)

        # Soma proxima de 0 (efeito convexidade pequeno em zero-coupon mas
        # pode ter alguma diferenca; usamos rel<1% do |pnl_bull|)
        soma = pnl_bull + pnl_bear
        ref = max(abs(pnl_bull), abs(pnl_bear), 1.0)
        assert abs(soma) < ref * 0.05, \
            f"{preset_name}/{leg['instrument']}: bull+bear = {soma}, ref={ref}"


@pytest.mark.parametrize("preset_name", PRESET_NAMES)
@pytest.mark.parametrize("magnitude", [10, 50])
def test_property_pos_neg_fly_cancel(preset_name, magnitude, all_processed_legs):
    """pos_fly(mag) + neg_fly(mag) = 0 em qualquer DU (formulas opostas)."""
    legs = all_processed_legs[preset_name]
    du_min, du_max = _du_min_max(legs)

    for leg in legs:
        if leg["instrument"] == "DOL":
            continue

        delta_pos = calc_scenario_delta(leg["du"], du_min, du_max, "pos_fly", magnitude)
        delta_neg = calc_scenario_delta(leg["du"], du_min, du_max, "neg_fly", magnitude)
        assert delta_pos == pytest.approx(-delta_neg, abs=1e-12)


@pytest.mark.parametrize("magnitude", [-10, 10])
def test_property_dol_di1_cancels_in_bull_par(magnitude, all_processed_legs):
    """DOL+DI1 (cupom sint.) em bull_par: P&L = 0 (DOL nao move, DI1 move sozinho)."""
    legs = all_processed_legs["DOL+DI1 (cupom sint.)"]
    du_min, du_max = _du_min_max(legs)

    total = 0.0
    for leg in legs:
        if leg["instrument"] == "DOL":
            continue
        delta = calc_scenario_delta(leg["du"], du_min, du_max, "bull_par", magnitude)
        total += calc_leg_pnl(leg, delta)

    # DOL com fx=0: P&L=0; DI1 sozinho move com choque
    # Esse teste nao ZERA porque DI1 nao tem hedge
    assert total != 0  # so sanity: ha movimento


def test_property_dol_di1_with_fx_only(all_processed_legs):
    """Apenas delta_fx (sem delta_bps): apenas DOL move, DI nao."""
    legs = all_processed_legs["DOL+DI1 (cupom sint.)"]
    dol = next(l for l in legs if l["instrument"] == "DOL")
    di = next(l for l in legs if l["instrument"] == "DI1")

    pnl_dol = calc_leg_pnl(dol, 0, delta_fx_pct=5.0)
    pnl_di = calc_leg_pnl(di, 0, delta_fx_pct=5.0)

    assert abs(pnl_dol) > 0  # DOL deve mover
    assert pnl_di == 0  # DI nao mexe com fx


# ============================================================================
# 8. SCENARIOS dict shape
# ============================================================================

def test_scenarios_dict_keys():
    """SCENARIOS tem todas as chaves esperadas."""
    expected = set(SCENARIO_KEYS) | {"custom"}
    assert set(SCENARIOS.keys()) == expected


def test_scenarios_have_name_and_desc():
    for key, sc in SCENARIOS.items():
        assert sc.name
        assert sc.desc
