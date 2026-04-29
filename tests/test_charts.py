"""Testes diretos das funcoes de chart em casada-tool/lib/charts.py.

Foco: garantir que scenario_key+magnitude produz outputs diferentes nos
charts de cupom, forward e taxa real (que antes eram inertes ao cenario).
"""

from __future__ import annotations

import pytest

from lib.charts import (
    chart_curva_antes_depois, chart_cupom_cambial,
    chart_dol_forward, chart_taxa_real,
)

from tests.conftest import LIQ_DATE, SPOT


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _trace_y(fig, name_substring):
    """Pega o array y do primeiro trace cujo name contenha substring."""
    for trace in fig.data:
        if name_substring.lower() in (getattr(trace, "name", "") or "").lower():
            return list(trace.y) if trace.y is not None else []
    return []


# ---------------------------------------------------------------------------
# 1. chart_cupom_cambial responde a scenario_key
# ---------------------------------------------------------------------------

class TestCupomChartScenario:
    def test_bull_par_shifts_curve_down(self, market_snap):
        fig0 = chart_cupom_cambial(market_snap.frc, scenario_key="bull_par", magnitude=0)
        fig10 = chart_cupom_cambial(market_snap.frc, scenario_key="bull_par", magnitude=10)
        before = _trace_y(fig0, "Antes")
        after_zero = _trace_y(fig0, "Depois")
        after_bull10 = _trace_y(fig10, "Depois")
        assert before == after_zero  # mag=0 -> sem deslocamento
        assert all(b - a == pytest.approx(0.10, abs=1e-9) for b, a in zip(before, after_bull10))  # -10 bps em todo lugar

    def test_bear_par_shifts_curve_up(self, market_snap):
        fig = chart_cupom_cambial(market_snap.frc, scenario_key="bear_par", magnitude=10)
        before = _trace_y(fig, "Antes")
        after = _trace_y(fig, "Depois")
        assert all(a - b == pytest.approx(0.10, abs=1e-9) for b, a in zip(before, after))

    def test_steepener_creates_slope(self, market_snap):
        fig = chart_cupom_cambial(market_snap.frc, scenario_key="bear_steep", magnitude=20)
        before = _trace_y(fig, "Antes")
        after = _trace_y(fig, "Depois")
        deltas = [a - b for b, a in zip(before, after)]
        # bear_steep: curtos pouco mexem, longos sobem
        assert deltas[-1] > deltas[0]
        # Magnitude maxima ~20 bps no ponto mais longo
        assert deltas[-1] < 0.21

    def test_slider_delta_cupom_added_to_scenario(self, market_snap):
        # Bull paralelo -10 bps + slider +5 bps = -5 bps liquido
        fig = chart_cupom_cambial(market_snap.frc, delta_cupom_bps=5,
                                   scenario_key="bull_par", magnitude=10)
        before = _trace_y(fig, "Antes")
        after = _trace_y(fig, "Depois")
        # -10 + 5 = -5 bps -> after = before - 0.05
        assert all(b - a == pytest.approx(0.05, abs=1e-9) for b, a in zip(before, after))


# ---------------------------------------------------------------------------
# 2. chart_dol_forward responde a scenario_key
# ---------------------------------------------------------------------------

class TestForwardChartScenario:
    def test_bull_par_changes_forward(self, market_snap):
        fig0 = chart_dol_forward(market_snap.di1, market_snap.frc, market_snap.spot_usd,
                                  scenario_key="bull_par", magnitude=0)
        fig10 = chart_dol_forward(market_snap.di1, market_snap.frc, market_snap.spot_usd,
                                   scenario_key="bull_par", magnitude=10)
        before = _trace_y(fig0, "Antes")
        after_zero = _trace_y(fig0, "Depois")
        after_bull10 = _trace_y(fig10, "Depois")

        # mag=0: forward antes == depois
        assert before == pytest.approx(after_zero, abs=1e-9)

        # mag=10 Bull: DI cai 10bp e FRC cai 10bp; o forward muda mas o sinal
        # depende da convencao. O importante: difere de zero.
        diffs = [b - a for b, a in zip(before, after_bull10)]
        assert any(abs(d) > 1e-6 for d in diffs)

    def test_fx_shock_shifts_spot_in_forward(self, market_snap):
        fig = chart_dol_forward(market_snap.di1, market_snap.frc, market_snap.spot_usd,
                                 delta_fx_pct=5.0, scenario_key="bull_par", magnitude=0)
        before = _trace_y(fig, "Antes")
        after = _trace_y(fig, "Depois")
        # FX +5% -> forward sobe ~5% em todos os vertices
        ratios = [a / b for b, a in zip(before, after) if b > 0]
        assert all(r == pytest.approx(1.05, rel=0.01) for r in ratios)


