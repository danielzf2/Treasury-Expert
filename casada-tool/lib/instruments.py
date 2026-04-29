"""Precificacao, Duration, DV01 e Key-Rate Duration para instrumentos do mercado brasileiro."""

from __future__ import annotations
import math
from dataclasses import dataclass
from datetime import date


# ---------------------------------------------------------------------------
# Definicoes de instrumentos
# ---------------------------------------------------------------------------

@dataclass
class InstrumentInfo:
    type: str       # 'tpf', 'deriv', 'fx', 'cupom'
    face: float
    cup_sem: float  # cupom semestral (decimal). 0 = zero-coupon
    conv: str       # 'exp252', 'lin360', 'price'
    benchmark: str
    mult: int = 0   # multiplicador (DOL=50)


INSTRUMENTS: dict[str, InstrumentInfo] = {
    "LTN":   InstrumentInfo("tpf",   1_000,   0,          "exp252", "Pre"),
    "NTN-F": InstrumentInfo("tpf",   1_000,   0.04880885, "exp252", "Pre"),
    "NTN-B": InstrumentInfo("tpf",   1_000,   0.02956301, "exp252", "IPCA+"),
    "LFT":   InstrumentInfo("tpf",   1_000,   0,          "exp252", "Selic+"),
    "DI1":   InstrumentInfo("deriv", 100_000,  0,          "exp252", "CDI"),
    "DAP":   InstrumentInfo("deriv", 100_000,  0,          "exp252", "IPCA"),
    "DOL":   InstrumentInfo("fx",    50_000,   0,          "price",  "USD/BRL", mult=50),
    "DDI":   InstrumentInfo("cupom", 100_000,  0,          "lin360", "CupSujo"),
    "FRC":   InstrumentInfo("cupom", 50_000,   0,          "lin360", "CupLimpo"),
}


# ---------------------------------------------------------------------------
# PU (Preco Unitario)
# ---------------------------------------------------------------------------

def _add_months(d: date, months: int) -> date:
    month = d.month - 1 + months
    year = d.year + month // 12
    month = month % 12 + 1
    return date(year, month, d.day)


def _coupon_cashflows(instrumento: str, liq_date: date | None,
                      venc_date: date | None, du_fallback: int) -> list[tuple[date | None, int, float]]:
    """Retorna fluxos semestrais em DU reais, alinhados ao vencimento."""
    info = INSTRUMENTS[instrumento]
    face_calc = 100 if instrumento == "NTN-B" else info.face

    if not liq_date or not venc_date:
        n_sem = max(1, math.ceil(du_fallback / 126))
        return [
            (
                None,
                round(du_fallback - (n_sem - j) * 126),
                face_calc * (1 + info.cup_sem) if j == n_sem else face_calc * info.cup_sem,
            )
            for j in range(1, n_sem + 1)
            if round(du_fallback - (n_sem - j) * 126) > 0
        ]

    from .calendar import du_entre

    coupon_dates: list[date] = []
    d = venc_date
    while d > liq_date:
        coupon_dates.append(d)
        d = _add_months(d, -6)
    coupon_dates.sort()

    flows: list[tuple[date | None, int, float]] = []
    for d in coupon_dates:
        dui = du_entre(liq_date, d)
        if dui <= 0:
            continue
        flow = face_calc * (1 + info.cup_sem) if d == venc_date else face_calc * info.cup_sem
        flows.append((d, dui, flow))
    return flows


def pu(instrumento: str, taxa: float, du: int, dc: int = 0,
       liq_date: date | None = None, venc_date: date | None = None) -> float:
    """Calcula o PU de qualquer instrumento.

    Args:
        instrumento: nome do instrumento (LTN, NTN-F, DI1, DOL, etc.)
        taxa: taxa em % a.a. (ou cotacao em R$/1000USD para DOL)
        du: dias uteis ate o vencimento
        dc: dias corridos ate o vencimento (usado para lin360)

    Formulas:
        LTN/DI1/DAP/LFT:  PU = Face / (1 + taxa/100)^(du/252)
        NTN-F:             PU = Sum[Cup_sem * VN / (1+TIR)^(dui/252)] + VN/(1+TIR)^(dun/252)
                           Cup_sem = (1.10)^0.5 - 1 = 4.880885%
        NTN-B:             Cotacao(%) = Sum[Cup% / (1+TIR)^(dui/252)] + 100/(1+TIR)^(dun/252)
                           Cup_sem = (1.06)^0.5 - 1 = 2.956301%
        DDI:               PU = 100000 / (1 + taxa/100 * DC/360)
        FRC:               PU = 50000 / (1 + taxa/100 * DC/360)
        DOL:               PU = cotacao (preco direto, sem calculo)
    """
    info = INSTRUMENTS[instrumento]
    r = taxa / 100

    if info.conv == "price":
        return taxa

    if info.conv == "lin360":
        return info.face / (1 + r * dc / 360)

    if info.cup_sem == 0:
        return info.face / (1 + r) ** (du / 252)

    total = 0.0
    for _, dui, flow in _coupon_cashflows(instrumento, liq_date, venc_date, du):
        total += flow / (1 + r) ** (dui / 252)
    return total


# ---------------------------------------------------------------------------
# Duration
# ---------------------------------------------------------------------------

