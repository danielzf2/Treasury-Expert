"""Oracle ANBIMA: wrappers float-puro construidos com helpers de server/tools/*.

Estes wrappers reimplementam exatamente as formulas das tools MCP treasury-docs,
retornando floats ao inves de strings markdown. Servem como source-of-truth
contra o qual casada-tool/lib/* sera comparado.

Convencoes ANBIMA aplicadas:
- LTN: PU = 1000/(1+r)^(du/252), exponencial T-14, PU T-6
- NTN-F: cupom 4.880885% sem (A-6), fluxos descontados A-9, PU T-6
- NTN-B: cupom 2.956301% sem (A-6), cotacao T-4, fluxos A-10, PU = cot/100 * VNA T-6
- LFT: cotacao = 100/(1+rent)^(du/252) T-4, PU = cot/100 * VNA T-6
- DI1/DAP: PU = 100000/(1+r)^(du/252), float puro (sem truncamento)
- DDI/FRC: PU = face / (1 + r * dc/360), linear 360 dc
- DOL: cotacao em pontos (preco direto)
- Cupom cambial: ((spot/futuro) * (1+pre)^(du/252) - 1) * 360/dc * 100
- NDF: spot * (1+pre)^(du/252) / (1 + cupom * dc/360)
- Duration: Σ(t_i * PV_i) / Σ(PV_i), com t_i = du_i/252
- DV01: Dmod * PU * 0.0001
"""

from __future__ import annotations

import math
from datetime import date

from tools.titulos_publicos import (
    _exp_trunc14,
    _generate_coupon_dates,
    _compute_dus,
    _trunc,
    _round,
    _NTNF_CUPOM_AA,
    _NTNB_CUPOM_AA,
)
from tools.dias_uteis import _count_business_days


# ----------------------------------------------------------------------------
# Convencoes basicas
# ----------------------------------------------------------------------------

VN_TPF = 1000.0
VF_DERIV = 100_000.0
FACE_FRC = 50_000.0
DOL_MULT = 50  # R$ por ponto (DOL = 50_000 USD => 50 R$/ponto)


def du_anbima(liq: date, venc: date) -> int:
    """DU ANBIMA: liq inclusive, venc exclusive. Usa server/tools/dias_uteis."""
    return _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)


# ----------------------------------------------------------------------------
# Titulos publicos (ANBIMA: com truncamentos oficiais)
# ----------------------------------------------------------------------------

def pu_ltn_anbima(taxa_aa: float, du: int) -> float:
    """PU LTN ANBIMA: PU = VN / (1+r)^(du/252), T-14 no fator, T-6 no PU."""
    r = taxa_aa / 100.0
    fator = _exp_trunc14(1.0 + r, du / 252.0)
    return _trunc(VN_TPF / fator, 6)


def pu_ltn_float(taxa_aa: float, du: int) -> float:
    """PU LTN float-puro (mesma formula, sem truncamento). Compativel com lib/instruments.pu."""
    r = taxa_aa / 100.0
    return VN_TPF / (1.0 + r) ** (du / 252.0)


def cupom_ntnf_sem() -> float:
    """Cupom NTN-F semestral em decimal: (1.10)^0.5 - 1, A-6."""
    raw = (1.0 + _NTNF_CUPOM_AA / 100.0) ** 0.5 - 1.0
    return _round(raw * 100, 6) / 100.0


def cupom_ntnb_sem() -> float:
    """Cupom NTN-B semestral em decimal: (1.06)^0.5 - 1, A-6."""
    raw = (1.0 + _NTNB_CUPOM_AA / 100.0) ** (6.0 / 12.0) - 1.0
    return _round(raw * 100, 6) / 100.0


def coupon_flows_ntnf(liq: date, venc: date) -> list[tuple[date, int, float]]:
    """Fluxos NTN-F: (data_pagamento, du, nominal). Cupom + principal no ultimo."""
    coupon_dates = _generate_coupon_dates(liq, venc)
    dus = _compute_dus(liq, coupon_dates)
    cupom_sem = cupom_ntnf_sem()
    last = dus[-1] if dus else 0
    out: list[tuple[date, int, float]] = []
    for du, cd in zip(dus, coupon_dates):
        if du == last:
            out.append((cd, du, VN_TPF * cupom_sem + VN_TPF))
        else:
            out.append((cd, du, VN_TPF * cupom_sem))
    return out


