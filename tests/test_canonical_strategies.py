"""Testes das estrategias canonicas do livro B3 DAP cap.6 que NAO sao presets fixos.

Cobre:
- NTN-B Sintetica (LFT + DAP em direcoes opostas)
- Hedge IPCA Sintetico (DI1 + DAP em direcoes opostas)
- FRA Cupom IPCA / Direcional Inclinacao DAP (2 DAPs vctos diferentes opostos)
- Venda Casada NTN-B (V NTN-B + V DAP)
- Verifica economic_description em todas as estrategias
- Verifica que get_exposure(DAP) retorna swap equivalente do livro (ativo CDI)
"""

from __future__ import annotations

import pytest
from datetime import date

from lib.exposure import detect_strategy, analyze_risk_factors, get_exposure
from api.simulator import _process_raw_legs

from tests.conftest import DATA_NEG_STR, SPOT


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _process(legs_input, market_snap):
    """Processa legs com market mockado."""
    return _process_raw_legs(legs_input, DATA_NEG_STR, SPOT)


# ---------------------------------------------------------------------------
# 1. Swap equivalente do DAP (livro B3 Swap Equivalente)
# ---------------------------------------------------------------------------

class TestDapSwapEquivalente:
    def test_dap_comprado_ativo_cdi(self):
        """DAP comprado: ativo CDI (DI Over), passivo IPCA+cupom — livro B3."""
        exp = get_exposure("DAP", "C", 7.40)
        assert exp["ativo"] == "CDI"
        assert "IPCA+" in exp["passivo"]
        assert "7.400%" in exp["passivo"]

    def test_dap_vendido_passivo_cdi(self):
        """DAP vendido: oposto."""
        exp = get_exposure("DAP", "V", 7.40)
        assert exp["passivo"] == "CDI"
        assert "IPCA+" in exp["ativo"]


# ---------------------------------------------------------------------------
# 2. NTN-B Sintetica (LFT + V DAP) - livro B3 cap.6
# ---------------------------------------------------------------------------

class TestNtnbSintetica:
    @pytest.fixture
    def legs_ntnb_sint(self, market_snap):
        legs_input = [
            {"instrument":"LFT","ticker":"U29","direction":"C","quantity":100,"taxa":0.05,"corr_type":"Nenhuma","corr_value":0.0,"vna":18900.0},
            {"instrument":"DAP","ticker":"N29","direction":"V","quantity":5,"taxa":7.40,"corr_type":"Nenhuma","corr_value":0.0},
        ]
        return _process(legs_input, market_snap)

    def test_detect_strategy_ntnb_sint(self, legs_ntnb_sint):
        s = detect_strategy(legs_ntnb_sint, SPOT)
        assert s["type"] == "ntnb_sint"
        assert s["bmk"] == "IPCA"
        assert "NTN-B Sintetica" in s["name"]
        assert s["cupom_dap"] == 7.40

    def test_economic_description(self, legs_ntnb_sint):
        s = detect_strategy(legs_ntnb_sint, SPOT)
        assert "NTN-B Sintetica" in s["economic_description"]
        assert "livro B3 DAP" in s["economic_description"]

    def test_risk_factors_ntnb_sint(self, legs_ntnb_sint):
        s = detect_strategy(legs_ntnb_sint, SPOT)
        factors = analyze_risk_factors(legs_ntnb_sint, s)
        # Deve expor IPCA (porque vira NTN-B sintetica)
        ipca = next((f for f in factors if "Inflacao" in f["fator"]), None)
        assert ipca is not None
        assert ipca["exposto"] is True


# ---------------------------------------------------------------------------
# 3. Hedge IPCA Sintetico (DI1 + V DAP) - livro B3 cap.6
# ---------------------------------------------------------------------------

class TestHedgeIpcaSintetico:
    @pytest.fixture
    def legs_ipca_sint(self, market_snap):
        legs_input = [
            {"instrument":"DI1","ticker":"F29","direction":"C","quantity":20,"taxa":13.75,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"DAP","ticker":"N29","direction":"V","quantity":3,"taxa":7.40,"corr_type":"Nenhuma","corr_value":0.0},
        ]
        return _process(legs_input, market_snap)

    def test_detect_strategy_ipca_sint(self, legs_ipca_sint):
        s = detect_strategy(legs_ipca_sint, SPOT)
        assert s["type"] == "ipca_sint"
        assert s["bmk"] == "IPCA"
        assert "Hedge IPCA Sintetico" in s["name"]

    def test_economic_description(self, legs_ipca_sint):
        s = detect_strategy(legs_ipca_sint, SPOT)
        assert "Hedge IPCA Sintetico" in s["economic_description"]
        assert "DI" in s["economic_description"]
        assert "DAP" in s["economic_description"]

    def test_risk_factors_ipca_sint(self, legs_ipca_sint):
        s = detect_strategy(legs_ipca_sint, SPOT)
        factors = analyze_risk_factors(legs_ipca_sint, s)
        # IPCA exposto, CDI cancela, cupom real exposto
        ipca = next(f for f in factors if "Inflacao" in f["fator"])
        assert ipca["exposto"] is True
        nivel = next(f for f in factors if "Nivel" in f["fator"])
        assert nivel["exposto"] is False