@dataclass
class DurationResult:
    macaulay: float   # em anos
    modificada: float # em anos


def duration(instrumento: str, taxa: float, du: int, dc: int = 0,
             liq_date: date | None = None, venc_date: date | None = None) -> DurationResult:
    """Duration de Macaulay e Modificada.

    Formulas:
        Zero-coupon exp252:  D_mac = du/252,  D_mod = D_mac / (1+taxa)
        Linear 360 (DDI/FRC):  D_mac = dc/360,  D_mod = D_mac / (1+taxa*dc/360)
        Com cupom (NTN-F/NTN-B):
            D_mac = Sum(t_i * PV_i) / Sum(PV_i)
            D_mod = D_mac / (1+taxa)
        DOL: D_mac = D_mod = 0 (instrumento de preco)
    """
    info = INSTRUMENTS[instrumento]
    r = taxa / 100

    if info.conv == "price":
        return DurationResult(0, 0)

    if info.conv == "lin360":
        mac = dc / 360
        return DurationResult(mac, mac / (1 + r * dc / 360))

    if info.cup_sem == 0:
        mac = du / 252
        return DurationResult(mac, mac / (1 + r))

    sum_pv = 0.0
    sum_t_pv = 0.0
    for _, dui, flow in _coupon_cashflows(instrumento, liq_date, venc_date, du):
        t = dui / 252
        pv_i = flow / (1 + r) ** t
        sum_pv += pv_i
        sum_t_pv += t * pv_i

    mac = sum_t_pv / sum_pv if sum_pv else 0
    return DurationResult(mac, mac / (1 + r))


# ---------------------------------------------------------------------------
# DV01
# ---------------------------------------------------------------------------

@dataclass
class DV01Result:
    unit: float   # R$ por bp por unidade
    total: float  # R$ por bp total


def dv01(instrumento: str, taxa: float, du: int, dc: int, quantidade: int,
         liq_date: date | None = None, venc_date: date | None = None) -> DV01Result:
    """DV01 — variacao de valor para 1 bp na taxa.

    Formula:
        DV01 = D_mod * PU_mercado * 0.0001

    Para DOL: sensibilidade = multiplicador (R$ 50/ponto/contrato).
    """
    info = INSTRUMENTS[instrumento]

    if info.conv == "price":
        return DV01Result(info.mult, info.mult * quantidade)

    dur = duration(instrumento, taxa, du, dc, liq_date, venc_date)
    pu_mkt = pu(instrumento, taxa, du, dc, liq_date, venc_date)

    unit = dur.modificada * pu_mkt * 0.0001
    return DV01Result(unit, unit * quantidade)


# ---------------------------------------------------------------------------
# Key-Rate Duration (para titulos com cupom)
# ---------------------------------------------------------------------------

@dataclass
class KRDFlow:
    label: str
    payment_date: date | None
    du: int
    t_anos: float
    nominal: float
    pv: float
    peso: float    # % do VP total
    krd: float     # contribuicao para duration


def key_rate_duration(instrumento: str, taxa: float, du: int,
                      liq_date: date | None = None,
                      venc_date: date | None = None) -> list[KRDFlow]:
    """Decomposicao da duration por fluxo de caixa (Key-Rate Duration).

    Mostra quanto cada cupom/principal contribui para a duration total.
    Util para NTN-F e NTN-B que tem fluxos intermediarios.

    Formula por fluxo i:
        peso_i = PV_i / Sum(PV)
        KRD_i = t_i * peso_i
        Sum(KRD_i) = D_macaulay
    """
    info = INSTRUMENTS[instrumento]
    if info.cup_sem == 0:
        return []

    r = taxa / 100
    flows: list[KRDFlow] = []
    total_pv = 0.0
    coupon_flows = _coupon_cashflows(instrumento, liq_date, venc_date, du)
    for j, (payment_date, dui, nominal) in enumerate(coupon_flows, start=1):
        t = dui / 252
        pv_i = nominal / (1 + r) ** t
        label = "Principal+Cupom" if j == len(coupon_flows) else f"Cupom {j}"
        total_pv += pv_i
        flows.append(KRDFlow(label, payment_date, dui, t, nominal, pv_i, 0, 0))

    for f in flows:
        f.peso = f.pv / total_pv if total_pv else 0
        f.krd = f.t_anos * f.peso

    return flows


# ---------------------------------------------------------------------------
# Cupom Cambial Implicito
# ---------------------------------------------------------------------------

def cupom_cambial_implicito(spot: float, dol_futuro: float, taxa_di: float,
                             du: int, dc: int) -> float:
    """Cupom cambial implicito pela paridade coberta de juros.

    Formula:
        cupom = [(Spot*1000/DOL) * (1+DI)^(DU/252) - 1] * 360/DC * 100

    Args:
        spot: dolar spot em R$/USD (ex: 4.9724)
        dol_futuro: cotacao DOL futuro em R$/1000USD (ex: 4976.5)
        taxa_di: taxa DI em % a.a. (ex: 14.6)
        du: dias uteis
        dc: dias corridos

    Returns:
        cupom em % a.a. linear 360
    """
    spot_pts = spot * 1000
    fator_pre = (1 + taxa_di / 100) ** (du / 252)
    return ((spot_pts / dol_futuro) * fator_pre - 1) * (360 / dc) * 100 if dc else 0
