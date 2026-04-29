"""Testes do motor generico de exposicoes (compute_net_exposure).

Cobre:
- Cancelamento Pre (LTN+DI1)
- Cancelamento IPCA+ (NTN-B+DAP)
- Sem cancelamento (NTN-F+DAP, LTN+FRC): fatores diferentes nao cancelam
- 3 pernas (LTN+DI1+FRC): Pre cancela, CDI cancela, CupLimpo residual
- Perna unica (NTN-B solo): IPCA+ residual
- DOL: USD residual
- Deteccao generica via detect_strategy type="generic" com risk factors automaticos
"""

from __future__ import annotations

import pytest

from lib.exposure import compute_net_exposure, detect_strategy, analyze_risk_factors
from api.simulator import _process_raw_legs

from tests.conftest import DATA_NEG_STR, SPOT


def _process(legs_input):
    return _process_raw_legs(legs_input, DATA_NEG_STR, SPOT)


# ============================================================================
# 1. Cancelamento basico
# ============================================================================

class TestCancelamentoPre:
    def test_ltn_di1_pre_cancela(self):
        """LTN C + DI1 C mesmo vcto: Pre cancela, CDI residual."""
        legs = _process([
            {"instrument":"LTN","ticker":"F32","direction":"C","quantity":2000,"taxa":13.76,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"DI1","ticker":"F32","direction":"C","quantity":20,"taxa":13.65,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        net = compute_net_exposure(legs)
        pre_cancel = next((c for c in net["cancelled"] if c["factor"] == "Pre"), None)
        assert pre_cancel is not None
        assert pre_cancel["spread_bps"] == pytest.approx(11.0, abs=1)
        cdi_residual = next((r for r in net["residual"] if r["factor"] == "CDI"), None)
        assert cdi_residual is not None
        assert "CDI" in net["result_label"]

    def test_ntnf_di1_pre_cancela(self):
        """NTN-F C + DI1 C: mesma logica."""
        legs = _process([
            {"instrument":"NTN-F","ticker":"F31","direction":"C","quantity":2000,"taxa":13.80,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"DI1","ticker":"F31","direction":"C","quantity":20,"taxa":13.65,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        net = compute_net_exposure(legs)
        pre_cancel = next((c for c in net["cancelled"] if c["factor"] == "Pre"), None)
        assert pre_cancel is not None
        assert pre_cancel["spread_bps"] == pytest.approx(15.0, abs=1)


class TestCancelamentoIpca:
    def test_ntnb_dap_ipca_cancela(self):
        """NTN-B C + DAP C: IPCA+ cancela, CDI residual."""
        legs = _process([
            {"instrument":"NTN-B","ticker":"N29","direction":"C","quantity":2000,"taxa":7.50,"corr_type":"Nenhuma","corr_value":0.0,"vna":4500.0},
            {"instrument":"DAP","ticker":"N29","direction":"C","quantity":20,"taxa":7.40,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        net = compute_net_exposure(legs)
        ipca_cancel = next((c for c in net["cancelled"] if c["factor"] == "IPCA+"), None)
        assert ipca_cancel is not None
        assert ipca_cancel["spread_bps"] == pytest.approx(10.0, abs=1)
        assert "CDI" in net["result_label"]


# ============================================================================
# 2. Sem cancelamento (fatores diferentes nao se cortam)
# ============================================================================

class TestSemCancelamento:
    def test_ntnf_dap_nao_cancela(self):
        """NTN-F C + DAP C: Pre e IPCA+ sao fatores DIFERENTES, nao cancelam."""
        legs = _process([
            {"instrument":"NTN-F","ticker":"F31","direction":"C","quantity":2000,"taxa":13.80,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"DAP","ticker":"N29","direction":"C","quantity":20,"taxa":7.40,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        net = compute_net_exposure(legs)
        # Pre e IPCA+ devem estar em residual, nao cancelado
        pre_residual = next((r for r in net["residual"] if r["factor"] == "Pre"), None)
        ipca_residual = next((r for r in net["residual"] if r["factor"] == "IPCA+"), None)
        assert pre_residual is not None, "Pre deveria ser residual (nao cancela com IPCA+)"
        assert ipca_residual is not None, "IPCA+ deveria ser residual"
        assert len(net["cancelled"]) == 0 or all(c["factor"] == "CDI" for c in net["cancelled"])

    def test_ltn_frc_nao_cancela(self):
        """LTN C + FRC V: Pre e CupLimpo sao fatores diferentes."""
        legs = _process([
            {"instrument":"LTN","ticker":"F32","direction":"C","quantity":2000,"taxa":13.76,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"FRC","ticker":"F28","direction":"V","quantity":20,"taxa":5.06,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        net = compute_net_exposure(legs)
        pre_residual = next((r for r in net["residual"] if r["factor"] == "Pre"), None)
        cup_residual = next((r for r in net["residual"] if r["factor"] == "CupLimpo"), None)
        assert pre_residual is not None
        assert cup_residual is not None


# ============================================================================
# 3. Multi-perna (3+)
# ============================================================================

class TestMultiPerna:
    def test_ltn_di1_frc_3_pernas(self):
        """LTN C + DI1 C + FRC V: Pre cancela, CDI cancela, CupLimpo residual."""
        legs = _process([
            {"instrument":"LTN","ticker":"F32","direction":"C","quantity":2000,"taxa":13.76,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"DI1","ticker":"F32","direction":"C","quantity":20,"taxa":13.65,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"FRC","ticker":"F28","direction":"V","quantity":20,"taxa":5.06,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        net = compute_net_exposure(legs)
        pre_cancel = next((c for c in net["cancelled"] if c["factor"] == "Pre"), None)
        cdi_cancel = next((c for c in net["cancelled"] if c["factor"] == "CDI"), None)
        cup_residual = next((r for r in net["residual"] if r["factor"] == "CupLimpo"), None)
        assert pre_cancel is not None
        assert cdi_cancel is not None
        assert cup_residual is not None
        assert cup_residual["rate_total"] == pytest.approx(5.06, abs=0.01)


# ============================================================================
# 4. Perna unica
# ============================================================================

class TestPernaUnica:
    def test_ntnb_solo_ipca_residual(self):
        """NTN-B C sozinha: IPCA+ 7.50% residual."""
        legs = _process([
            {"instrument":"NTN-B","ticker":"N29","direction":"C","quantity":2000,"taxa":7.50,"corr_type":"Nenhuma","corr_value":0.0,"vna":4500.0},
        ])
        net = compute_net_exposure(legs)
        assert len(net["cancelled"]) == 0
        ipca = next((r for r in net["residual"] if r["factor"] == "IPCA+"), None)
        assert ipca is not None
        assert ipca["rate_total"] == pytest.approx(7.50, abs=0.01)

    def test_dol_solo_usd_residual(self):
        """DOL C sozinho: USD residual."""
        legs = _process([
            {"instrument":"DOL","ticker":"K26","direction":"C","quantity":10,"taxa":4976.5,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        net = compute_net_exposure(legs)
        usd = next((r for r in net["residual"] if r["factor"] == "USD"), None)
        assert usd is not None


# ============================================================================
# 5. detect_strategy retorna type="generic" com net_exposure + risk factors auto
# ============================================================================

class TestGenericDetection:
    def test_ntnf_dap_generic_type(self):
        """Combinacao nao-padrao: detect_strategy retorna type='generic' com net_exposure."""
        legs = _process([
            {"instrument":"NTN-F","ticker":"F31","direction":"C","quantity":2000,"taxa":13.80,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"DAP","ticker":"N29","direction":"C","quantity":20,"taxa":7.40,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        strat = detect_strategy(legs, SPOT)
        assert strat["type"] == "generic"
        assert "net_exposure" in strat
        assert strat["economic_description"]

    def test_generic_has_risk_factors(self):
        """Combinacao generica tem fatores de risco derivados automaticamente."""
        legs = _process([
            {"instrument":"NTN-F","ticker":"F31","direction":"C","quantity":2000,"taxa":13.80,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"DAP","ticker":"N29","direction":"C","quantity":20,"taxa":7.40,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        strat = detect_strategy(legs, SPOT)
        factors = analyze_risk_factors(legs, strat)
        assert len(factors) > 0
        # Pre deve aparecer como fator exposto (nao cancela)
        pre_factor = next((f for f in factors if "Pre" in f["fator"]), None)
        assert pre_factor is not None
        assert pre_factor["exposto"] is True

    def test_ltn_frc_generic_factors(self):
        """LTN C + FRC V: fatores Pre e CupLimpo expostos."""
        legs = _process([
            {"instrument":"LTN","ticker":"F32","direction":"C","quantity":2000,"taxa":13.76,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"FRC","ticker":"F28","direction":"V","quantity":20,"taxa":5.06,"corr_type":"Nenhuma","corr_value":0.0},
        ])
        strat = detect_strategy(legs, SPOT)
        factors = analyze_risk_factors(legs, strat)
        factor_names = [f["fator"] for f in factors]
        assert any("Pre" in n for n in factor_names)
        assert any("CupLimpo" in n for n in factor_names)


# ============================================================================
# 6. Presets existentes continuam com type != "generic" (hardcoded funciona)
# ============================================================================

class TestHardcodedPreservado:
    def test_casada_ltn_di1_is_casada(self, all_processed_legs):
        strat = detect_strategy(all_processed_legs["Casada LTN+DI1"], SPOT)
        assert strat["type"] == "casada"
        assert "net_exposure" in strat

    def test_casada_ntnb_dap_is_casada(self, all_processed_legs):
        strat = detect_strategy(all_processed_legs["Casada NTN-B+DAP"], SPOT)
        assert strat["type"] == "casada"
        assert "net_exposure" in strat

    def test_dol_di1_is_cupom_sint(self, all_processed_legs):
        strat = detect_strategy(all_processed_legs["DOL+DI1 (cupom sint.)"], SPOT)
        assert strat["type"] == "cupom_sint"

    def test_di1_frc_is_dol_sint(self, all_processed_legs):
        strat = detect_strategy(all_processed_legs["DI1+FRC (dol sint.)"], SPOT)
        assert strat["type"] == "dol_sint"

    def test_single_legs_are_single(self, all_processed_legs):
        for name in ("FRC direcional", "LTN direcional"):
            strat = detect_strategy(all_processed_legs[name], SPOT)
            assert strat["type"] == "single"
            assert "net_exposure" in strat
