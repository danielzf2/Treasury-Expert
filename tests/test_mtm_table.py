"""MtM table: validacao das 13 magnitudes x 8 cenarios x 8 presets.

A MtM table do endpoint /sim/mtm-table devolve:
{
  table: [
    {delta: -20, pnls: [pnl_perna_1, pnl_perna_2, ...], total: float},
    ...
    {delta: +20, ...},
  ],
  total_pnl: float (linha do magnitude solicitado),
  flow_pnl: [{instrument, ticker, total, flows: [...]}, ...]
}

Replica internamente o que mtm_table faz, comparando contra o oracle:
- Para cada delta in _MTM_STEPS:
  - Para cada perna:
    - DOL (price): pnl=0 sempre (delta_fx=0 default)
    - Cupom: usa calc_leg_pnl_per_flow com curva spot
    - Demais: usa calc_leg_pnl com TIR-shift
"""

from __future__ import annotations

import pytest

from api.simulator import _MTM_STEPS, mtm_table, MtmTableRequest, _serialize_leg

from tests import oracle
from tests.conftest import LIQ_DATE, TOL_PNL
from tests.presets import PRESET_NAMES, COUPON_PRESETS


SCENARIO_KEYS = ["bull_par", "bear_par", "bull_steep", "bear_steep",
                 "bull_flat", "bear_flat", "pos_fly", "neg_fly"]


def _build_mtm_req(legs: list[dict], scenario_key: str, magnitude: float,
                   di1: list, dap: list,
                   delta_fx_pct: float = 0.0,
                   delta_ipca_bps: float = 0.0,
                   delta_cupom_bps: float = 0.0) -> MtmTableRequest:
    """Constroi MtmTableRequest a partir das legs processadas serializadas."""
    serialized = [_serialize_leg(l) for l in legs]
    return MtmTableRequest(
        legs=serialized,
        scenario_key=scenario_key,
        magnitude=magnitude,
        delta_fx_pct=delta_fx_pct,
        delta_ipca_bps=delta_ipca_bps,
        delta_cupom_bps=delta_cupom_bps,
        di1=di1,
        dap=dap,
    )


# ============================================================================
# 1. Shape e estrutura
# ============================================================================

@pytest.mark.parametrize("preset_name", PRESET_NAMES)
def test_mtm_table_shape(preset_name, all_processed_legs, market_snap):
    """MtM table tem 13 linhas, total_pnl, flow_pnl shape."""
    legs = all_processed_legs[preset_name]
    req = _build_mtm_req(legs, "bear_par", 10.0, market_snap.di1, market_snap.dap)
    res = mtm_table(req)

    assert "table" in res
    assert "total_pnl" in res
    assert "flow_pnl" in res
    assert len(res["table"]) == len(_MTM_STEPS)

    for row in res["table"]:
        assert "delta" in row
        assert "pnls" in row
        assert "total" in row
        assert len(row["pnls"]) == len(legs)


def test_mtm_table_steps():
    """_MTM_STEPS contem as 13 magnitudes esperadas."""
    assert _MTM_STEPS == [-20, -15, -10, -5, -2, -1, 0, 1, 2, 5, 10, 15, 20]


# ============================================================================
# 2. Linha delta=0: P&L = 0 (sem choque)
# ============================================================================

@pytest.mark.parametrize("preset_name", PRESET_NAMES)
@pytest.mark.parametrize("scenario_key", SCENARIO_KEYS)
def test_mtm_table_zero_magnitude_zero_pnl(preset_name, scenario_key,
                                             all_processed_legs, market_snap):
    """Em qualquer cenario, magnitude=0 da P&L=0 em todas as pernas."""
    legs = all_processed_legs[preset_name]
    req = _build_mtm_req(legs, scenario_key, 10.0, market_snap.di1, market_snap.dap)
    res = mtm_table(req)

    zero_row = next(r for r in res["table"] if r["delta"] == 0)
    assert zero_row["total"] == pytest.approx(0.0, abs=TOL_PNL)
    for pnl in zero_row["pnls"]:
        assert pnl == pytest.approx(0.0, abs=TOL_PNL)


# ============================================================================
# 3. Total = soma de pernas (consistencia interna)
# ============================================================================