def coupon_flows_ntnb(liq: date, venc: date) -> list[tuple[date, int, float]]:
    """Fluxos NTN-B em % do VNA (face=100). Cupom + 100 no ultimo."""
    coupon_dates = _generate_coupon_dates(liq, venc)
    dus = _compute_dus(liq, coupon_dates)
    cupom_sem_pct = cupom_ntnb_sem() * 100
    last = dus[-1] if dus else 0
    out: list[tuple[date, int, float]] = []
    for du, cd in zip(dus, coupon_dates):
        if du == last:
            out.append((cd, du, cupom_sem_pct + 100.0))
        else:
            out.append((cd, du, cupom_sem_pct))
    return out


def pu_ntnf_anbima(taxa_aa: float, liq: date, venc: date) -> float:
    """PU NTN-F ANBIMA: fluxos descontados A-9, PU T-6."""
    r = taxa_aa / 100.0
    total = 0.0
    for _, du, nominal in coupon_flows_ntnf(liq, venc):
        fator = _exp_trunc14(1.0 + r, du / 252.0)
        total += _round(nominal / fator, 9)
    return _trunc(total, 6)


def pu_ntnf_float(taxa_aa: float, liq: date, venc: date) -> float:
    """PU NTN-F float-puro, compativel com lib/instruments.pu."""
    r = taxa_aa / 100.0
    total = 0.0
    cupom_sem = cupom_ntnf_sem()
    coupon_dates = _generate_coupon_dates(liq, venc)
    dus = _compute_dus(liq, coupon_dates)
    last = dus[-1]
    for du in dus:
        nominal = VN_TPF * cupom_sem + VN_TPF if du == last else VN_TPF * cupom_sem
        total += nominal / (1.0 + r) ** (du / 252.0)
    return total


def cotacao_ntnb_anbima(taxa_real_aa: float, liq: date, venc: date) -> float:
    """Cotacao NTN-B em % do VNA: fluxos descontados A-10, cotacao T-4."""
    r = taxa_real_aa / 100.0
    total_pct = 0.0
    for _, du, fluxo_pct in coupon_flows_ntnb(liq, venc):
        fator = _exp_trunc14(1.0 + r, du / 252.0)
        total_pct += _round(fluxo_pct / fator, 10)
    return _trunc(total_pct, 4)


def pu_ntnb_anbima(taxa_real_aa: float, vna: float, liq: date, venc: date) -> float:
    """PU NTN-B ANBIMA: cotacao(%)/100 * VNA(T-6), PU T-6."""
    cot = cotacao_ntnb_anbima(taxa_real_aa, liq, venc)
    vna_t6 = _trunc(vna, 6)
    return _trunc((cot / 100.0) * vna_t6, 6)


def pu_ntnb_float(taxa_real_aa: float, vna: float, liq: date, venc: date) -> float:
    """PU NTN-B float-puro: lib/instruments.pu retorna cotacao*vna/100 (sem truncamento)."""
    r = taxa_real_aa / 100.0
    total_pct = 0.0
    cupom_sem_pct = cupom_ntnb_sem() * 100
    coupon_dates = _generate_coupon_dates(liq, venc)
    dus = _compute_dus(liq, coupon_dates)
    last = dus[-1]
    for du in dus:
        fluxo_pct = cupom_sem_pct + 100.0 if du == last else cupom_sem_pct
        total_pct += fluxo_pct / (1.0 + r) ** (du / 252.0)
    return (total_pct / 100.0) * vna


def pu_lft_anbima(rentabilidade_aa_pct: float, vna: float, du: int) -> float:
    """PU LFT ANBIMA: cot = 100/(1+r)^(du/252) T-4, PU = cot/100 * VNA T-6."""
    r = rentabilidade_aa_pct / 100.0
    fator = _exp_trunc14(1.0 + r, du / 252.0)
    cot = _trunc(100.0 / fator, 4)
    vna_t6 = _trunc(vna, 6)
    return _trunc((cot / 100.0) * vna_t6, 6)


# ----------------------------------------------------------------------------
# Derivativos exp 252 (DI1, DAP)
# ----------------------------------------------------------------------------

def pu_di1(taxa_aa: float, du: int) -> float:
    """PU DI1: VF=100k, base 252, exponencial. Float puro."""
    if du <= 0:
        return VF_DERIV
    return VF_DERIV / (1.0 + taxa_aa / 100.0) ** (du / 252.0)


