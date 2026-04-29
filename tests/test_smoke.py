"""Smoke tests to validate fixtures and oracle imports."""

from __future__ import annotations

from datetime import date

import pytest

from tests.presets import PRESETS_INPUT, PRESET_NAMES
from tests import oracle


def test_preset_names():
    assert len(PRESET_NAMES) == 8
    assert "Casada LTN+DI1" in PRESET_NAMES
    assert "DOL+DI1 (cupom sint.)" in PRESET_NAMES


def test_oracle_pu_ltn():
    pu = oracle.pu_ltn_anbima(13.7625, 1485)
    assert pu > 0
    assert pu < 1000


def test_oracle_pu_di1():
    pu = oracle.pu_di1(13.65, 1485)
    assert 40_000 < pu < 100_000


def test_oracle_pu_frc():
    pu = oracle.pu_frc(5.06, 920)
    assert 40_000 < pu < 50_000


def test_oracle_pu_ntnb():
    pu = oracle.pu_ntnb_anbima(7.50, 4500.0, date(2026, 4, 30), date(2029, 5, 15))
    assert pu > 0


def test_oracle_pu_ntnf():
    pu = oracle.pu_ntnf_anbima(13.80, date(2026, 4, 30), date(2031, 1, 1))
    assert pu > 0


def test_oracle_scenarios():
    for k in ("bull_par", "bear_par", "bull_steep", "bear_steep",
              "bull_flat", "bear_flat", "pos_fly", "neg_fly", "custom"):
        d = oracle.scenario_delta_bps(1000, 500, 1500, k, 10.0)
        assert isinstance(d, float)


def test_processed_legs_factory(processed_legs_factory, all_processed_legs):
    for name in PRESET_NAMES:
        legs = all_processed_legs[name]
        assert len(legs) == len(PRESETS_INPUT[name])
        for leg in legs:
            assert "instrument" in leg
            assert "pu" in leg
            assert "du" in leg
            assert leg["du"] > 0
            assert "venc" in leg


def test_market_snap(market_snap):
    assert market_snap.spot_usd > 0
    assert len(market_snap.di1) > 0
    assert len(market_snap.dap) > 0
    assert len(market_snap.frc) > 0
    assert len(market_snap.dol) > 0