@pytest.mark.parametrize("preset_name", PRESET_NAMES)
@pytest.mark.parametrize("scenario_key", SCENARIO_KEYS)
def test_mtm_table_total_consistency(preset_name, scenario_key,
                                       all_processed_legs, market_snap):
    """Em cada linha: total == soma(pnls) (com arredondamento de 0.02)."""
    legs = all_processed_legs[preset_name]
    req = _build_mtm_req(legs, scenario_key, 10.0, market_snap.di1, market_snap.dap)
    res = mtm_table(req)

    for row in res["table"]:
        soma = sum(row["pnls"])
        # row.total = round(sum(pnls_raw), 2); pnls = [round(pnl_raw, 2) for ...]
        # Diferenca max: len(legs) * 0.005 (arredondamentos individuais) + 0.005 (total)
        assert row["total"] == pytest.approx(soma, abs=len(legs) * 0.005 + 0.005)


# ============================================================================
# 4. P&L per leg vs oracle (full coverage 8 presets x 8 cenarios x 13 mag)
# ============================================================================

@pytest.mark.parametrize("preset_name", PRESET_NAMES)
@pytest.mark.parametrize("scenario_key", SCENARIO_KEYS)
@pytest.mark.parametrize("magnitude", _MTM_STEPS)
def test_mtm_table_per_leg_oracle(preset_name, scenario_key, magnitude,
                                    all_processed_legs, market_snap):
    """Cada linha da MtM table bate com oracle para cada perna.

    Oracle:
    - DOL: pnl = 0 (delta_fx_pct=0)
    - NTN-F/NTN-B: oracle.pnl_per_flow(...).leg_pnl
    - Demais: oracle.pnl_per_leg_scenario(...)
    """
    legs = all_processed_legs[preset_name]
    req = _build_mtm_req(legs, scenario_key, 10.0, market_snap.di1, market_snap.dap)
    res = mtm_table(req)

    row = next(r for r in res["table"] if r["delta"] == magnitude)

    # mtm_table usa ancoras absolutas (1m, 10y) — definicao consistente de
    # 'curtos vs longos' independente da carteira.
    from lib.scenarios import SCENARIO_DU_SHORT, SCENARIO_DU_LONG
    du_min = SCENARIO_DU_SHORT
    du_max = SCENARIO_DU_LONG

    # Build spot curves
    from lib.curves import build_di_vertices, build_dap_vertices
    di_verts = build_di_vertices(market_snap.di1, LIQ_DATE)
    dap_verts = build_dap_vertices(market_snap.dap, LIQ_DATE)

    for li, leg in enumerate(legs):
        actual = row["pnls"][li]
        info = leg["info"]
        inst = leg["instrument"]

        if info.conv == "price":
            # DOL: pnl=0 (delta_fx=0)
            assert actual == pytest.approx(0.0, abs=TOL_PNL)
            continue

        if info.cup_sem > 0:
            # NTN-F, NTN-B
            spot = dap_verts if inst == "NTN-B" else di_verts
            res_flow = oracle.pnl_per_flow(
                leg, scenario_key, magnitude, du_min, du_max, spot,
            )
            expected = res_flow["leg_pnl"]
        else:
            expected = oracle.pnl_per_leg_scenario(
                leg, scenario_key, magnitude, du_min, du_max,
            )

        assert actual == pytest.approx(expected, abs=TOL_PNL), \
            f"{preset_name}/{inst}/{scenario_key}/mag={magnitude}: lib={actual} oracle={expected}"


# ============================================================================
# 5. flow_pnl: detalhamento por fluxo (NTN-F, NTN-B)
# ============================================================================

@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
@pytest.mark.parametrize("scenario_key", ["bull_par", "bear_par", "bear_steep"])
@pytest.mark.parametrize("magnitude", [-10, 0, 10])
def test_mtm_flow_pnl_total(preset_name, scenario_key, magnitude,
                              all_processed_legs, market_snap):
    """flow_pnl.total bate com oracle.pnl_per_flow.leg_pnl."""
    legs = all_processed_legs[preset_name]
    req = _build_mtm_req(legs, scenario_key, magnitude, market_snap.di1, market_snap.dap)
    res = mtm_table(req)

    flow_pnl = res["flow_pnl"]
    assert len(flow_pnl) >= 1  # pelo menos 1 perna com cupom

    from lib.scenarios import SCENARIO_DU_SHORT, SCENARIO_DU_LONG
    du_min = SCENARIO_DU_SHORT
    du_max = SCENARIO_DU_LONG

    from lib.curves import build_di_vertices, build_dap_vertices
    di_verts = build_di_vertices(market_snap.di1, LIQ_DATE)
    dap_verts = build_dap_vertices(market_snap.dap, LIQ_DATE)

    for fp in flow_pnl:
        inst = fp["instrument"]
        leg = next(l for l in legs if l["instrument"] == inst)
        spot = dap_verts if inst == "NTN-B" else di_verts

        expected_res = oracle.pnl_per_flow(
            leg, scenario_key, magnitude, du_min, du_max, spot,
        )
        assert fp["total"] == pytest.approx(expected_res["leg_pnl"], abs=TOL_PNL)
        # Numero de fluxos
        assert len(fp["flows"]) == len(expected_res["flows"])


