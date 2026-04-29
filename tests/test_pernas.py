"""Validacao bit-a-bit de cada perna processada de cada preset.

Para cada perna de cada preset valida:
- du, dc, taxa, tax_fin (apos corretagem)
- pu (vs oracle.pu_*_float e oracle.pu_*_anbima)
- fin = pu * quantity (exceto DOL onde fin = cotacao * mult * qty)
- noc = quantity * face
- d_mac, d_mod (duration)
- dv01_unit, dv01_total
- corr_brl, corr_bps
- side, tax_dir, exp.ativo, exp.passivo
- cashflows.flows[] (NTN-F, NTN-B): du, nominal, pv, peso, krd

Tolerancias documentadas em conftest.py.
"""

from __future__ import annotations

import math
from datetime import date

import pytest

from lib.instruments import INSTRUMENTS
from lib.calendar import du_entre, dc_entre, parse_ticker

from tests import oracle
from tests.conftest import (
    LIQ_DATE, TOL_PU, TOL_PU_NTNB, TOL_PU_LFT,
    TOL_DURATION, TOL_DV01_REL, TOL_PNL,
)
from tests.presets import PRESETS_INPUT, PRESET_NAMES


# ----------------------------------------------------------------------------
# Helpers de identificacao
# ----------------------------------------------------------------------------

def _expected_du_dc(instrument: str, ticker: str) -> tuple[int, int, date]:
    parsed = parse_ticker(instrument, ticker)
    venc = parsed["date"]
    du = du_entre(LIQ_DATE, venc)
    dc = dc_entre(LIQ_DATE, venc)
    return du, dc, venc


def _all_legs():
    """Generator: (preset_name, leg_idx, leg_input) para todas as 14 pernas."""
    for name in PRESET_NAMES:
        for i, leg in enumerate(PRESETS_INPUT[name]):
            yield (name, i, leg)


def _ids(items):
    return [f"{p}#{i}-{l['instrument']}" for p, i, l in items]


# Lista materializada para parametrize ids
ALL_LEGS = list(_all_legs())
ALL_LEG_IDS = _ids(ALL_LEGS)


# ----------------------------------------------------------------------------
# DU / DC / Datas
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_du_dc(preset_name, leg_idx, leg_input, all_processed_legs):
    """DU/DC da perna batem com calendario ANBIMA."""
    leg = all_processed_legs[preset_name][leg_idx]
    exp_du, exp_dc, exp_venc = _expected_du_dc(leg_input["instrument"], leg_input["ticker"])
    assert leg["du"] == exp_du, f"DU mismatch: lib={leg['du']} expected={exp_du}"
    assert leg["dc"] == exp_dc, f"DC mismatch: lib={leg['dc']} expected={exp_dc}"
    assert leg["parsed"]["date"] == exp_venc


# ----------------------------------------------------------------------------
# Tax / Tax_fin (corretagem aplicada)
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_tax_fin(preset_name, leg_idx, leg_input, all_processed_legs):
    """tax_fin reflete corretagem '% na taxa' corretamente.

    Regra:
    - 'Nenhuma' ou price (DOL): tax_fin == taxa
    - 'R$/contrato' / 'R$/titulo': nao altera taxa
    - '% na taxa': comprado subtrai (vendido em taxa); vendido soma
    """
    leg = all_processed_legs[preset_name][leg_idx]
    info = INSTRUMENTS[leg_input["instrument"]]
    corr_type = leg_input.get("corr_type", "Nenhuma")
    corr_value = leg_input.get("corr_value", 0.0)
    taxa = leg_input["taxa"]

    if corr_type == "% na taxa" and info.conv != "price":
        if leg_input["direction"] == "C":
            expected = taxa - corr_value
        else:
            expected = taxa + corr_value
    else:
        expected = taxa

    assert leg["tax_fin"] == pytest.approx(expected, abs=1e-12)


# ----------------------------------------------------------------------------
# PU (compliance ANBIMA + regression float)
# ----------------------------------------------------------------------------

