"""Testes dos fetchers ANBIMA: parsers determinísticos + mock HTTP.

Não usa rede em CI. Os parsers sao testados com samples reais
(capturados de ms260428.txt e brasilindicadores.com.br/titulos-publicos/vna/).
"""

from __future__ import annotations

from datetime import date

import pytest

from lib import anbima_fetchers as af


# ============================================================================
# Sample real do ms260428.txt (29/04/2026 - Treasury data captured live)
# ============================================================================

SAMPLE_TPF_TXT = """ANBIMA - Associa\xe7\xe3o Brasileira das Entidades dos Mercados Financeiro e de Capitais

Titulo@Data Referencia@Codigo SELIC@Data Base/Emissao@Data Vencimento@Tx. Compra@Tx. Venda@Tx. Indicativas@PU@Desvio padrao@Interv. Ind. Inf. (D0)@Interv. Ind. Sup. (D0)@Interv. Ind. Inf. (D+1)@Interv. Ind. Sup. (D+1)@Criterio
LTN@20260428@100000@20230106@20260701@14,3018@14,2485@14,2656@976,984714@0,02733668475382@14,1107@14,42@14,1337@14,4394@Calculado
LTN@20260428@100000@20250110@20320101@13,7563@13,745@13,7502@483,112051@0,00091714660224@13,2816@14,286@13,2893@14,2937@Calculado
NTN-B@20260428@760199@20000715@20290515@7,8434@7,8146@7,83@4597,816018@0@7,4756@8,1481@7,4834@8,1563@Calculado
NTN-F@20260428@950199@20180105@20290101@13,6761@13,6491@13,6616@957,047201@0,00131740485045@13,1612@14,1806@13,181@14,2004@Calculado
LFT@20260428@210100@20000701@20260901@0,0003@-0,0089@-0,0035@18886,609415@0,00316227765859@-0,0344@0,0222@-0,0365@0,0202@Calculado
"""

SAMPLE_VNA_HTML = """
<html><body><table><tbody>
    <tr>
        <td>760199</td>
        <td>29/04/2026</td>
        <td>R$ 4.687,318378</td>
        <td>0,67% (índice projetado)</td>
        <td>29/04/2026</td>
    </tr>
    <tr>
        <td>770100</td>
        <td>29/04/2026</td>
        <td>R$ 6.620,049870</td>
        <td>2,73% (índice fechado)</td>
        <td>29/04/2026</td>
    </tr>
    <tr>
        <td>210100</td>
        <td>29/04/2026</td>
        <td>R$ 18.896,631664</td>
        <td>14,65%</td>
    </tr>
</tbody></table></body></html>
"""


# ============================================================================
# 1. Helpers internos
# ============================================================================

class TestHelpers:
    def test_parse_br_decimal_simple(self):
        assert af._parse_br_decimal("14,2656") == 14.2656

    def test_parse_br_decimal_with_thousands(self):
        assert af._parse_br_decimal("4.687,318378") == 4687.318378
        assert af._parse_br_decimal("18.896,631664") == 18896.631664

    def test_parse_br_decimal_negative(self):
        assert af._parse_br_decimal("-0,0089") == -0.0089

    def test_parse_br_decimal_empty(self):
        assert af._parse_br_decimal("") == 0.0
        assert af._parse_br_decimal("   ") == 0.0

    def test_parse_yyyymmdd_valid(self):
        assert af._parse_yyyymmdd("20260428") == date(2026, 4, 28)

    def test_parse_yyyymmdd_invalid(self):
        assert af._parse_yyyymmdd("2026") is None
        assert af._parse_yyyymmdd("invalid") is None

    def test_parse_ddmmyyyy(self):
        assert af._parse_ddmmyyyy("29/04/2026") == date(2026, 4, 29)
        assert af._parse_ddmmyyyy("invalid") is None


# ============================================================================
# 2. Parser TPF TXT
# ============================================================================