def pu_dap(taxa_aa: float, du: int) -> float:
    """PU DAP: idem DI1 mas para taxa real (cupom IPCA implicito)."""
    if du <= 0:
        return VF_DERIV
    return VF_DERIV / (1.0 + taxa_aa / 100.0) ** (du / 252.0)


# ----------------------------------------------------------------------------
# Derivativos lin 360 (DDI, FRC)
# ----------------------------------------------------------------------------

def pu_ddi(taxa_aa: float, dc: int) -> float:
    """PU DDI: face 100k, linear 360 dc."""
    if dc <= 0:
        return VF_DERIV
    return VF_DERIV / (1.0 + (taxa_aa / 100.0) * dc / 360.0)


def pu_frc(taxa_aa: float, dc: int) -> float:
    """PU FRC: face 50k, linear 360 dc."""
    if dc <= 0:
        return FACE_FRC
    return FACE_FRC / (1.0 + (taxa_aa / 100.0) * dc / 360.0)


# ----------------------------------------------------------------------------
# DOL (preco direto)
# ----------------------------------------------------------------------------

def pu_dol(cotacao_pontos: float) -> float:
    """DOL: cotacao em pontos = R$/1000USD. PU = cotacao."""
    return cotacao_pontos


# ----------------------------------------------------------------------------
# Cambio: cupom cambial implicito, NDF
# ----------------------------------------------------------------------------

def cupom_cambial_implicito(spot: float, dol_futuro: float, taxa_di_aa: float,
                             du: int, dc: int) -> float:
    """Cupom cambial implicito % a.a. lin360.

    Formula: ((spot * 1000 / DOL) * (1+DI/100)^(du/252) - 1) * 360/dc * 100
    """
    if dc <= 0 or dol_futuro <= 0:
        return 0.0
    spot_pts = spot * 1000
    fator_pre = (1.0 + taxa_di_aa / 100.0) ** (du / 252.0)
    return ((spot_pts / dol_futuro) * fator_pre - 1.0) * (360.0 / dc) * 100.0


def ndf_teorico(spot: float, taxa_pre_aa: float, cupom_aa: float,
                du: int, dc: int) -> float:
    """NDF teorico via paridade coberta:
    NDF = spot * (1+pre)^(du/252) / (1 + cupom * dc/360)
    """
    num = spot * (1.0 + taxa_pre_aa / 100.0) ** (du / 252.0)
    den = 1.0 + (cupom_aa / 100.0) * (dc / 360.0)
    return num / den if den != 0 else 0.0


def dol_sintetico_fwd_di_frc(spot: float, taxa_di_aa: float, taxa_frc_aa: float,
                              du: int, dc: int) -> float:
    """Dolar forward sintetico de DI1+FRC: spot * (1+pre)^(du/252) / (1 + cupom*dc/360)."""
    return ndf_teorico(spot, taxa_di_aa, taxa_frc_aa, du, dc)


# ----------------------------------------------------------------------------
# Duration / DV01 / KRD
# ----------------------------------------------------------------------------

def duration_zero_coupon(taxa_aa: float, du: int) -> tuple[float, float]:
    """Duration Macaulay e Modificada para zero-coupon exp 252. Retorna (mac, mod) em anos."""
    mac = du / 252.0
    return mac, mac / (1.0 + taxa_aa / 100.0)


def duration_lin360(taxa_aa: float, dc: int) -> tuple[float, float]:
    """Duration para DDI/FRC (linear 360)."""
    mac = dc / 360.0
    r = taxa_aa / 100.0
    return mac, mac / (1.0 + r * dc / 360.0)


def duration_with_coupons(taxa_aa: float, flows: list[tuple[date, int, float]]) -> tuple[float, float]:
    """Duration de titulo com cupom: D_mac = Σ(t*PV)/Σ(PV) em anos."""
    r = taxa_aa / 100.0
    sum_pv = 0.0
    sum_t_pv = 0.0
    for _, du, nominal in flows:
        t = du / 252.0
        pv_i = nominal / (1.0 + r) ** t
        sum_pv += pv_i
        sum_t_pv += t * pv_i
    if sum_pv <= 0:
        return 0.0, 0.0
    mac = sum_t_pv / sum_pv
    return mac, mac / (1.0 + r)