# ---------------------------------------------------------------------------
# 3. chart_taxa_real responde a scenario_key
# ---------------------------------------------------------------------------

class TestRealChartScenario:
    def test_bull_par_shifts_dap_down(self, market_snap):
        fig = chart_taxa_real(market_snap.dap, scenario_key="bull_par", magnitude=10)
        before = _trace_y(fig, "Antes")
        after = _trace_y(fig, "Depois")
        assert all(b - a == pytest.approx(0.10, abs=1e-9) for b, a in zip(before, after))

    def test_bear_steep_creates_slope(self, market_snap):
        fig = chart_taxa_real(market_snap.dap, scenario_key="bear_steep", magnitude=20)
        before = _trace_y(fig, "Antes")
        after = _trace_y(fig, "Depois")
        deltas = [a - b for b, a in zip(before, after)]
        # bear_steep: longos sobem mais que curtos
        assert deltas[-1] > deltas[0]

    def test_slider_delta_ipca_added_to_scenario(self, market_snap):
        fig = chart_taxa_real(market_snap.dap, delta_ipca_bps=5,
                               scenario_key="bull_par", magnitude=10)
        before = _trace_y(fig, "Antes")
        after = _trace_y(fig, "Depois")
        # -10 + 5 = -5 bps
        assert all(b - a == pytest.approx(0.05, abs=1e-9) for b, a in zip(before, after))


# ---------------------------------------------------------------------------
# 4. Coerencia: P&L da FRC/DAP em Bull Parallel bate com chart shift
# ---------------------------------------------------------------------------

class TestCoerenciaPnlVsChart:
    def test_pnl_frc_consistent_with_cupom_chart_bull_par(self, all_processed_legs, market_snap):
        """Em DI1+FRC com Bull Parallel mag=10, o P&L da FRC corresponde a um
        deslocamento de -10 bps na curva (mesmo deslocamento exibido no chart)."""
        from lib.scenarios import calc_leg_pnl

        legs = all_processed_legs["DI1+FRC (dol sint.)"]
        frc = next(l for l in legs if l["instrument"] == "FRC")

        # Aplica Bull Parallel mag=10: para FRC o cenario aplicado eh -10 bps
        pnl_real = calc_leg_pnl(frc, -10)  # delta direto na taxa pre
        # FRC linear: -sign * dv01_total * delta_bps; sign=+1 para FRC vendido
        sign = -1 if frc["direction"] == "C" else 1
        pnl_linear = -sign * frc["dv01_total"] * (-10)
        # Tem que ter mesmo sinal (direcao do P&L)
        assert (pnl_real >= 0) == (pnl_linear >= 0)
        # E magnitude proxima (FRC eh lin360, convexidade pequena)
        assert abs(pnl_real - pnl_linear) / max(abs(pnl_real), 1) < 0.05

    def test_pnl_dap_consistent_with_real_chart_bull_par(self, all_processed_legs, market_snap):
        """Em NTN-B+DAP com Bull Parallel mag=10, o P&L da DAP corresponde a -10bps."""
        from lib.scenarios import calc_leg_pnl

        legs = all_processed_legs["Casada NTN-B+DAP"]
        dap = next(l for l in legs if l["instrument"] == "DAP")

        pnl_real = calc_leg_pnl(dap, -10)
        sign = -1 if dap["direction"] == "C" else 1
        pnl_linear = -sign * dap["dv01_total"] * (-10)
        assert (pnl_real >= 0) == (pnl_linear >= 0)
        assert abs(pnl_real - pnl_linear) / max(abs(pnl_real), 1) < 0.05