class TestParseAnbimaTpfTxt:
    def test_parse_returns_records(self):
        records = af.parse_anbima_tpf_txt(SAMPLE_TPF_TXT)
        assert len(records) == 5

    def test_parse_skips_header(self):
        records = af.parse_anbima_tpf_txt(SAMPLE_TPF_TXT)
        for r in records:
            assert r.instrument != "Titulo"

    def test_parse_ltn_f32(self):
        records = af.parse_anbima_tpf_txt(SAMPLE_TPF_TXT)
        ltn_f32 = next(r for r in records if r.instrument == "LTN" and r.data_vencimento == date(2032, 1, 1))
        assert ltn_f32.selic_code == "100000"
        assert ltn_f32.data_ref == date(2026, 4, 28)
        assert ltn_f32.tx_indicativa == 13.7502
        assert ltn_f32.tx_compra == 13.7563
        assert ltn_f32.tx_venda == 13.745
        assert ltn_f32.pu == 483.112051
        assert ltn_f32.criterio == "Calculado"

    def test_parse_ntnb_n29(self):
        records = af.parse_anbima_tpf_txt(SAMPLE_TPF_TXT)
        ntnb = next(r for r in records if r.instrument == "NTN-B")
        assert ntnb.data_vencimento == date(2029, 5, 15)
        assert ntnb.selic_code == "760199"
        assert ntnb.tx_indicativa == 7.83
        assert ntnb.pu == 4597.816018
        assert ntnb.desvio_padrao == 0.0  # caso de zero exato

    def test_parse_ntnf_2029(self):
        records = af.parse_anbima_tpf_txt(SAMPLE_TPF_TXT)
        ntnf = next(r for r in records if r.instrument == "NTN-F")
        assert ntnf.data_vencimento == date(2029, 1, 1)
        assert ntnf.tx_indicativa == 13.6616

    def test_parse_lft_negative_yield(self):
        records = af.parse_anbima_tpf_txt(SAMPLE_TPF_TXT)
        lft = next(r for r in records if r.instrument == "LFT")
        # Tx venda negativa (-0,0089 = agio de 0.89bp)
        assert lft.tx_venda == -0.0089
        assert lft.tx_compra == 0.0003
        assert lft.tx_indicativa == -0.0035

    def test_parse_intervalos(self):
        records = af.parse_anbima_tpf_txt(SAMPLE_TPF_TXT)
        ltn_f32 = next(r for r in records if r.instrument == "LTN" and r.data_vencimento == date(2032, 1, 1))
        assert ltn_f32.intervalo_d0_inf == 13.2816
        assert ltn_f32.intervalo_d0_sup == 14.286
        assert ltn_f32.intervalo_d1_inf == 13.2893
        assert ltn_f32.intervalo_d1_sup == 14.2937

    def test_parse_empty_string(self):
        assert af.parse_anbima_tpf_txt("") == []

    def test_parse_malformed_skips_line(self):
        # Linha com poucos campos eh ignorada
        bad = "LTN@20260428@bad_data\n"
        assert af.parse_anbima_tpf_txt(bad) == []

    def test_record_to_dict(self):
        records = af.parse_anbima_tpf_txt(SAMPLE_TPF_TXT)
        d = records[0].to_dict()
        assert "instrument" in d
        assert "tx_indicativa" in d
        assert "pu" in d
        assert isinstance(d["data_ref"], str)


# ============================================================================
# 3. Parser VNA Brasil Indicadores
# ============================================================================