def _oracle_pu_float(leg_input: dict, du: int, dc: int, venc: date) -> float:
    """Oracle PU float-puro replicando exatamente lib/instruments.pu.

    NOTA: simulator usa taxa BRUTA (leg['taxa']) para PU/duration/DV01,
    nao tax_fin. tax_fin so eh exibido.
    """
    inst = leg_input["instrument"]
    taxa = leg_input["taxa"]
    vna = leg_input.get("vna")
    return oracle._pu_for_leg(inst, taxa, du, dc, LIQ_DATE, venc, vna)


def _oracle_pu_anbima(leg_input: dict, du: int, dc: int, venc: date) -> float:
    """Oracle PU com truncamentos ANBIMA quando aplicavel. Usa taxa BRUTA."""
    inst = leg_input["instrument"]
    taxa = leg_input["taxa"]
    vna = leg_input.get("vna")

    if inst == "LTN":
        return oracle.pu_ltn_anbima(taxa, du)
    if inst == "NTN-F":
        return oracle.pu_ntnf_anbima(taxa, LIQ_DATE, venc)
    if inst == "NTN-B":
        return oracle.pu_ntnb_anbima(taxa, vna or 100.0, LIQ_DATE, venc)
    if inst == "LFT":
        return oracle.pu_lft_anbima(taxa, vna or 1000.0, du)
    if inst == "DI1" or inst == "DAP":
        return oracle.pu_di1(taxa, du)
    if inst == "DDI":
        return oracle.pu_ddi(taxa, dc)
    if inst == "FRC":
        return oracle.pu_frc(taxa, dc)
    if inst == "DOL":
        return oracle.pu_dol(taxa)
    raise ValueError(inst)


@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_pu_float_regression(preset_name, leg_idx, leg_input, all_processed_legs):
    """PU do lib bate exatamente (float) com a formula float-pura."""
    leg = all_processed_legs[preset_name][leg_idx]
    exp_du, exp_dc, exp_venc = _expected_du_dc(leg_input["instrument"], leg_input["ticker"])
    expected = _oracle_pu_float(leg_input, exp_du, exp_dc, exp_venc)
    assert leg["pu"] == pytest.approx(expected, rel=1e-9, abs=1e-9)


@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_pu_anbima_compliance(preset_name, leg_idx, leg_input, all_processed_legs):
    """PU do lib esta dentro da tolerancia ANBIMA (truncado)."""
    leg = all_processed_legs[preset_name][leg_idx]
    exp_du, exp_dc, exp_venc = _expected_du_dc(leg_input["instrument"], leg_input["ticker"])
    expected = _oracle_pu_anbima(leg_input, exp_du, exp_dc, exp_venc)

    inst = leg_input["instrument"]
    if inst == "NTN-B":
        tol = TOL_PU_NTNB
    elif inst == "LFT":
        tol = TOL_PU_LFT
    else:
        tol = TOL_PU

    assert leg["pu"] == pytest.approx(expected, abs=tol)


# ----------------------------------------------------------------------------
# Financeiro / Nocional
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_fin_noc(preset_name, leg_idx, leg_input, all_processed_legs):
    """fin = pu * quantity, noc = quantity * face."""
    leg = all_processed_legs[preset_name][leg_idx]
    info = INSTRUMENTS[leg_input["instrument"]]
    qty = leg_input["quantity"]

    expected_fin = leg["pu"] * qty
    expected_noc = qty * info.face

    assert leg["fin"] == pytest.approx(expected_fin, rel=1e-9)
    assert leg["noc"] == pytest.approx(expected_noc, rel=1e-9)


# ----------------------------------------------------------------------------
# Duration (Macaulay e Modificada)
# ----------------------------------------------------------------------------

