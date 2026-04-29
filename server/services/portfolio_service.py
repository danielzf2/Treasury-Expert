"""
Portfolio risk calculation service.
Prices bonds, computes duration/convexity/DV01, aggregates portfolio-level
metrics, and suggests DI futures hedge.

All computations use 252 business-day convention and ANBIMA truncation rules
consistent with the existing tools in server/tools/.

Inputs (all public functions documented below):
    Bond data dicts with type, rate, dates, notional, etc.

Outputs:
    Structured dicts with per-bond and portfolio-level risk metrics.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import Any

from tools.dias_uteis import _parse_date, _count_business_days, _is_business_day
from tools.titulos_publicos import (
    _trunc, _round, _exp_trunc14, _VN,
    _NTNF_CUPOM_AA, _NTNB_CUPOM_AA,
    _generate_coupon_dates, _compute_dus,
)


# ── Data structures ──────────────────────────────────────────────────────────

@dataclass
class BondInput:
    """
    Inputs for a single bond position.

    id: str — unique identifier for the bond.
    type: str — one of LTN, NTN-F, NTN-B, LFT.
    notional: float — total face value in BRL.
    quantity: int — number of bonds.
    rate: float — purchase rate (% p.a.).
    settlement_date: str — settlement date (DD/MM/YYYY or YYYY-MM-DD).
    maturity_date: str — maturity date (DD/MM/YYYY or YYYY-MM-DD).
    vna: float | None — VNA for NTN-B (truncated 6 decimals).
    premium_bps: float | None — premium/discount in bps for LFT.
    current_rate: float | None — current market rate for MtM (% p.a.).
    """
    id: str
    type: str
    notional: float
    quantity: int
    rate: float
    settlement_date: str
    maturity_date: str
    vna: float | None = None
    premium_bps: float | None = None
    current_rate: float | None = None


@dataclass
class CashFlow:
    du: int
    amount: float
    event: str


@dataclass
class BondRisk:
    """
    Outputs per bond: pricing and risk metrics.
    """
    id: str
    type: str
    pu: float
    market_value: float
    du: int
    duration_macaulay: float
    duration_modified: float
    duration_anbima_du: float
    convexity: float
    dv01: float
    carry_1du: float
    notional: float
    quantity: int
    rate: float
    current_rate: float
    cash_flows: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class PortfolioRisk:
    """
    Outputs for the full portfolio.
    """
    bonds: list[BondRisk]
    total_dv01: float
    total_market_value: float
    weighted_duration_mod: float
    weighted_duration_anbima: float
    weighted_convexity: float
    exposure_by_type: dict[str, float]
    exposure_by_maturity_bucket: dict[str, float]


@dataclass
class HedgeSuggestion:
    """
    Outputs: DI futures hedge recommendation.
    """
    portfolio_dv01: float
    hedge_dv01_per_contract: float
    contracts_needed: int
    contracts_raw: float
    residual_dv01: float
    direction: str
    hedge_maturity_du: int


# ── Bond-level computations ──────────────────────────────────────────────────

def _generate_cash_flows(bond: BondInput) -> list[CashFlow]:
    """
    Generates cash flow schedule for a bond.

    Inputs:
        bond: BondInput — bond specification.

    Outputs:
        list[CashFlow] — list of cash flows with du, amount, and event type.
    """
    liq = _parse_date(bond.settlement_date)
    venc = _parse_date(bond.maturity_date)
    bond_type = bond.type.upper().replace(" ", "-").replace("_", "-")

    if bond_type == "LTN":
        du = _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)
        return [CashFlow(du=du, amount=_VN, event="principal")]

    elif bond_type in ("NTN-F", "NTNF"):
        coupon_dates = _generate_coupon_dates(liq, venc)
        dus = _compute_dus(liq, coupon_dates)
        cupom_sem = _round((1.0 + _NTNF_CUPOM_AA / 100.0) ** 0.5 - 1.0, 8)
        flows = []
        last_du = dus[-1] if dus else 0
        for du in dus:
            if du == last_du:
                flows.append(CashFlow(du=du, amount=_VN * cupom_sem + _VN, event="coupon+principal"))
            else:
                flows.append(CashFlow(du=du, amount=_VN * cupom_sem, event="coupon"))
        return flows

    elif bond_type in ("NTN-B", "NTNB"):
        coupon_dates = _generate_coupon_dates(liq, venc)
        dus = _compute_dus(liq, coupon_dates)
        cupom_sem_pct = _round(((1.0 + _NTNB_CUPOM_AA / 100.0) ** 0.5 - 1.0) * 100, 6)
        cupom_sem = cupom_sem_pct / 100.0
        vna = bond.vna or _VN
        flows = []
        last_du = dus[-1] if dus else 0
        for du in dus:
            if du == last_du:
                flows.append(CashFlow(du=du, amount=vna * (1.0 + cupom_sem), event="coupon+principal"))
            else:
                flows.append(CashFlow(du=du, amount=vna * cupom_sem, event="coupon"))
        return flows

    elif bond_type == "LFT":
        du = _count_business_days(liq, venc, start_inclusive=True, end_inclusive=False)
        vna = bond.vna or _VN
        return [CashFlow(du=du, amount=vna, event="principal")]

    else:
        raise ValueError(f"Unsupported bond type: {bond.type}")


def _price_bond(flows: list[CashFlow], rate_aa: float) -> float:
    """
    PU via discounted cash flows: PU = Σ FC_i / (1 + r)^(du_i / 252).

    Inputs:
        flows: list[CashFlow] — cash flow schedule.
        rate_aa: float — discount rate in % p.a.

    Outputs:
        float — PU (truncated 6 decimals).
    """
    r = rate_aa / 100.0
    pv_total = 0.0
    for cf in flows:
        fator = _exp_trunc14(1.0 + r, cf.du / 252.0)
        pv_total += cf.amount / fator
    return _trunc(pv_total, 6)


def _compute_risk_metrics(
    flows: list[CashFlow], rate_aa: float
) -> dict[str, float]:
    """
    Computes duration (Macaulay, modified, ANBIMA), convexity, and DV01.

    Inputs:
        flows: list[CashFlow] — cash flow schedule.
        rate_aa: float — discount rate in % p.a.

    Outputs:
        dict with keys: duration_macaulay, duration_modified, duration_anbima_du,
                        convexity, pv_total.
    """
    r = rate_aa / 100.0
    if r <= -1:
        raise ValueError("Rate results in non-positive base (1+y).")

    pv_list = []
    t_list = []
    du_list = []

    for cf in flows:
        t = cf.du / 252.0
        pv = cf.amount / math.pow(1.0 + r, t)
        pv_list.append(pv)
        t_list.append(t)
        du_list.append(cf.du)

    pv_total = sum(pv_list)
    if pv_total == 0:
        raise ValueError("Total PV is zero.")

    # Macaulay duration (in years)
    d_mac = sum(t * pv for t, pv in zip(t_list, pv_list)) / pv_total

    # Modified duration
    d_mod = d_mac / (1.0 + r)

    # ANBIMA duration (in business days)
    d_anbima = sum(du * pv for du, pv in zip(du_list, pv_list)) / pv_total

    # Convexity
    inv252 = 1.0 / 252.0
    numer = sum(t * (t + inv252) * pv for t, pv in zip(t_list, pv_list))
    convex = numer / (pv_total * (1.0 + r) ** 2)

    return {
        "duration_macaulay": d_mac,
        "duration_modified": d_mod,
        "duration_anbima_du": d_anbima,
        "convexity": convex,
        "pv_total": pv_total,
    }


def _solve_rate_from_pu(flows: list[CashFlow], target_pu: float) -> float:
    """
    Bisection method: finds rate (% a.a.) such that _price_bond(flows, rate) ≈ target_pu.
    PU is monotonically decreasing in rate, so we can use simple bisection.
    """
    lo, hi = -5.0, 200.0
    for _ in range(300):
        mid = (lo + hi) / 2.0
        pu_mid = _price_bond(flows, mid)
        if abs(pu_mid - target_pu) < 1e-8:
            return round(mid, 6)
        if pu_mid > target_pu:
            lo = mid
        else:
            hi = mid
    return round((lo + hi) / 2.0, 6)


def enrich_bond(
    bond_type: str,
    settlement_date: str,
    maturity_date: str,
    quantity: int,
    input_mode: str,
    rate: float | None = None,
    pu_input: float | None = None,
    vna: float | None = None,
    mtm_settlement_date: str | None = None,
    mtm_rate: float | None = None,
) -> dict[str, Any]:
    """
    Computes purchase values (PU/rate) and MtM values (current PU, DV01, duration).
    Purchase uses the original settlement_date; MtM uses today + ANBIMA indicative rate.
    """
    # ── Purchase ──────────────────────────────────────────────────────────
    purchase_bond = BondInput(
        id="purchase", type=bond_type, notional=0, quantity=quantity,
        rate=rate or 0.0, settlement_date=settlement_date,
        maturity_date=maturity_date, vna=vna,
    )
    purchase_flows = _generate_cash_flows(purchase_bond)

    if input_mode == "pu" and pu_input is not None:
        purchase_rate = _solve_rate_from_pu(purchase_flows, pu_input)
        purchase_pu = pu_input
    elif input_mode == "taxa" and rate is not None:
        purchase_pu = _price_bond(purchase_flows, rate)
        purchase_rate = rate
    else:
        raise ValueError("Provide rate (mode=taxa) or pu (mode=pu).")

    # ── MtM ───────────────────────────────────────────────────────────────
    if mtm_settlement_date and mtm_rate is not None:
        mtm_bond = BondInput(
            id="mtm", type=bond_type, notional=0, quantity=quantity,
            rate=mtm_rate, settlement_date=mtm_settlement_date,
            maturity_date=maturity_date, vna=vna,
        )
        mtm_flows = _generate_cash_flows(mtm_bond)
        mtm_pu = _price_bond(mtm_flows, mtm_rate)
        mtm_metrics = _compute_risk_metrics(mtm_flows, mtm_rate)
        mtm_rate_out = mtm_rate
    else:
        mtm_flows = purchase_flows
        mtm_pu = purchase_pu
        mtm_metrics = _compute_risk_metrics(purchase_flows, purchase_rate)
        mtm_rate_out = purchase_rate

    mtm_mv = mtm_pu * quantity
    mtm_dv01 = mtm_metrics["duration_modified"] * mtm_mv * 0.0001
    du = max(cf.du for cf in mtm_flows) if mtm_flows else 0

    return {
        "purchase_rate": round(purchase_rate, 6),
        "purchase_pu": round(purchase_pu, 6),
        "pu": round(mtm_pu, 6),
        "rate": round(mtm_rate_out, 6),
        "dv01": round(mtm_dv01, 2),
        "duration_modified": round(mtm_metrics["duration_modified"], 6),
        "duration_anbima_du": round(mtm_metrics["duration_anbima_du"], 2),
        "duration_macaulay": round(mtm_metrics["duration_macaulay"], 6),
        "convexity": round(mtm_metrics["convexity"], 6),
        "market_value": round(mtm_mv, 2),
        "du": du,
        "notional": round(mtm_mv, 2),
        "vna_used": vna,
    }


def compute_bond_risk(bond: BondInput) -> BondRisk:
    """
    Full risk analysis for a single bond position.

    Inputs:
        bond: BondInput — bond specification with position data.

    Outputs:
        BondRisk — pricing and risk metrics for the bond.
    """
    flows = _generate_cash_flows(bond)
    rate = bond.current_rate if bond.current_rate is not None else bond.rate
    pu = _price_bond(flows, rate)
    market_value = pu * bond.quantity

    metrics = _compute_risk_metrics(flows, rate)
    dv01_val = metrics["duration_modified"] * market_value * 0.0001

    du_total = max(cf.du for cf in flows) if flows else 0

    # Carry (1 du)
    r = rate / 100.0
    pu_d0 = pu
    if du_total > 0 and r > -1:
        pu_d1 = _trunc(metrics["pv_total"] * math.pow(1.0 + r, 1.0 / 252.0), 6)
        carry = (pu_d1 - pu_d0)
    else:
        carry = 0.0

    cf_dicts = [{"du": cf.du, "amount": round(cf.amount, 6), "event": cf.event} for cf in flows]

    return BondRisk(
        id=bond.id,
        type=bond.type.upper(),
        pu=pu,
        market_value=round(market_value, 2),
        du=du_total,
        duration_macaulay=round(metrics["duration_macaulay"], 6),
        duration_modified=round(metrics["duration_modified"], 6),
        duration_anbima_du=round(metrics["duration_anbima_du"], 2),
        convexity=round(metrics["convexity"], 6),
        dv01=round(dv01_val, 2),
        carry_1du=round(carry * bond.quantity, 2),
        notional=bond.notional,
        quantity=bond.quantity,
        rate=bond.rate,
        current_rate=rate,
        cash_flows=cf_dicts,
    )


# ── Portfolio-level computations ─────────────────────────────────────────────

def _maturity_bucket(du: int) -> str:
    if du <= 63:
        return "0-3M"
    elif du <= 126:
        return "3-6M"
    elif du <= 252:
        return "6-12M"
    elif du <= 504:
        return "1-2Y"
    elif du <= 1260:
        return "2-5Y"
    elif du <= 2520:
        return "5-10Y"
    else:
        return "10Y+"


def compute_portfolio_risk(bonds: list[BondInput]) -> PortfolioRisk:
    """
    Aggregated risk analysis for a portfolio of bonds.

    Inputs:
        bonds: list[BondInput] — list of bond specifications.

    Outputs:
        PortfolioRisk — per-bond risks and portfolio-level aggregates.
    """
    bond_risks = [compute_bond_risk(b) for b in bonds]

    total_mv = sum(br.market_value for br in bond_risks)
    total_dv01 = sum(br.dv01 for br in bond_risks)

    if total_mv > 0:
        w_dmod = sum(br.duration_modified * br.market_value for br in bond_risks) / total_mv
        w_danbima = sum(br.duration_anbima_du * br.market_value for br in bond_risks) / total_mv
        w_conv = sum(br.convexity * br.market_value for br in bond_risks) / total_mv
    else:
        w_dmod = w_danbima = w_conv = 0.0

    by_type: dict[str, float] = {}
    by_bucket: dict[str, float] = {}
    for br in bond_risks:
        by_type[br.type] = by_type.get(br.type, 0.0) + br.market_value
        bucket = _maturity_bucket(br.du)
        by_bucket[bucket] = by_bucket.get(bucket, 0.0) + br.market_value

    return PortfolioRisk(
        bonds=bond_risks,
        total_dv01=round(total_dv01, 2),
        total_market_value=round(total_mv, 2),
        weighted_duration_mod=round(w_dmod, 6),
        weighted_duration_anbima=round(w_danbima, 2),
        weighted_convexity=round(w_conv, 6),
        exposure_by_type=by_type,
        exposure_by_maturity_bucket=by_bucket,
    )


def compute_hedge(
    bonds: list[BondInput],
    hedge_rate_aa: float,
    hedge_du: int,
    contract_face: float = 100_000.0,
) -> HedgeSuggestion:
    """
    Suggests number of DI futures contracts to hedge portfolio DV01.

    Inputs:
        bonds: list[BondInput] — portfolio bonds.
        hedge_rate_aa: float — DI futures implied rate (% p.a.) for the hedge vertex.
        hedge_du: int — business days to maturity of the DI futures contract.
        contract_face: float — face value per contract (default 100,000 for DI1).

    Outputs:
        HedgeSuggestion — contracts needed, direction, residual DV01.
    """
    portfolio = compute_portfolio_risk(bonds)

    r = hedge_rate_aa / 100.0
    pu_contract = contract_face / math.pow(1.0 + r, hedge_du / 252.0)
    t = hedge_du / 252.0
    d_mod_contract = t / (1.0 + r)
    dv01_contract = d_mod_contract * pu_contract * 0.0001

    if dv01_contract == 0:
        raise ValueError("DV01 per contract is zero — check hedge rate and DU.")

    q_raw = portfolio.total_dv01 / dv01_contract
    q = int(round(q_raw))

    residual = portfolio.total_dv01 - q * dv01_contract
    direction = "sell (vender taxa / comprar PU)" if q > 0 else "buy (comprar taxa / vender PU)"

    return HedgeSuggestion(
        portfolio_dv01=round(portfolio.total_dv01, 2),
        hedge_dv01_per_contract=round(dv01_contract, 6),
        contracts_needed=abs(q),
        contracts_raw=round(q_raw, 4),
        residual_dv01=round(residual, 2),
        direction=direction,
        hedge_maturity_du=hedge_du,
    )


def simulate_scenario(
    bonds: list[BondInput],
    shock_bps: float,
) -> dict[str, Any]:
    """
    Simulates a parallel rate shock and estimates portfolio P&L.

    Inputs:
        bonds: list[BondInput] — portfolio bonds.
        shock_bps: float — parallel shift in basis points (positive = rates up).

    Outputs:
        dict with per-bond and portfolio-level P&L estimates.
    """
    portfolio = compute_portfolio_risk(bonds)
    dy = shock_bps / 10_000.0

    bond_pnl = []
    total_pnl_1st = 0.0
    total_pnl_2nd = 0.0

    for br in portfolio.bonds:
        pnl_1st = -br.duration_modified * dy * br.market_value
        pnl_2nd = pnl_1st + 0.5 * br.convexity * (dy ** 2) * br.market_value
        total_pnl_1st += pnl_1st
        total_pnl_2nd += pnl_2nd
        bond_pnl.append({
            "id": br.id,
            "type": br.type,
            "market_value": br.market_value,
            "pnl_1st_order": round(pnl_1st, 2),
            "pnl_2nd_order": round(pnl_2nd, 2),
            "pnl_pct": round(pnl_2nd / br.market_value * 100, 4) if br.market_value else 0,
        })

    return {
        "shock_bps": shock_bps,
        "bonds": bond_pnl,
        "total_pnl_1st_order": round(total_pnl_1st, 2),
        "total_pnl_2nd_order": round(total_pnl_2nd, 2),
        "total_market_value": portfolio.total_market_value,
        "total_pnl_pct": round(total_pnl_2nd / portfolio.total_market_value * 100, 4) if portfolio.total_market_value else 0,
    }


# ── Cashflows ────────────────────────────────────────────────────────────────

MONTH_LABELS = {
    1: "jan", 2: "fev", 3: "mar", 4: "abr", 5: "mai", 6: "jun",
    7: "jul", 8: "ago", 9: "set", 10: "out", 11: "nov", 12: "dez",
}


def _add_business_days(start: date, du: int) -> date:
    d = start
    counted = 0
    while counted < du:
        d += timedelta(days=1)
        if _is_business_day(d):
            counted += 1
    return d


def _date_label(d: date) -> str:
    return f"{MONTH_LABELS.get(d.month, str(d.month))}/{d.year}"


def compute_portfolio_cashflows(
    bonds: list[BondInput],
    vna_override: dict[str, float] | None = None,
) -> dict[str, Any]:
    vna_map = vna_override or {}
    liq_dates: dict[str, date] = {}
    all_flows: list[dict[str, Any]] = []

    for bond in bonds:
        liq = _parse_date(bond.settlement_date)
        liq_dates[bond.id] = liq
        bond_type = bond.type.upper().replace(" ", "-").replace("_", "-")

        if bond_type in ("NTN-F", "NTNF", "NTN-B", "NTNB"):
            venc = _parse_date(bond.maturity_date)
            coupon_dates = _generate_coupon_dates(liq, venc)

            if bond_type in ("NTN-F", "NTNF"):
                cupom_sem = _round((1.0 + _NTNF_CUPOM_AA / 100.0) ** 0.5 - 1.0, 8)
                for i, cd in enumerate(coupon_dates):
                    is_last = (i == len(coupon_dates) - 1)
                    if is_last:
                        amount = (_VN * cupom_sem + _VN) * bond.quantity
                        event = "cupom + principal"
                    else:
                        amount = _VN * cupom_sem * bond.quantity
                        event = "cupom"
                    all_flows.append({
                        "date": cd.isoformat(),
                        "date_label": _date_label(cd),
                        "month_key": f"{cd.year}-{cd.month:02d}",
                        "bond_id": bond.id,
                        "bond_type": bond.type,
                        "maturity_label": getattr(bond, "maturity_label", None) or _date_label(venc),
                        "event": event,
                        "amount": round(amount, 2),
                    })
            else:
                cupom_sem = _round(((1.0 + _NTNB_CUPOM_AA / 100.0) ** 0.5 - 1.0) * 100, 6) / 100.0
                vna = bond.vna or vna_map.get("NTN-B") or _VN
                for i, cd in enumerate(coupon_dates):
                    is_last = (i == len(coupon_dates) - 1)
                    if is_last:
                        amount = vna * (1.0 + cupom_sem) * bond.quantity
                        event = "cupom + principal"
                    else:
                        amount = vna * cupom_sem * bond.quantity
                        event = "cupom"
                    all_flows.append({
                        "date": cd.isoformat(),
                        "date_label": _date_label(cd),
                        "month_key": f"{cd.year}-{cd.month:02d}",
                        "bond_id": bond.id,
                        "bond_type": bond.type,
                        "maturity_label": getattr(bond, "maturity_label", None) or _date_label(venc),
                        "event": event,
                        "amount": round(amount, 2),
                    })
        else:
            venc = _parse_date(bond.maturity_date)
            if bond_type == "LFT":
                vna = bond.vna or vna_map.get("LFT") or _VN
            else:
                vna = _VN
            amount = vna * bond.quantity
            all_flows.append({
                "date": venc.isoformat(),
                "date_label": _date_label(venc),
                "month_key": f"{venc.year}-{venc.month:02d}",
                "bond_id": bond.id,
                "bond_type": bond.type,
                "maturity_label": getattr(bond, "maturity_label", None) or _date_label(venc),
                "event": "principal",
                "amount": round(amount, 2),
            })

    all_flows.sort(key=lambda f: f["date"])

    total_amount = sum(f["amount"] for f in all_flows)
    next_flow = all_flows[0] if all_flows else None

    return {
        "flows": all_flows,
        "summary": {
            "total_flows": len(all_flows),
            "total_amount": round(total_amount, 2),
            "next_flow_date": next_flow["date"] if next_flow else None,
            "next_flow_date_label": next_flow["date_label"] if next_flow else None,
            "next_flow_amount": next_flow["amount"] if next_flow else None,
        },
        "vna_used": {k: round(v, 6) for k, v in vna_map.items()} if vna_map else None,
    }
