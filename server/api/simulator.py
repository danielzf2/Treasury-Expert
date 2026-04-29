"""FastAPI router — simulator endpoints for TPF + Derivativos."""

from __future__ import annotations

import json
import time
from dataclasses import asdict
from datetime import date, datetime
from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from lib.calendar import parse_ticker, du_entre, dc_entre, default_liq_date
from lib.market_data import fetch_all, get_tpf_vctos, find_di1_rate_for_date, MarketSnapshot
from lib.instruments import INSTRUMENTS, pu, duration, dv01, key_rate_duration, cupom_cambial_implicito
from lib.exposure import get_exposure, detect_strategy, analyze_risk_factors, suggest_hedge
from lib.scenarios import SCENARIOS, calc_scenario_delta, calc_leg_pnl, calc_leg_pnl_per_flow
from lib.charts import (
    chart_curva_antes_depois, chart_pnl_barras,
    chart_pnl_consolidado, chart_pnl_por_perna,
    chart_cupom_cambial, chart_dol_forward, chart_taxa_real,
)

router = APIRouter(tags=["simulator"])

# ---------------------------------------------------------------------------
# PRESETS
# ---------------------------------------------------------------------------

PRESETS = {
    "Casada LTN+DI1": [
        {"instrument": "LTN", "ticker": "F32", "direction": "C", "quantity": 2000, "taxa": 13.7625, "corr_type": "% na taxa", "corr_value": 0.001},
        {"instrument": "DI1", "ticker": "F32", "direction": "C", "quantity": 20, "taxa": 13.650, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "Venda Casada LTN+DI1": [
        {"instrument": "LTN", "ticker": "F32", "direction": "V", "quantity": 2000, "taxa": 13.7625, "corr_type": "% na taxa", "corr_value": 0.001},
        {"instrument": "DI1", "ticker": "F32", "direction": "V", "quantity": 20, "taxa": 13.650, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "Casada NTN-F+DI1": [
        {"instrument": "NTN-F", "ticker": "F31", "direction": "C", "quantity": 2000, "taxa": 13.80, "corr_type": "% na taxa", "corr_value": 0.001},
        {"instrument": "DI1", "ticker": "F31", "direction": "C", "quantity": 20, "taxa": 13.65, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "Casada NTN-B+DAP": [
        {"instrument": "NTN-B", "ticker": "N29", "direction": "C", "quantity": 2000, "taxa": 7.50, "corr_type": "% na taxa", "corr_value": 0.001, "vna": 4500.0},
        {"instrument": "DAP", "ticker": "N29", "direction": "C", "quantity": 20, "taxa": 7.40, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "DOL+DI1 (cupom sint.)": [
        {"instrument": "DOL", "ticker": "K26", "direction": "C", "quantity": 10, "taxa": 4976.5, "corr_type": "Nenhuma", "corr_value": 0.0},
        {"instrument": "DI1", "ticker": "K26", "direction": "C", "quantity": 10, "taxa": 14.60, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "DI1+FRC (dol sint.)": [
        {"instrument": "DI1", "ticker": "F28", "direction": "C", "quantity": 20, "taxa": 14.60, "corr_type": "R$/contrato", "corr_value": 1.30},
        {"instrument": "FRC", "ticker": "F28", "direction": "V", "quantity": 20, "taxa": 5.06, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "FRC direcional": [
        {"instrument": "FRC", "ticker": "F28", "direction": "C", "quantity": 20, "taxa": 5.06, "corr_type": "R$/contrato", "corr_value": 1.30},
    ],
    "LTN direcional": [
        {"instrument": "LTN", "ticker": "F32", "direction": "C", "quantity": 2000, "taxa": 13.76, "corr_type": "% na taxa", "corr_value": 0.001},
    ],
}

# ---------------------------------------------------------------------------
# Market-data cache (module-level, TTL-based)
# ---------------------------------------------------------------------------

_market_cache: dict[str, Any] = {"snap": None, "ts": 0.0}
_CACHE_TTL = 300


def _get_market_data() -> MarketSnapshot:
    now = time.time()
    if _market_cache["snap"] and (now - _market_cache["ts"]) < _CACHE_TTL:
        return _market_cache["snap"]
    snap = fetch_all()
    _market_cache["snap"] = snap
    _market_cache["ts"] = now
    return snap


# ---------------------------------------------------------------------------
# Ticker helpers
# ---------------------------------------------------------------------------

_MONTH_TO_TICKER = {
    1: "F", 2: "G", 3: "H", 4: "J", 5: "K", 6: "M",
    7: "N", 8: "Q", 9: "U", 10: "V", 11: "X", 12: "Z",
}


def _date_to_ticker(date_str: str) -> str:
    parts = date_str.split("-")
    return f"{_MONTH_TO_TICKER[int(parts[1])]}{int(parts[0]) % 100:02d}"


def _available_tickers(instrument: str, snap: MarketSnapshot) -> list[str]:
    _src = {
        "DI1": snap.di1, "DOL": snap.dol, "FRC": snap.frc,
        "DAP": snap.dap, "DDI": snap.ddi,
    }
    if instrument in _src:
        return [c["symb"][3:] for c in _src[instrument] if len(c["symb"]) > 3]
    if instrument in ("LTN", "NTN-F", "NTN-B", "LFT"):
        return [_date_to_ticker(d) for d in get_tpf_vctos(instrument)]
    return []


# ---------------------------------------------------------------------------
# Serialization helpers
# ---------------------------------------------------------------------------

def _serialize(obj: Any) -> Any:
    """Recursively convert Python objects to JSON-serializable types."""
    if obj is None:
        return None
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, date) and not isinstance(obj, datetime):
        return obj.strftime("%d/%m/%Y")
    if isinstance(obj, datetime):
        return obj.strftime("%d/%m/%Y %H:%M:%S")
    if hasattr(obj, "__dataclass_fields__"):
        return {k: _serialize(v) for k, v in asdict(obj).items()}
    if isinstance(obj, dict):
        return {k: _serialize(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_serialize(v) for v in obj]
    return str(obj)


def _serialize_leg(leg: dict) -> dict:
    """Convert a processed leg dict to a JSON-safe dict."""
    out: dict[str, Any] = {}
    for k, v in leg.items():
        if k == "info":
            out["info_type"] = v.type
            out["info_conv"] = v.conv
            out["info_benchmark"] = v.benchmark
            out["info_face"] = v.face
            out["info_mult"] = v.mult
        elif k == "parsed":
            out["parsed_label"] = v["label"]
            out["parsed_full"] = v["full"]
        elif k == "exp":
            out["exp_ativo"] = v.get("ativo", "—")
            out["exp_passivo"] = v.get("passivo", "—")
        elif k == "liq":
            out["liq"] = v.strftime("%d/%m/%Y") if isinstance(v, date) else v
        else:
            out[k] = _serialize(v)
    return out


def _serialize_leg_ref(leg: dict) -> dict:
    """Extract key fields from a leg dict used as a reference inside strategy/hedge."""
    parsed = leg.get("parsed", {})
    label = parsed.get("label", "") if isinstance(parsed, dict) else ""
    return {
        "instrument": leg.get("instrument"),
        "ticker": leg.get("ticker"),
        "direction": leg.get("direction"),
        "taxa": leg.get("taxa"),
        "tax_fin": leg.get("tax_fin"),
        "du": leg.get("du"),
        "dc": leg.get("dc"),
        "dv01_total": leg.get("dv01_total"),
        "d_mac": leg.get("d_mac"),
        "quantity": leg.get("quantity"),
        "parsed_label": label,
    }


def _parse_br_date(value: Any) -> date | None:
    if isinstance(value, date):
        return value
    if not isinstance(value, str) or not value:
        return None
    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def _serialize_strategy(strat: dict) -> dict:
    if not strat:
        return {}
    out: dict[str, Any] = {}
    for k, v in strat.items():
        if isinstance(v, dict) and "info" in v:
            out[k] = _serialize_leg_ref(v)
            out[f"{k}_taxa"] = v.get("taxa", 0)
            out[f"{k}_inst"] = v.get("instrument", "")
        else:
            out[k] = _serialize(v)
    return out


def _serialize_hedge(hedge: dict | None) -> dict | None:
    if not hedge:
        return None
    out: dict[str, Any] = {}
    for k, v in hedge.items():
        if k == "tpf" and isinstance(v, dict):
            out[k] = _serialize_leg_ref(v)
        elif k == "strip" and isinstance(v, list):
            out[k] = [_serialize(s) for s in v]
        else:
            out[k] = _serialize(v)
    return out


def _cashflow_breakdown(leg: dict) -> dict | None:
    info = leg.get("info")
    if not info or info.type != "tpf":
        return None

    leg_vna = leg.get("vna")
    vna_scale = (leg_vna / 100) if (leg.get("instrument") == "NTN-B" and leg_vna and leg_vna > 0) else 1.0

    rows = []
    if info.cup_sem > 0:
        flows = key_rate_duration(
            leg["instrument"],
            leg["taxa"],
            leg["du"],
            leg.get("liq"),
            leg.get("parsed", {}).get("date"),
        )
        if not flows:
            return None

        pv_total = sum(f.pv * vna_scale for f in flows)
        duration_macaulay = sum(f.krd for f in flows)
        duration_anbima_du = sum(f.du * f.pv for f in flows) / sum(f.pv for f in flows) if flows else 0.0

        for f in flows:
            rows.append({
                "label": f.label,
                "payment_date": f.payment_date.strftime("%d/%m/%Y") if f.payment_date else "",
                "du": f.du,
                "t_anos": f.t_anos,
                "nominal": f.nominal * vna_scale,
                "pv": f.pv * vna_scale,
                "peso": f.peso,
                "krd": f.krd,
            })
    else:
        venc = leg.get("parsed", {}).get("date")
        duration_macaulay = leg["d_mac"]
        duration_anbima_du = leg["du"]
        pv_total = leg["pu"]
        rows.append({
            "label": "Principal",
            "payment_date": venc.strftime("%d/%m/%Y") if isinstance(venc, date) else "",
            "du": leg["du"],
            "t_anos": leg["du"] / 252,
            "nominal": info.face,
            "pv": leg["pu"],
            "peso": 1.0,
            "krd": duration_macaulay,
        })

    return {
        "flows": rows,
        "pv_total": pv_total,
        "duration_macaulay": duration_macaulay,
        "duration_anbima_du": duration_anbima_du,
    }


# ---------------------------------------------------------------------------
# Leg processing (mirrors Streamlit's process_legs)
# ---------------------------------------------------------------------------

def _process_raw_legs(legs_input: list[dict], data_neg_str: str, spot: float) -> list[dict]:
    """Process raw leg dicts into enriched leg dicts with all computed fields."""
    data_neg = date.fromisoformat(data_neg_str)
    results: list[dict] = []

    for leg in legs_input:
        info = INSTRUMENTS.get(leg["instrument"])
        if not info:
            continue
        parsed = parse_ticker(leg["instrument"], leg["ticker"])
        if not parsed:
            continue

        liq = default_liq_date(data_neg)
        du_val = du_entre(liq, parsed["date"])
        dc_val = dc_entre(liq, parsed["date"])

        if info.type == "tpf" or info.conv == "price":
            side = "Ativo" if leg["direction"] == "C" else "Passivo"
        else:
            side = "Passivo" if leg["direction"] == "C" else "Ativo"

        if info.conv == "price":
            tax_dir = "Compra USD" if leg["direction"] == "C" else "Vende USD"
        elif info.type == "tpf":
            tax_dir = "Vende taxa" if leg["direction"] == "C" else "Compra taxa"
        else:
            tax_dir = "Compra taxa" if leg["direction"] == "C" else "Vende taxa"

        venc = parsed["date"]
        leg_vna = leg.get("vna")
        pu_val = pu(leg["instrument"], leg["taxa"], du_val, dc_val, liq, venc, vna=leg_vna)
        dur = duration(leg["instrument"], leg["taxa"], du_val, dc_val, liq, venc)
        dv = dv01(leg["instrument"], leg["taxa"], du_val, dc_val, leg["quantity"], liq, venc, vna=leg_vna)
        fin = pu_val * leg["quantity"]
        noc = leg["quantity"] * info.face
        exp = get_exposure(leg["instrument"], leg["direction"], leg["taxa"])

        tax_fin = leg["taxa"]
        corr_brl, corr_bps = 0.0, 0.0
        corr_type = leg.get("corr_type", "Nenhuma")
        corr_value = leg.get("corr_value", 0.0)

        if corr_type == "% na taxa" and info.conv != "price":
            tax_fin = (
                leg["taxa"] - corr_value
                if leg["direction"] == "C"
                else leg["taxa"] + corr_value
            )
            corr_brl = abs(pu(leg["instrument"], tax_fin, du_val, dc_val, liq, venc, vna=leg_vna) - pu_val) * leg["quantity"]
            corr_bps = corr_value * 100
        elif corr_type in ("R$/contrato", "R$/titulo"):
            corr_brl = corr_value * leg["quantity"]
            corr_bps = corr_brl / dv.total if dv.total > 0 else 0

        processed = {
            "instrument": leg["instrument"],
            "direction": leg["direction"],
            "ticker": leg["ticker"],
            "quantity": leg["quantity"],
            "taxa": leg["taxa"],
            "corr_type": corr_type,
            "corr_value": corr_value,
            "vna": leg_vna,
            "hedge_mode": leg.get("hedge_mode", "manual"),
            "auto": leg.get("auto", False),
            "auto_for": leg.get("auto_for"),
            "info": info,
            "parsed": parsed,
            "du": du_val,
            "dc": dc_val,
            "liq": liq,
            "side": side,
            "tax_dir": tax_dir,
            "tax_fin": tax_fin,
            "pu": pu_val,
            "fin": fin,
            "noc": noc,
            "d_mac": dur.macaulay,
            "d_mod": dur.modificada,
            "dv01_unit": dv.unit,
            "dv01_total": dv.total,
            "corr_brl": corr_brl,
            "corr_bps": corr_bps,
            "exp": exp,
        }
        processed["cashflows"] = _cashflow_breakdown(processed)
        results.append(processed)

    return results


def _ticker_for_du(du: int, liq_date: date) -> str:
    """Approximate ticker from a DU offset from liq_date."""
    from datetime import timedelta
    target_dc = round(du * 365 / 252)
    target_date = liq_date + timedelta(days=target_dc)
    return f"{_MONTH_TO_TICKER[target_date.month]}{target_date.year % 100:02d}"


def _expand_hedge_legs(processed_legs: list[dict],
                       di1_curve: list[dict], dap_curve: list[dict],
                       data_neg_str: str, spot: float) -> list[dict]:
    """Expand TPF legs with hedge_mode != manual by inserting auto DI1/DAP legs.

    Filters out any pre-existing auto legs (regenerates from scratch each call).
    Returns a new list with auto-generated legs inserted immediately after their TPF.
    """
    from lib.curves import flat_forward_interp, build_di_vertices, build_dap_vertices

    processed_legs = [l for l in processed_legs if not l.get("auto")]

    data_neg = date.fromisoformat(data_neg_str)
    liq = default_liq_date(data_neg)

    di_vertices = build_di_vertices(di1_curve, liq) if di1_curve else []
    dap_vertices = build_dap_vertices(dap_curve, liq) if dap_curve else []

    user_di_pairs = [(l["du"], l["taxa"]) for l in processed_legs if l.get("instrument") == "DI1"]
    user_dap_pairs = [(l["du"], l["taxa"]) for l in processed_legs if l.get("instrument") == "DAP"]

    if not di_vertices and user_di_pairs:
        di_vertices = sorted(user_di_pairs)
    if not dap_vertices and user_dap_pairs:
        dap_vertices = sorted(user_dap_pairs)

    def _rate_at_du(du: int, hedge_inst: str, fallback: float) -> float:
        verts = dap_vertices if hedge_inst == "DAP" else di_vertices
        r = flat_forward_interp(verts, du) if verts else None
        return r if r is not None else fallback

    expanded: list[dict] = []
    for idx, leg in enumerate(processed_legs):
        expanded.append(leg)
        info = leg.get("info") or INSTRUMENTS.get(leg.get("instrument"))
        if not info or info.cup_sem <= 0:
            continue
        mode = leg.get("hedge_mode", "manual")
        if mode == "manual":
            continue

        hedge_inst = "DAP" if leg["instrument"] == "NTN-B" else "DI1"

        if mode in ("maturity", "duration"):
            target_du = leg["du"] if mode == "maturity" else round(leg["d_mac"] * 252)
            target_du = max(1, target_du)
            taxa = _rate_at_du(target_du, hedge_inst, leg["taxa"])
            ticker = _ticker_for_du(target_du, liq)

            auto_input = {
                "instrument": hedge_inst,
                "ticker": ticker,
                "direction": leg["direction"],
                "quantity": 0,
                "taxa": taxa,
                "corr_type": "Nenhuma",
                "corr_value": 0.0,
                "auto": True,
                "auto_for": idx,
                "hedge_mode": "manual",
            }
            auto_processed = _process_raw_legs([auto_input], data_neg_str, spot)
            if not auto_processed:
                continue
            ap = auto_processed[0]
            di_unit_dv01 = ap["dv01_unit"]
            n = round(leg["dv01_total"] / di_unit_dv01) if di_unit_dv01 else 0

            auto_input["quantity"] = n
            ap2 = _process_raw_legs([auto_input], data_neg_str, spot)
            if ap2:
                expanded.append(ap2[0])

        elif mode == "strip":
            cf = leg.get("cashflows") or {}
            flows = cf.get("flows") or []
            if not flows:
                continue
            tir = leg["taxa"] / 100
            for f in flows:
                target_du = max(1, f["du"])
                taxa = _rate_at_du(target_du, hedge_inst, leg["taxa"])
                ticker = _ticker_for_du(target_du, liq)

                t = target_du / 252
                pv_flow = f["pv"]
                d_mod_flow = t / (1 + tir)
                dv01_flow = d_mod_flow * pv_flow * 0.0001 * leg["quantity"]

                temp_input = {
                    "instrument": hedge_inst,
                    "ticker": ticker,
                    "direction": leg["direction"],
                    "quantity": 1,
                    "taxa": taxa,
                    "corr_type": "Nenhuma",
                    "corr_value": 0.0,
                    "auto": True,
                    "auto_for": idx,
                    "hedge_mode": "manual",
                }
                ap_one = _process_raw_legs([temp_input], data_neg_str, spot)
                if not ap_one:
                    continue
                unit_dv01 = ap_one[0]["dv01_unit"]
                n = round(dv01_flow / unit_dv01) if unit_dv01 else 0
                if n == 0:
                    continue
                temp_input["quantity"] = n
                ap_full = _process_raw_legs([temp_input], data_neg_str, spot)
                if ap_full:
                    expanded.append(ap_full[0])

    return expanded


def _rehydrate_legs(legs: list[dict]) -> list[dict]:
    """Re-attach InstrumentInfo objects and parsed dicts to legs from the client."""
    result: list[dict] = []
    for leg in legs:
        leg = dict(leg)
        leg["info"] = INSTRUMENTS.get(leg.get("instrument"))
        if "parsed" not in leg or not isinstance(leg.get("parsed"), dict):
            p = parse_ticker(leg.get("instrument", ""), leg.get("ticker", ""))
            if p:
                leg["parsed"] = p
            else:
                leg["parsed"] = {"label": leg.get("parsed_label", ""), "full": leg.get("parsed_full", ""), "date": date.today()}
        if isinstance(leg["parsed"], dict) and "date" not in leg["parsed"]:
            p = parse_ticker(leg.get("instrument", ""), leg.get("ticker", ""))
            if p:
                leg["parsed"]["date"] = p["date"]
        liq = _parse_br_date(leg.get("liq"))
        if liq:
            leg["liq"] = liq
        result.append(leg)
    return result


# ---------------------------------------------------------------------------
# Pydantic request models
# ---------------------------------------------------------------------------

class LegInput(BaseModel):
    instrument: str
    ticker: str
    direction: str
    quantity: float
    taxa: float
    corr_type: str = "Nenhuma"
    corr_value: float = 0.0
    vna: float | None = None
    hedge_mode: str = "manual"  # manual | maturity | duration | strip
    auto: bool = False
    auto_for: int | None = None


class ProcessRequest(BaseModel):
    legs: list[LegInput]
    data_neg: str
    spot: float
    di1: list[dict] = []
    dap: list[dict] = []


class CurveChartRequest(BaseModel):
    legs: list[dict]
    scenario_key: str
    magnitude: float
    di1: list[dict] = []
    dap: list[dict] = []
    custom_parallel_bps: float = 0.0
    custom_slope_bps: float = 0.0
    custom_curvature_bps: float = 0.0


class PnlBarsRequest(BaseModel):
    legs: list[dict]
    scenario_key: str
    magnitude: float
    delta_fx_pct: float = 0.0
    delta_ipca_bps: float = 0.0
    delta_cupom_bps: float = 0.0
    custom_parallel_bps: float = 0.0
    custom_slope_bps: float = 0.0
    custom_curvature_bps: float = 0.0
    di1: list[dict] = []
    dap: list[dict] = []


class PnlConsolidatedRequest(BaseModel):
    legs: list[dict]
    scenario_key: str = "bear_par"
    magnitude: float = 10.0
    delta_fx_pct: float = 0.0
    delta_ipca_bps: float = 0.0
    delta_cupom_bps: float = 0.0
    custom_parallel_bps: float = 0.0
    custom_slope_bps: float = 0.0
    custom_curvature_bps: float = 0.0
    di1: list[dict] = []
    dap: list[dict] = []
    expand_flows: bool = False


class CupomChartRequest(BaseModel):
    frc_contracts: list[dict]
    delta_cupom_bps: float = 0.0
    legs: list[dict] = []


class ForwardChartRequest(BaseModel):
    di1: list[dict]
    frc: list[dict]
    spot: float
    delta_pre_bps: float = 0.0
    delta_cupom_bps: float = 0.0
    delta_fx_pct: float = 0.0
    legs: list[dict] = []


class RealChartRequest(BaseModel):
    dap_contracts: list[dict]
    delta_ipca_bps: float = 0.0
    legs: list[dict] = []


class MtmTableRequest(BaseModel):
    legs: list[dict]
    scenario_key: str
    magnitude: float = 10.0
    delta_fx_pct: float = 0.0
    delta_ipca_bps: float = 0.0
    delta_cupom_bps: float = 0.0
    custom_parallel_bps: float = 0.0
    custom_slope_bps: float = 0.0
    custom_curvature_bps: float = 0.0
    di1: list[dict] = []
    dap: list[dict] = []


# ---------------------------------------------------------------------------
# 1. GET /presets
# ---------------------------------------------------------------------------

@router.get("/presets")
def get_presets():
    return PRESETS


# ---------------------------------------------------------------------------
# 2. GET /market-data
# ---------------------------------------------------------------------------

@router.get("/market-data")
def get_market_data():
    snap = _get_market_data()
    return _serialize(snap)


# ---------------------------------------------------------------------------
# 3. POST /process
# ---------------------------------------------------------------------------

@router.post("/process")
def process(req: ProcessRequest):
    legs_input = [leg.model_dump() for leg in req.legs]
    valid = _process_raw_legs(legs_input, req.data_neg, req.spot)
    if not valid:
        raise HTTPException(status_code=400, detail="No valid legs to process")

    valid = _expand_hedge_legs(valid, req.di1, req.dap, req.data_neg, req.spot)

    strat = detect_strategy(valid, req.spot)
    risk_factors = analyze_risk_factors(valid, strat)
    total_corr = sum(l["corr_brl"] for l in valid)
    total_corr_bps = sum(l["corr_bps"] for l in valid if l["info"].conv != "price")

    hedge = None
    has_cupom_tpf = any(INSTRUMENTS[l["instrument"]].cup_sem > 0 for l in valid)
    if has_cupom_tpf:
        hedge = suggest_hedge(valid)

    total_dv01 = sum(l["dv01_total"] for l in valid)
    total_fin = sum(l["fin"] for l in valid if l["info"].conv != "price")

    return {
        "legs": [_serialize_leg(l) for l in valid],
        "strategy": _serialize_strategy(strat),
        "risk_factors": risk_factors,
        "total_corr": total_corr,
        "total_corr_bps": total_corr_bps,
        "total_dv01": total_dv01,
        "total_fin": total_fin,
        "hedge": _serialize_hedge(hedge),
    }


# ---------------------------------------------------------------------------
# 4. POST /charts/curve
# ---------------------------------------------------------------------------

@router.post("/charts/curve")
def chart_curve(req: CurveChartRequest):
    legs = _rehydrate_legs(req.legs)
    fig = chart_curva_antes_depois(
        legs, req.scenario_key, req.magnitude,
        di1_curve=req.di1 or None,
        dap_curve=req.dap or None,
        custom_parallel_bps=req.custom_parallel_bps,
        custom_slope_bps=req.custom_slope_bps,
        custom_curvature_bps=req.custom_curvature_bps,
    )
    return json.loads(fig.to_json())


# ---------------------------------------------------------------------------
# 5. POST /charts/pnl-bars
# ---------------------------------------------------------------------------

@router.post("/charts/pnl-bars")
def chart_pnl_bars(req: PnlBarsRequest):
    legs = _rehydrate_legs(req.legs)
    fig = chart_pnl_barras(
        legs, req.scenario_key, req.magnitude,
        delta_fx_pct=req.delta_fx_pct,
        delta_ipca_bps=req.delta_ipca_bps,
        delta_cupom_bps=req.delta_cupom_bps,
        custom_parallel_bps=req.custom_parallel_bps,
        custom_slope_bps=req.custom_slope_bps,
        custom_curvature_bps=req.custom_curvature_bps,
        di1_curve=req.di1 or None,
        dap_curve=req.dap or None,
    )
    return json.loads(fig.to_json())


# ---------------------------------------------------------------------------
# 6. POST /charts/pnl-consolidated
# ---------------------------------------------------------------------------

@router.post("/charts/pnl-consolidated")
def chart_pnl_consolidated(req: PnlConsolidatedRequest):
    legs = _rehydrate_legs(req.legs)
    fig = chart_pnl_consolidado(
        legs,
        scenario_key=req.scenario_key,
        magnitude=req.magnitude,
        delta_fx_pct=req.delta_fx_pct,
        delta_ipca_bps=req.delta_ipca_bps,
        delta_cupom_bps=req.delta_cupom_bps,
        custom_parallel_bps=req.custom_parallel_bps,
        custom_slope_bps=req.custom_slope_bps,
        custom_curvature_bps=req.custom_curvature_bps,
        di1_curve=req.di1 or None,
        dap_curve=req.dap or None,
    )
    return json.loads(fig.to_json())


# ---------------------------------------------------------------------------
# 7. POST /charts/pnl-per-leg
# ---------------------------------------------------------------------------

@router.post("/charts/pnl-per-leg")
def chart_pnl_per_leg(req: PnlConsolidatedRequest):
    legs = _rehydrate_legs(req.legs)
    fig = chart_pnl_por_perna(
        legs,
        scenario_key=req.scenario_key,
        magnitude=req.magnitude,
        delta_fx_pct=req.delta_fx_pct,
        delta_ipca_bps=req.delta_ipca_bps,
        delta_cupom_bps=req.delta_cupom_bps,
        custom_parallel_bps=req.custom_parallel_bps,
        custom_slope_bps=req.custom_slope_bps,
        custom_curvature_bps=req.custom_curvature_bps,
        di1_curve=req.di1 or None,
        dap_curve=req.dap or None,
        expand_flows=req.expand_flows,
    )
    return json.loads(fig.to_json())


# ---------------------------------------------------------------------------
# 8. POST /charts/cupom
# ---------------------------------------------------------------------------

@router.post("/charts/cupom")
def chart_cupom(req: CupomChartRequest):
    legs = _rehydrate_legs(req.legs) if req.legs else None
    fig = chart_cupom_cambial(
        req.frc_contracts,
        delta_cupom_bps=req.delta_cupom_bps,
        legs=legs,
    )
    return json.loads(fig.to_json())


# ---------------------------------------------------------------------------
# 9. POST /charts/forward
# ---------------------------------------------------------------------------

@router.post("/charts/forward")
def chart_forward(req: ForwardChartRequest):
    legs = _rehydrate_legs(req.legs) if req.legs else None
    fig = chart_dol_forward(
        req.di1, req.frc, req.spot,
        delta_pre_bps=req.delta_pre_bps,
        delta_cupom_bps=req.delta_cupom_bps,
        delta_fx_pct=req.delta_fx_pct,
        legs=legs,
    )
    return json.loads(fig.to_json())


# ---------------------------------------------------------------------------
# 10. POST /charts/real
# ---------------------------------------------------------------------------

@router.post("/charts/real")
def chart_real(req: RealChartRequest):
    legs = _rehydrate_legs(req.legs) if req.legs else None
    fig = chart_taxa_real(
        req.dap_contracts,
        delta_ipca_bps=req.delta_ipca_bps,
        legs=legs,
    )
    return json.loads(fig.to_json())


# ---------------------------------------------------------------------------
# 11. GET /tickers/{instrument}
# ---------------------------------------------------------------------------

@router.get("/tickers/{instrument}")
def get_tickers(instrument: str):
    snap = _get_market_data()
    tickers = _available_tickers(instrument, snap)
    return {"instrument": instrument, "tickers": tickers}


# ---------------------------------------------------------------------------
# 12. POST /mtm-table
# ---------------------------------------------------------------------------

_MTM_STEPS = [-20, -15, -10, -5, -2, -1, 0, 1, 2, 5, 10, 15, 20]


def _flow_pnl_for_leg(leg: dict, req: MtmTableRequest,
                      du_min: int, du_max: int,
                      spot_curve: list) -> dict | None:
    """Compute per-cashflow P&L using calc_leg_pnl_per_flow with the spot curve."""
    info = leg.get("info") or INSTRUMENTS.get(leg.get("instrument"))
    if not info or info.type != "tpf" or info.cup_sem <= 0:
        return None
    if not spot_curve:
        return None

    res = calc_leg_pnl_per_flow(
        leg, req.scenario_key, req.magnitude, du_min, du_max, spot_curve,
        req.custom_parallel_bps, req.custom_slope_bps, req.custom_curvature_bps,
        req.delta_ipca_bps,
    )
    if not res:
        return None

    rows = []
    for f in res["flows"]:
        rows.append({
            "label": f["label"],
            "payment_date": f["payment_date"].strftime("%d/%m/%Y") if f["payment_date"] else "",
            "du": f["du"],
            "nominal": None,
            "pv": f["old_pv"],
            "delta_bps": f["delta_bps"],
            "pnl": round(f["pnl_flow"], 2),
        })

    return {
        "instrument": leg["instrument"],
        "ticker": leg["ticker"],
        "parsed_label": leg.get("parsed_label") or leg.get("parsed", {}).get("label", ""),
        "direction": leg["direction"],
        "total": round(res["leg_pnl"], 2),
        "flows": rows,
        "spread_credito": res.get("spread_credito"),
    }


@router.post("/mtm-table")
def mtm_table(req: MtmTableRequest):
    from lib.scenarios import get_spot_curve_for_leg

    legs = _rehydrate_legs(req.legs)

    rate_legs = [l for l in legs if l["info"] and l["info"].conv != "price"]
    du_min = min(l["du"] for l in rate_legs) if rate_legs else 0
    du_max = max(l["du"] for l in rate_legs) if rate_legs else 1

    spot_per_leg = [
        get_spot_curve_for_leg(l, req.di1, req.dap, l.get("liq")) for l in legs
    ]

    rows: list[dict] = []
    for m in _MTM_STEPS:
        row_total = 0.0
        pnls = []
        for li, l in enumerate(legs):
            info = l.get("info") or INSTRUMENTS.get(l.get("instrument"))
            if info and info.conv == "price":
                delta = 0.0
            else:
                delta = calc_scenario_delta(
                    l["du"], du_min, du_max, req.scenario_key, m,
                    req.custom_parallel_bps, req.custom_slope_bps, req.custom_curvature_bps,
                )

            spot = spot_per_leg[li]
            if info and info.cup_sem > 0 and spot:
                res = calc_leg_pnl_per_flow(
                    l, req.scenario_key, m, du_min, du_max, spot,
                    req.custom_parallel_bps, req.custom_slope_bps, req.custom_curvature_bps,
                    req.delta_ipca_bps,
                )
                pnl = res["leg_pnl"] if res else 0.0
            else:
                pnl = calc_leg_pnl(
                    l, delta,
                    delta_fx_pct=req.delta_fx_pct,
                    delta_ipca_bps=req.delta_ipca_bps,
                    delta_cupom_bps=req.delta_cupom_bps,
                )
            row_total += pnl
            pnls.append(round(pnl, 2))

        rows.append({
            "delta": m,
            "pnls": pnls,
            "total": round(row_total, 2),
        })

    flow_pnl = [
        fp for fp in (
            _flow_pnl_for_leg(l, req, du_min, du_max, spot_per_leg[li])
            for li, l in enumerate(legs)
        )
        if fp is not None
    ]

    mag_row = next((r for r in rows if r["delta"] == req.magnitude), rows[len(rows)//2])
    return {"table": rows, "total_pnl": mag_row["total"], "flow_pnl": flow_pnl}