def _expected_duration(leg_input: dict, du: int, dc: int, venc: date) -> tuple[float, float]:
    """Duration usando taxa BRUTA (igual lib/simulator)."""
    inst = leg_input["instrument"]
    info = INSTRUMENTS[inst]
    taxa = leg_input["taxa"]

    if info.conv == "price":
        return 0.0, 0.0
    if info.conv == "lin360":
        return oracle.duration_lin360(taxa, dc)
    if info.cup_sem == 0:
        return oracle.duration_zero_coupon(taxa, du)

    # NTN-F, NTN-B: with coupons
    if inst == "NTN-F":
        flows = oracle.coupon_flows_ntnf(LIQ_DATE, venc)
    else:
        flows = oracle.coupon_flows_ntnb(LIQ_DATE, venc)
    return oracle.duration_with_coupons(taxa, flows)


@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_duration(preset_name, leg_idx, leg_input, all_processed_legs):
    """Duration Macaulay e Modificada batem com oracle."""
    leg = all_processed_legs[preset_name][leg_idx]
    exp_du, exp_dc, exp_venc = _expected_du_dc(leg_input["instrument"], leg_input["ticker"])
    exp_mac, exp_mod = _expected_duration(leg_input, exp_du, exp_dc, exp_venc)
    assert leg["d_mac"] == pytest.approx(exp_mac, abs=TOL_DURATION)
    assert leg["d_mod"] == pytest.approx(exp_mod, abs=TOL_DURATION)


# ----------------------------------------------------------------------------
# DV01 (unit + total)
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_dv01(preset_name, leg_idx, leg_input, all_processed_legs):
    """DV01 unit = D_mod * PU * 0.0001; total = unit * qty (exceto DOL: 50/contrato).

    Para DOL: dv01_unit = mult (50), dv01_total = mult * qty.
    """
    leg = all_processed_legs[preset_name][leg_idx]
    info = INSTRUMENTS[leg_input["instrument"]]
    qty = leg_input["quantity"]

    if info.conv == "price":
        # DOL
        assert leg["dv01_unit"] == pytest.approx(50.0, rel=TOL_DV01_REL)
        assert leg["dv01_total"] == pytest.approx(50.0 * qty, rel=TOL_DV01_REL)
        return

    expected_unit = oracle.dv01_unit(leg["d_mod"], leg["pu"])
    assert leg["dv01_unit"] == pytest.approx(expected_unit, rel=TOL_DV01_REL)
    assert leg["dv01_total"] == pytest.approx(expected_unit * qty, rel=TOL_DV01_REL)


# ----------------------------------------------------------------------------
# Corretagem
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_corretagem(preset_name, leg_idx, leg_input, all_processed_legs):
    """corr_brl e corr_bps consistentes com tipo/valor."""
    leg = all_processed_legs[preset_name][leg_idx]
    info = INSTRUMENTS[leg_input["instrument"]]
    corr_type = leg_input.get("corr_type", "Nenhuma")
    corr_value = leg_input.get("corr_value", 0.0)
    qty = leg_input["quantity"]

    if corr_type == "Nenhuma":
        assert leg["corr_brl"] == 0.0
        assert leg["corr_bps"] == 0.0
        return

    if corr_type in ("R$/contrato", "R$/titulo"):
        assert leg["corr_brl"] == pytest.approx(corr_value * qty, rel=1e-9)
        if leg["dv01_total"] > 0:
            expected_bps = (corr_value * qty) / leg["dv01_total"]
            assert leg["corr_bps"] == pytest.approx(expected_bps, rel=TOL_DV01_REL)
        return

    if corr_type == "% na taxa" and info.conv != "price":
        # corr_brl = abs(PU(tax_fin) - PU(taxa_bruta)) * qty
        exp_du, exp_dc, exp_venc = _expected_du_dc(leg_input["instrument"], leg_input["ticker"])
        # PU com tax_fin (apos corretagem)
        tax_fin = leg["tax_fin"]
        vna = leg_input.get("vna")
        pu_tax_fin = oracle._pu_for_leg(
            leg_input["instrument"], tax_fin, exp_du, exp_dc, LIQ_DATE, exp_venc, vna,
        )
        expected_brl = abs(pu_tax_fin - leg["pu"]) * qty
        expected_bps = corr_value * 100  # % -> bps
        assert leg["corr_brl"] == pytest.approx(expected_brl, rel=1e-6, abs=1e-3)
        assert leg["corr_bps"] == pytest.approx(expected_bps, rel=1e-9)