# ---------------------------------------------------------------------------
# 4. FRA Cupom IPCA / Direcional Inclinacao (2 DAPs vctos diferentes opostos)
# ---------------------------------------------------------------------------

class TestFraCupomIpca:
    @pytest.fixture
    def legs_fra(self, market_snap):
        legs_input = [
            {"instrument":"DAP","ticker":"N28","direction":"C","quantity":10,"taxa":7.50,"corr_type":"Nenhuma","corr_value":0.0},
            {"instrument":"DAP","ticker":"N32","direction":"V","quantity":6,"taxa":7.35,"corr_type":"Nenhuma","corr_value":0.0},
        ]
        return _process(legs_input, market_snap)

    def test_detect_strategy_fra_real(self, legs_fra):
        s = detect_strategy(legs_fra, SPOT)
        assert s["type"] == "fra_real"
        assert "FRA Cupom IPCA" in s["name"] or "Direcional" in s["name"]

    def test_economic_description(self, legs_fra):
        s = detect_strategy(legs_fra, SPOT)
        assert "FRA" in s["economic_description"]
        assert "Inclinacao" in s["economic_description"] or "inclinacao" in s["economic_description"]

    def test_risk_factors_fra(self, legs_fra):
        s = detect_strategy(legs_fra, SPOT)
        factors = analyze_risk_factors(legs_fra, s)
        # Inclinacao exposta, paralelo cancela, IPCA cancela
        incl = next(f for f in factors if "Inclinacao" in f["fator"])
        assert incl["exposto"] is True
        ipca = next(f for f in factors if "Inflacao" in f["fator"])
        assert ipca["exposto"] is False


# ---------------------------------------------------------------------------
# 5. Venda Casada NTN-B (V NTN-B + V DAP) - livro B3 cap.6
# ---------------------------------------------------------------------------

class TestVendaCasadaNtnb:
    @pytest.fixture
    def legs_venda_casada(self, market_snap):
        legs_input = [
            {"instrument":"NTN-B","ticker":"N29","direction":"V","quantity":2000,"taxa":7.50,"corr_type":"% na taxa","corr_value":0.001,"vna":4500.0},
            {"instrument":"DAP","ticker":"N29","direction":"V","quantity":20,"taxa":7.40,"corr_type":"R$/contrato","corr_value":1.30},
        ]
        return _process(legs_input, market_snap)

    def test_detect_strategy_venda_casada(self, legs_venda_casada):
        s = detect_strategy(legs_venda_casada, SPOT)
        assert s["type"] == "casada"
        assert s["bmk"] == "CDI"
        assert "Venda Casada" in s["name"]

    def test_economic_description(self, legs_venda_casada):
        s = detect_strategy(legs_venda_casada, SPOT)
        assert "Venda Casada" in s["economic_description"]
        assert "CDI" in s["economic_description"]


# ---------------------------------------------------------------------------
# 6. Compatibilidade: presets atuais continuam tendo economic_description
# ---------------------------------------------------------------------------

class TestPresetsHaveEconomicDescription:
    @pytest.mark.parametrize("preset_name", [
        "Casada LTN+DI1", "Venda Casada LTN+DI1", "Casada NTN-F+DI1",
        "Casada NTN-B+DAP", "DOL+DI1 (cupom sint.)", "DI1+FRC (dol sint.)",
    ])
    def test_preset_has_economic_description(self, preset_name, all_processed_legs):
        s = detect_strategy(all_processed_legs[preset_name], SPOT)
        assert "economic_description" in s
        assert s["economic_description"]
        assert "name" in s

    @pytest.mark.parametrize("preset_name", [
        "Casada LTN+DI1", "Casada NTN-F+DI1",
    ])
    def test_casada_pre_mentions_book(self, preset_name, all_processed_legs):
        """Casada Pre cita comportamento economico."""
        s = detect_strategy(all_processed_legs[preset_name], SPOT)
        assert "CDI" in s["economic_description"]
        assert "spread" in s["economic_description"].lower()

    def test_carteira_ipca_flutuante_cita_livro(self, all_processed_legs):
        """Casada NTN-B+DAP comprado-comprado cita o nome canonico do livro B3."""
        s = detect_strategy(all_processed_legs["Casada NTN-B+DAP"], SPOT)
        assert "Carteira de NTN-B" in s["economic_description"]
        assert "Cupom de IPCA Flutuante" in s["economic_description"]
        assert "livro B3 DAP" in s["economic_description"]