@pytest.mark.parametrize("preset_name", COUPON_PRESETS)
@pytest.mark.parametrize("scenario_key", ["bull_par", "bear_par"])
@pytest.mark.parametrize("magnitude", [-10, 10])
def test_mtm_flow_pnl_per_flow_detail(preset_name, scenario_key, magnitude,
                                        all_processed_legs, market_snap):
    """Cada fluxo do flow_pnl: pnl, du, delta_bps batem com oracle."""
    legs = all_processed_legs[preset_name]
    req = _build_mtm_req(legs, scenario_key, magnitude, market_snap.di1, market_snap.dap)
    res = mtm_table(req)

    rate_legs = [l for l in legs if l["info"].conv != "price"]
    du_min = min(l["du"] for l in rate_legs) if rate_legs else 0
    du_max = max(l["du"] for l in rate_legs) if rate_legs else 1

    from lib.curves import build_di_vertices, build_dap_vertices
    di_verts = build_di_vertices(market_snap.di1, LIQ_DATE)
    dap_verts = build_dap_vertices(market_snap.dap, LIQ_DATE)

    for fp in res["flow_pnl"]:
        inst = fp["instrument"]
        leg = next(l for l in legs if l["instrument"] == inst)
        spot = dap_verts if inst == "NTN-B" else di_verts

        expected_res = oracle.pnl_per_flow(
            leg, scenario_key, magnitude, du_min, du_max, spot,
        )

        for af, ef in zip(fp["flows"], expected_res["flows"]):
            assert af["du"] == ef["du"]
            assert af["delta_bps"] == pytest.approx(ef["delta_bps"], rel=1e-9)
            assert af["pnl"] == pytest.approx(ef["pnl_flow"], abs=TOL_PNL)


# ============================================================================
# 6. total_pnl: linha da magnitude solicitada
# ============================================================================

@pytest.mark.parametrize("preset_name", PRESET_NAMES)
@pytest.mark.parametrize("scenario_key", ["bull_par", "bear_par"])
@pytest.mark.parametrize("magnitude_req", [-10, 0, 10])
def test_mtm_total_pnl_matches_row(preset_name, scenario_key, magnitude_req,
                                     all_processed_legs, market_snap):
    """total_pnl == row.total da linha cuja delta == magnitude solicitado."""
    legs = all_processed_legs[preset_name]
    req = _build_mtm_req(legs, scenario_key, magnitude_req, market_snap.di1, market_snap.dap)
    res = mtm_table(req)

    matching_row = next((r for r in res["table"] if r["delta"] == magnitude_req), None)
    if matching_row:
        assert res["total_pnl"] == matching_row["total"]


# ============================================================================
# 7. Custom scenario na MtM table
# ============================================================================

@pytest.mark.parametrize("preset_name", ["LTN direcional", "Casada LTN+DI1"])
@pytest.mark.parametrize("custom_p,custom_s,custom_c", [
    (10, 0, 0),    # paralelo puro
    (0, 10, 0),    # slope puro
    (0, 0, 10),    # curvature puro
])
def test_mtm_table_custom_scenario(preset_name, custom_p, custom_s, custom_c,
                                    all_processed_legs, market_snap):
    """MtM table com cenario custom: linhas batem com oracle."""
    legs = all_processed_legs[preset_name]
    serialized = [_serialize_leg(l) for l in legs]
    req = MtmTableRequest(
        legs=serialized,
        scenario_key="custom",
        magnitude=10.0,
        custom_parallel_bps=custom_p,
        custom_slope_bps=custom_s,
        custom_curvature_bps=custom_c,
        di1=market_snap.di1,
        dap=market_snap.dap,
    )
    res = mtm_table(req)

    from lib.scenarios import SCENARIO_DU_SHORT, SCENARIO_DU_LONG
    du_min = SCENARIO_DU_SHORT
    du_max = SCENARIO_DU_LONG

    for row in res["table"]:
        mag = row["delta"]
        for li, leg in enumerate(legs):
            if leg["info"].conv == "price":
                continue
            if leg["info"].cup_sem > 0:
                continue  # so direcional/zero-coupon nesse subset

            expected = oracle.pnl_per_leg_scenario(
                leg, "custom", mag, du_min, du_max,
                custom_parallel_bps=custom_p,
                custom_slope_bps=custom_s,
                custom_curvature_bps=custom_c,
            )
            assert row["pnls"][li] == pytest.approx(expected, abs=TOL_PNL)