class TestParseVnaBrasilIndicadores:
    def test_parse_three_records(self):
        records = af.parse_vna_brasil_indicadores(SAMPLE_VNA_HTML)
        assert len(records) == 3

    def test_parse_ntnb(self):
        records = af.parse_vna_brasil_indicadores(SAMPLE_VNA_HTML)
        ntnb = next(r for r in records if r.instrument == "NTN-B")
        assert ntnb.selic_code == "760199"
        assert ntnb.vna == 4687.318378
        assert ntnb.data_ref == date(2026, 4, 29)
        assert "índice projetado" in ntnb.indice_str
        assert ntnb.data_atualizacao == date(2026, 4, 29)

    def test_parse_lft_no_data_atu(self):
        """LFT vem com 4 tds (sem data_atualizacao)."""
        records = af.parse_vna_brasil_indicadores(SAMPLE_VNA_HTML)
        lft = next(r for r in records if r.instrument == "LFT")
        assert lft.vna == 18896.631664
        assert lft.data_atualizacao is None

    def test_parse_ntnc(self):
        records = af.parse_vna_brasil_indicadores(SAMPLE_VNA_HTML)
        ntnc = next(r for r in records if r.instrument == "NTN-C")
        assert ntnc.vna == 6620.04987

    def test_parse_empty_html(self):
        assert af.parse_vna_brasil_indicadores("") == []

    def test_parse_html_no_tables(self):
        assert af.parse_vna_brasil_indicadores("<html><body>no data</body></html>") == []

    def test_parse_skips_unknown_codes(self):
        html = """
        <td>999999</td>
        <td>29/04/2026</td>
        <td>R$ 100,00</td>
        <td>1%</td>
        """
        assert af.parse_vna_brasil_indicadores(html) == []

    def test_record_to_dict(self):
        records = af.parse_vna_brasil_indicadores(SAMPLE_VNA_HTML)
        d = records[0].to_dict()
        assert "instrument" in d
        assert "vna" in d
        assert isinstance(d["vna"], float)


# ============================================================================
# 4. Mock HTTP fetchers
# ============================================================================

class TestFetchAnbimaTpfTxtMocked:
    def test_fetcher_uses_first_responding_date(self, monkeypatch):
        af.clear_cache()
        calls = []

        def mock_get(url, timeout=10, headers=None):
            calls.append(url)
            return SAMPLE_TPF_TXT.encode("latin-1")

        monkeypatch.setattr(af, "_http_get", mock_get)
        records = af.fetch_anbima_tpf_txt()
        assert len(records) == 5
        assert len(calls) == 1  # Para no primeiro sucesso
        assert "ms" in calls[0]
        assert ".txt" in calls[0]

    def test_fetcher_falls_back_after_failures(self, monkeypatch):
        af.clear_cache()
        attempts = []

        def mock_get(url, timeout=10, headers=None):
            attempts.append(url)
            if len(attempts) < 3:
                return None
            return SAMPLE_TPF_TXT.encode("latin-1")

        monkeypatch.setattr(af, "_http_get", mock_get)
        records = af.fetch_anbima_tpf_txt(reference_date=date(2026, 4, 28))
        assert len(records) == 5
        assert len(attempts) == 3

    def test_fetcher_returns_empty_when_all_fail(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: None)
        records = af.fetch_anbima_tpf_txt(reference_date=date(2026, 4, 28),
                                            fallback_lookback=2)
        assert records == []

    def test_fetcher_uses_cache(self, monkeypatch):
        af.clear_cache()
        call_count = [0]

        def mock_get(url, timeout=10, headers=None):
            call_count[0] += 1
            return SAMPLE_TPF_TXT.encode("latin-1")

        monkeypatch.setattr(af, "_http_get", mock_get)
        af.fetch_anbima_tpf_txt(reference_date=date(2026, 4, 28))
        af.fetch_anbima_tpf_txt(reference_date=date(2026, 4, 28))
        af.fetch_anbima_tpf_txt(reference_date=date(2026, 4, 28))
        assert call_count[0] == 1