def dv01_unit(d_mod: float, pu_mkt: float) -> float:
    """DV01 = Dmod * PU * 0.0001 (R$ por bp por unidade)."""
    return d_mod * pu_mkt * 0.0001


def dv01_dol_unit() -> float:
    """DV01 do DOL: multiplicador R$ 50 por ponto (sensibilidade direta de preco)."""
    return float(DOL_MULT)


def krd_flows(taxa_aa: float, flows: list[tuple[date, int, float]]) -> list[dict]:
    """KRD por fluxo: peso_i = PV_i/PV_total, krd_i = t_i * peso_i.

    Retorna lista de dicts com du, t_anos, nominal, pv, peso, krd.
    Soma de krd_i = D_mac. Soma de peso_i = 1.0.
    """
    r = taxa_aa / 100.0
    rows: list[dict] = []
    total_pv = 0.0
    for cd, du, nominal in flows:
        t = du / 252.0
        pv_i = nominal / (1.0 + r) ** t
        rows.append({
            "payment_date": cd,
            "du": du,
            "t_anos": t,
            "nominal": nominal,
            "pv": pv_i,
        })
        total_pv += pv_i
    for row in rows:
        row["peso"] = row["pv"] / total_pv if total_pv else 0.0
        row["krd"] = row["t_anos"] * row["peso"]
    return rows


# ----------------------------------------------------------------------------
# Cenarios de curva (formulas explicitas re-derivadas de lib/scenarios.py)
# ----------------------------------------------------------------------------

def t_normalize(du: int, du_min: int, du_max: int) -> float:
    """Normaliza posicao do vertice na curva: t in [-1, +1]."""
    du_mid = (du_min + du_max) / 2
    du_range = (du_max - du_min) / 2 or 1
    return max(-1.0, min(1.0, (du - du_mid) / du_range))


def scenario_delta_bps(du: int, du_min: int, du_max: int,
                       scenario_key: str, magnitude: float,
                       custom_parallel_bps: float = 0.0,
                       custom_slope_bps: float = 0.0,
                       custom_curvature_bps: float = 0.0) -> float:
    """Choque em bps para um vertice especifico no cenario.

    Formulas (mesmas de lib/scenarios.py):
      bull_par:    -mag
      bear_par:    +mag
      bull_steep:  -mag + mag*(t+1)/2
      bear_steep:  +mag*(t+1)/2
      bull_flat:   -mag*(t+1)/2
      bear_flat:   +mag - mag*(t+1)/2
      pos_fly:     mag * (0.5 - 1.5*t^2)
      neg_fly:     mag * (1.5*t^2 - 0.5)
      custom:      (mag/10) * (par + slope*t + curv*(0.5 - 1.5*t^2))
    """
    if du_min == du_max and scenario_key in ("pos_fly", "neg_fly"):
        return 0.0

    t = t_normalize(du, du_min, du_max)
    mag = magnitude

    if scenario_key == "bull_par":
        return -mag
    if scenario_key == "bear_par":
        return mag
    if scenario_key == "bull_steep":
        return -mag + mag * (t + 1) / 2
    if scenario_key == "bear_steep":
        return mag * (t + 1) / 2
    if scenario_key == "bull_flat":
        return -mag * (t + 1) / 2
    if scenario_key == "bear_flat":
        return mag - mag * (t + 1) / 2
    if scenario_key == "pos_fly":
        return mag * (0.5 - 1.5 * t * t)
    if scenario_key == "neg_fly":
        return mag * (1.5 * t * t - 0.5)
    if scenario_key == "custom":
        scale = mag / 10 if mag else 0
        return scale * (custom_parallel_bps
                        + custom_slope_bps * t
                        + custom_curvature_bps * (0.5 - 1.5 * t * t))
    return 0.0


# ----------------------------------------------------------------------------
# P&L per leg (parallel shift via TIR-shift)
# ----------------------------------------------------------------------------