# ----------------------------------------------------------------------------
# Side / Tax_dir / Exposure
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_side_tax_dir(preset_name, leg_idx, leg_input, all_processed_legs):
    """side e tax_dir corretos por tipo de instrumento e direcao.

    Regras do simulator:
    - tpf ou price: side = Ativo se C, Passivo se V
    - deriv (DI1/DAP/DDI/FRC): side = Passivo se C, Ativo se V
    - DOL (price): tax_dir = 'Compra USD' se C, 'Vende USD' se V
    - tpf: tax_dir = 'Vende taxa' se C, 'Compra taxa' se V
    - deriv: tax_dir = 'Compra taxa' se C, 'Vende taxa' se V
    """
    leg = all_processed_legs[preset_name][leg_idx]
    info = INSTRUMENTS[leg_input["instrument"]]
    direction = leg_input["direction"]

    if info.type == "tpf" or info.conv == "price":
        expected_side = "Ativo" if direction == "C" else "Passivo"
    else:
        expected_side = "Passivo" if direction == "C" else "Ativo"

    if info.conv == "price":
        expected_tax_dir = "Compra USD" if direction == "C" else "Vende USD"
    elif info.type == "tpf":
        expected_tax_dir = "Vende taxa" if direction == "C" else "Compra taxa"
    else:
        expected_tax_dir = "Compra taxa" if direction == "C" else "Vende taxa"

    assert leg["side"] == expected_side
    assert leg["tax_dir"] == expected_tax_dir


@pytest.mark.parametrize("preset_name,leg_idx,leg_input", ALL_LEGS, ids=ALL_LEG_IDS)
def test_exposure(preset_name, leg_idx, leg_input, all_processed_legs):
    """exp.ativo e exp.passivo corretos.

    Ver lib/exposure.get_exposure (swap equivalente livro B3):
    - DOL (price): C -> ativo='DOL <cot>', passivo='—'; V -> oposto
    - TPF: C -> ativo='<bench> <taxa>%', passivo='—'; V -> oposto
    - cupom (DDI, FRC): C -> ativo='CDI', passivo='<bench> <taxa>%'; V -> oposto
    - DI1: C -> ativo='CDI', passivo='Pre <taxa>%'; V -> oposto
    - DAP: C -> ativo='CDI' (DI Over), passivo='IPCA+ <taxa>%'; V -> oposto
      (livro B3 DAP, secao Swap Equivalente: comprador DAP fica ativo em DI Over,
       passivo em IPCA + Cupom)
    """
    leg = all_processed_legs[preset_name][leg_idx]
    inst = leg_input["instrument"]
    info = INSTRUMENTS[inst]
    direction = leg_input["direction"]
    taxa = leg_input["taxa"]

    if info.conv == "price":
        cotacao = f"DOL {taxa:.1f}"
        if direction == "C":
            assert leg["exp"]["ativo"] == cotacao
            assert leg["exp"]["passivo"] == "—"
        else:
            assert leg["exp"]["ativo"] == "—"
            assert leg["exp"]["passivo"] == cotacao
        return

    rs = f"{taxa:.3f}%"
    if info.type == "tpf":
        val = f"{info.benchmark} {rs}"
        if direction == "C":
            assert leg["exp"]["ativo"] == val
            assert leg["exp"]["passivo"] == "—"
        else:
            assert leg["exp"]["ativo"] == "—"
            assert leg["exp"]["passivo"] == val
        return

    if info.type == "cupom":
        val = f"{info.benchmark} {rs}"
        if direction == "C":
            assert leg["exp"]["ativo"] == "CDI"
            assert leg["exp"]["passivo"] == val
        else:
            assert leg["exp"]["ativo"] == val
            assert leg["exp"]["passivo"] == "CDI"
        return

    # DI1 ou DAP — ambos com swap equivalente: ativo CDI, passivo {Pre|IPCA+}
    pay_bm = "IPCA+" if inst == "DAP" else "Pre"
    rec_bm = "CDI"  # DI1: CDI; DAP: CDI/DI Over (swap equivalente livro B3)
    val = f"{pay_bm} {rs}"
    if direction == "C":
        assert leg["exp"]["ativo"] == rec_bm
        assert leg["exp"]["passivo"] == val
    else:
        assert leg["exp"]["ativo"] == val
        assert leg["exp"]["passivo"] == rec_bm