class TestFetchVnaBrasilIndicadoresMocked:
    def test_fetcher_returns_records(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: SAMPLE_VNA_HTML.encode("utf-8"))
        records = af.fetch_vna_brasil_indicadores()
        assert len(records) == 3

    def test_fetcher_returns_empty_on_failure(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: None)
        records = af.fetch_vna_brasil_indicadores()
        assert records == []

    def test_get_vna_ntnb(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: SAMPLE_VNA_HTML.encode("utf-8"))
        assert af.get_vna_ntnb() == 4687.318378

    def test_get_vna_lft(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: SAMPLE_VNA_HTML.encode("utf-8"))
        assert af.get_vna_lft() == 18896.631664

    def test_get_vna_returns_none_when_unavailable(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: None)
        assert af.get_vna_ntnb() is None
        assert af.get_vna_lft() is None


# ============================================================================
# 5. Helpers de uso (grouping, find)
# ============================================================================

class TestHighLevelHelpers:
    def test_get_anbima_tpf_grouped(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: SAMPLE_TPF_TXT.encode("latin-1"))
        grouped = af.get_anbima_tpf_grouped()
        assert "LTN" in grouped
        assert "NTN-B" in grouped
        assert "NTN-F" in grouped
        assert "LFT" in grouped
        assert len(grouped["LTN"]) == 2
        assert len(grouped["NTN-B"]) == 1

    def test_get_anbima_tpf_grouped_sorted_by_vencimento(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: SAMPLE_TPF_TXT.encode("latin-1"))
        ltns = af.get_anbima_tpf_grouped()["LTN"]
        # Ordem por vencimento crescente
        assert ltns[0].data_vencimento < ltns[1].data_vencimento

    def test_get_vencimentos(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: SAMPLE_TPF_TXT.encode("latin-1"))
        vs = af.get_anbima_tpf_vencimentos("LTN")
        assert vs == ["2026-07-01", "2032-01-01"]

    def test_find_anbima_tpf(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: SAMPLE_TPF_TXT.encode("latin-1"))
        rec = af.find_anbima_tpf("LTN", date(2032, 1, 1))
        assert rec is not None
        assert rec.tx_indicativa == 13.7502

    def test_find_anbima_tpf_not_found(self, monkeypatch):
        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: SAMPLE_TPF_TXT.encode("latin-1"))
        rec = af.find_anbima_tpf("LTN", date(2099, 1, 1))
        assert rec is None


# ============================================================================
# 6. URL building
# ============================================================================

class TestUrlBuilding:
    def test_anbima_tpf_url_format(self):
        url = af._anbima_tpf_url(date(2026, 4, 28))
        assert url == "https://www.anbima.com.br/informacoes/merc-sec/arqs/ms260428.txt"

    def test_anbima_tpf_url_padding(self):
        url = af._anbima_tpf_url(date(2026, 1, 5))
        assert "ms260105.txt" in url

    def test_previous_business_days_skips_weekend(self):
        # 27/04/2026 = segunda DU
        bdays = af._previous_business_days(date(2026, 4, 27), 5)
        # Inclui 27/04 (segunda), 24/04 (sexta), 23, 22, 17 ... pulando fds
        assert date(2026, 4, 27) in bdays
        assert date(2026, 4, 24) in bdays
        # 25 e 26 sao fds
        assert date(2026, 4, 25) not in bdays
        assert date(2026, 4, 26) not in bdays


# ============================================================================
# 7. Integracao endpoints (com mock)
# ============================================================================

@pytest.fixture
def api_client_with_mock(monkeypatch, market_snap):
    """Cliente FastAPI com http mockado para os endpoints anbima."""
    from fastapi import FastAPI
    from fastapi.testclient import TestClient
    from api.simulator import router as sim_router

    af.clear_cache()

    def mock_http(url, timeout=10, headers=None):
        if "anbima.com.br" in url and url.endswith(".txt"):
            return SAMPLE_TPF_TXT.encode("latin-1")
        if "brasilindicadores" in url:
            return SAMPLE_VNA_HTML.encode("utf-8")
        return None

    monkeypatch.setattr(af, "_http_get", mock_http)

    app = FastAPI()
    app.include_router(sim_router, prefix="/sim")
    return TestClient(app)