def _pu_for_leg(instrumento: str, taxa: float, du: int, dc: int,
                liq: date | None, venc: date | None,
                vna: float | None) -> float:
    """Calcula PU float-puro de uma perna (compativel com lib/instruments.pu)."""
    if instrumento == "LTN":
        return pu_ltn_float(taxa, du)
    if instrumento == "NTN-F":
        return pu_ntnf_float(taxa, liq, venc)
    if instrumento == "NTN-B":
        return pu_ntnb_float(taxa, vna or 100.0, liq, venc)
    if instrumento == "LFT":
        return pu_ltn_float(taxa, du) * (vna / 1000.0 if vna else 1.0)
    if instrumento in ("DI1", "DAP"):
        return pu_di1(taxa, du)
    if instrumento in ("DDI",):
        return pu_ddi(taxa, dc)
    if instrumento == "FRC":
        return pu_frc(taxa, dc)
    if instrumento == "DOL":
        return pu_dol(taxa)
    raise ValueError(f"Instrumento nao suportado: {instrumento}")


def pnl_per_leg_parallel(leg: dict, delta_bps: float,
                         delta_fx_pct: float = 0.0,
                         delta_ipca_bps: float = 0.0,
                         delta_cupom_bps: float = 0.0) -> float:
    """P&L de uma perna sob choque de TIR (TIR-shift).

    Replicacao explicita de lib/scenarios.calc_leg_pnl:
    - DOL (price): sign * (taxa * delta_fx_pct/100) * mult * qty
    - NTN-B/DAP: usa delta_ipca_bps se != 0, senao delta_bps
    - DDI/FRC: usa delta_cupom_bps se != 0, senao delta_bps
    - Demais: usa delta_bps
    - Sinal: TPF C => +1, TPF V => -1; deriv C => -1, deriv V => +1
    """
    inst = leg["instrument"]
    qty = leg["quantity"]
    direction = leg["direction"]
    taxa = leg["tax_fin"]
    du = leg["du"]
    dc = leg["dc"]
    liq = leg.get("liq")
    venc = leg.get("venc")
    vna = leg.get("vna")

    if inst == "DOL":
        sign = 1 if direction == "C" else -1
        delta_pts = taxa * delta_fx_pct / 100.0
        return sign * delta_pts * DOL_MULT * qty

    effective_delta = delta_bps
    if inst in ("NTN-B", "DAP"):
        effective_delta = delta_bps + delta_ipca_bps
    elif inst in ("DDI", "FRC"):
        effective_delta = delta_bps + delta_cupom_bps

    new_rate = taxa + effective_delta / 100.0
    new_pu = _pu_for_leg(inst, new_rate, du, dc, liq, venc, vna)
    old_pu = _pu_for_leg(inst, taxa, du, dc, liq, venc, vna)

    if inst in ("LTN", "NTN-F", "NTN-B", "LFT"):
        sign = 1 if direction == "C" else -1
    else:
        sign = -1 if direction == "C" else 1

    return sign * (new_pu - old_pu) * qty


def pnl_per_leg_scenario(leg: dict,
                          scenario_key: str, magnitude: float,
                          du_min: int, du_max: int,
                          custom_parallel_bps: float = 0.0,
                          custom_slope_bps: float = 0.0,
                          custom_curvature_bps: float = 0.0,
                          delta_fx_pct: float = 0.0,
                          delta_ipca_bps: float = 0.0,
                          delta_cupom_bps: float = 0.0) -> float:
    """P&L per leg em cenario de curva (TIR-shift no DU da perna)."""
    inst = leg["instrument"]
    if inst == "DOL":
        return pnl_per_leg_parallel(leg, 0, delta_fx_pct=delta_fx_pct)

    delta = scenario_delta_bps(leg["du"], du_min, du_max, scenario_key, magnitude,
                                custom_parallel_bps, custom_slope_bps, custom_curvature_bps)
    return pnl_per_leg_parallel(
        leg, delta,
        delta_fx_pct=delta_fx_pct,
        delta_ipca_bps=delta_ipca_bps,
        delta_cupom_bps=delta_cupom_bps,
    )


# ----------------------------------------------------------------------------
# Curva spot (flat forward exp 252)
# ----------------------------------------------------------------------------