# ----------------------------------------------------------------------------
# Cashflows / KRD (apenas NTN-F e NTN-B)
# ----------------------------------------------------------------------------

COUPON_LEGS = [
    (name, i, leg)
    for (name, i, leg) in ALL_LEGS
    if leg["instrument"] in ("NTN-F", "NTN-B")
]
COUPON_LEG_IDS = _ids(COUPON_LEGS)


@pytest.mark.parametrize("preset_name,leg_idx,leg_input", COUPON_LEGS, ids=COUPON_LEG_IDS)
def test_cashflows_count_and_dus(preset_name, leg_idx, leg_input, all_processed_legs):
    """Numero de fluxos e DUs batem com oracle."""
    leg = all_processed_legs[preset_name][leg_idx]
    cf = leg["cashflows"]
    assert cf is not None
    flows = cf["flows"]

    inst = leg_input["instrument"]
    _, _, venc = _expected_du_dc(inst, leg_input["ticker"])
    if inst == "NTN-F":
        expected_flows = oracle.coupon_flows_ntnf(LIQ_DATE, venc)
    else:
        expected_flows = oracle.coupon_flows_ntnb(LIQ_DATE, venc)

    assert len(flows) == len(expected_flows), \
        f"flows count mismatch: lib={len(flows)} oracle={len(expected_flows)}"

    for got, expected in zip(flows, expected_flows):
        exp_cd, exp_du, _ = expected
        assert got["du"] == exp_du
        if exp_cd:
            # lib retorna como string DD/MM/YYYY (ja serializado em _cashflow_breakdown)
            assert got["payment_date"] == exp_cd.strftime("%d/%m/%Y")


@pytest.mark.parametrize("preset_name,leg_idx,leg_input", COUPON_LEGS, ids=COUPON_LEG_IDS)
def test_cashflows_pv_peso_krd(preset_name, leg_idx, leg_input, all_processed_legs):
    """PV, peso e KRD por fluxo batem com oracle. Soma KRD = D_mac."""
    leg = all_processed_legs[preset_name][leg_idx]
    cf = leg["cashflows"]
    flows = cf["flows"]

    inst = leg_input["instrument"]
    _, _, venc = _expected_du_dc(inst, leg_input["ticker"])
    info = INSTRUMENTS[inst]
    taxa = leg_input["taxa"]  # taxa BRUTA, igual lib/simulator

    if inst == "NTN-F":
        expected_flows = oracle.coupon_flows_ntnf(LIQ_DATE, venc)
    else:
        expected_flows = oracle.coupon_flows_ntnb(LIQ_DATE, venc)

    expected_krd = oracle.krd_flows(taxa, expected_flows)
    vna = leg_input.get("vna")
    vna_scale = (vna / 100.0) if (inst == "NTN-B" and vna and vna > 0) else 1.0

    sum_krd = 0.0
    for got, expected in zip(flows, expected_krd):
        # nominal: para NTN-B, lib aplica vna_scale; para NTN-F, e R$ direto
        expected_nominal = expected["nominal"] * vna_scale
        expected_pv = expected["pv"] * vna_scale
        assert got["nominal"] == pytest.approx(expected_nominal, rel=1e-9)
        assert got["pv"] == pytest.approx(expected_pv, rel=1e-9)
        assert got["peso"] == pytest.approx(expected["peso"], rel=1e-9)
        assert got["krd"] == pytest.approx(expected["krd"], rel=1e-9)
        sum_krd += got["krd"]

    # Soma de KRD = D_macaulay
    assert sum_krd == pytest.approx(leg["d_mac"], abs=TOL_DURATION)
    assert cf["duration_macaulay"] == pytest.approx(leg["d_mac"], abs=TOL_DURATION)