class TestEndpoints:
    def test_get_vna_endpoint(self, api_client_with_mock):
        r = api_client_with_mock.get("/sim/vna")
        assert r.status_code == 200
        data = r.json()
        assert data["vna_ntnb"] == 4687.318378
        assert data["vna_lft"] == 18896.631664
        assert len(data["records"]) == 3

    def test_get_anbima_tpf_endpoint_all(self, api_client_with_mock):
        r = api_client_with_mock.get("/sim/anbima-tpf")
        assert r.status_code == 200
        data = r.json()
        assert data["data_ref"] == "2026-04-28"
        assert len(data["records"]) == 5

    def test_tickers_tpf_uses_anbima_when_available(self, api_client_with_mock):
        """GET /sim/tickers/LFT retorna lista do ANBIMA (sample tem 1 LFT: U26)."""
        r = api_client_with_mock.get("/sim/tickers/LFT")
        assert r.status_code == 200
        data = r.json()
        # Sample so tem LFT venc 2026-09-01 = U26
        assert "U26" in data["tickers"]

    def test_tickers_tpf_ltn_from_anbima(self, api_client_with_mock):
        """LTN tickers vem do ANBIMA (sample tem 2 LTNs: 2026-07-01 + 2032-01-01 = N26, F32)."""
        r = api_client_with_mock.get("/sim/tickers/LTN")
        assert r.status_code == 200
        data = r.json()
        assert "N26" in data["tickers"]
        assert "F32" in data["tickers"]

    def test_tickers_tpf_falls_back_when_anbima_offline(self, monkeypatch, market_snap):
        """Sem feed ANBIMA, tickers TPF caem no hardcoded TPF_VENCIMENTOS."""
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        from api.simulator import router

        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: None)

        app = FastAPI()
        app.include_router(router, prefix="/sim")
        c = TestClient(app)

        r = c.get("/sim/tickers/LFT")
        assert r.status_code == 200
        # hardcoded em lib/market_data tem 7 LFT vencimentos
        tickers = r.json()["tickers"]
        assert len(tickers) >= 1
        assert any(t.startswith("U") or t.startswith("H") for t in tickers)

    def test_get_anbima_tpf_filter_by_instrument(self, api_client_with_mock):
        r = api_client_with_mock.get("/sim/anbima-tpf?instrument=NTN-B")
        assert r.status_code == 200
        data = r.json()
        assert len(data["records"]) == 1
        assert data["records"][0]["instrument"] == "NTN-B"

    def test_get_presets_uses_dynamic_vna(self, api_client_with_mock):
        """GET /sim/presets retorna NTN-B com VNA do feed (mocked = 4687.318378)."""
        r = api_client_with_mock.get("/sim/presets")
        assert r.status_code == 200
        presets = r.json()
        ntnb_dap = presets["Casada NTN-B+DAP"]
        ntnb_leg = next(l for l in ntnb_dap if l["instrument"] == "NTN-B")
        assert ntnb_leg["vna"] == 4687.318378

    def test_get_presets_falls_back_when_feed_down(self, monkeypatch, market_snap):
        """Sem feed (mock retorna None), preset usa fallback hardcoded."""
        from fastapi import FastAPI
        from fastapi.testclient import TestClient
        from api.simulator import router, _FALLBACK_VNA_NTNB

        af.clear_cache()
        monkeypatch.setattr(af, "_http_get", lambda *a, **k: None)

        app = FastAPI()
        app.include_router(router, prefix="/sim")
        c = TestClient(app)

        r = c.get("/sim/presets")
        assert r.status_code == 200
        ntnb_dap = r.json()["Casada NTN-B+DAP"]
        ntnb_leg = next(l for l in ntnb_dap if l["instrument"] == "NTN-B")
        assert ntnb_leg["vna"] == _FALLBACK_VNA_NTNB