def flat_forward(vertices: list[tuple[int, float]], du_alvo: int) -> float | None:
    """Interpola taxa spot via flat forward (exp 252).

    Igual a lib/curves.flat_forward_interp:
      fwd = (f2/f1)^(252/(du2-du1)) - 1
      f_alvo = f1 * (1+fwd)^((du_alvo-du1)/252)
      r_alvo = f_alvo^(252/du_alvo) - 1
    """
    if not vertices or du_alvo <= 0:
        return None
    verts = sorted(vertices)
    if du_alvo <= verts[0][0]:
        return verts[0][1]
    if du_alvo >= verts[-1][0]:
        return verts[-1][1]
    for j in range(len(verts) - 1):
        du1, r1 = verts[j]
        du2, r2 = verts[j + 1]
        if du1 <= du_alvo <= du2:
            if du1 == du2:
                return r1
            r1d = r1 / 100.0
            r2d = r2 / 100.0
            f1 = (1.0 + r1d) ** (du1 / 252.0)
            f2 = (1.0 + r2d) ** (du2 / 252.0)
            fwd = (f2 / f1) ** (252.0 / (du2 - du1)) - 1.0
            f_alvo = f1 * (1.0 + fwd) ** ((du_alvo - du1) / 252.0)
            return (f_alvo ** (252.0 / du_alvo) - 1.0) * 100.0
    return None


def pnl_per_flow(leg: dict,
                  scenario_key: str, magnitude: float,
                  du_min: int, du_max: int,
                  spot_curve: list[tuple[int, float]],
                  custom_parallel_bps: float = 0.0,
                  custom_slope_bps: float = 0.0,
                  custom_curvature_bps: float = 0.0,
                  delta_ipca_bps: float = 0.0) -> dict | None:
    """Per-cashflow MtM usando curva spot.

    Replica lib/scenarios.calc_leg_pnl_per_flow:
    - i_k = curve(du_k) + spread_credito (constante)
    - delta_k = scenario_delta(du_k) ou delta_ipca_bps se NTN-B
    - pnl_flow_k = sign * (new_pv_k - old_pv_k) * vna_scale * qty
    """
    inst = leg["instrument"]
    if inst not in ("NTN-F", "NTN-B"):
        return None

    use_ipca = inst == "NTN-B"
    base_delta_override = delta_ipca_bps if use_ipca and delta_ipca_bps != 0 else None

    liq = leg.get("liq")
    venc = leg.get("venc")
    vna = leg.get("vna")

    if inst == "NTN-F":
        flows = coupon_flows_ntnf(liq, venc)
        face_calc = 1.0  # nominais ja em R$
    else:
        flows = coupon_flows_ntnb(liq, venc)
        face_calc = 1.0  # nominais em % do VNA

    tir = leg["tax_fin"]
    curve_at_maturity = flat_forward(spot_curve, leg["du"])
    if curve_at_maturity is None:
        return None
    spread = tir - curve_at_maturity

    vna_scale = (vna / 100.0) if (inst == "NTN-B" and vna and vna > 0) else 1.0
    sign = 1 if leg["direction"] == "C" else -1

    rows: list[dict] = []
    old_pu = 0.0
    new_pu = 0.0
    for j, (cd, du_i, nominal) in enumerate(flows, start=1):
        spot_k = flat_forward(spot_curve, du_i)
        if spot_k is None:
            spot_k = curve_at_maturity
        i_k = spot_k + spread

        if base_delta_override is not None:
            delta_k = base_delta_override
        else:
            delta_k = scenario_delta_bps(
                du_i, du_min, du_max, scenario_key, magnitude,
                custom_parallel_bps, custom_slope_bps, custom_curvature_bps,
            )

        t = du_i / 252.0
        old_pv = nominal / (1.0 + i_k / 100.0) ** t
        new_pv = nominal / (1.0 + (i_k + delta_k / 100.0) / 100.0) ** t

        old_pv_brl = old_pv * vna_scale * leg["quantity"]
        new_pv_brl = new_pv * vna_scale * leg["quantity"]
        pnl_flow = sign * (new_pv_brl - old_pv_brl)

        old_pu += old_pv
        new_pu += new_pv

        label = "Principal+Cupom" if j == len(flows) else f"Cupom {j}"
        rows.append({
            "label": label,
            "payment_date": cd,
            "du": du_i,
            "old_pv": old_pv * vna_scale,
            "new_pv": new_pv * vna_scale,
            "delta_bps": delta_k,
            "pnl_flow": pnl_flow,
        })

    leg_pnl = sign * (new_pu - old_pu) * vna_scale * leg["quantity"]

    return {
        "leg_pnl": leg_pnl,
        "old_pu": old_pu * vna_scale,
        "new_pu": new_pu * vna_scale,
        "flows": rows,
        "spread_credito": spread,
    }
