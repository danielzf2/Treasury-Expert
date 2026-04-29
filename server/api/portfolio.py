"""
REST endpoints for portfolio risk analysis and hedge suggestions.

POST /api/portfolio/risk     — compute risk metrics for a bond portfolio.
POST /api/portfolio/hedge    — suggest DI futures hedge.
POST /api/portfolio/scenario — simulate a parallel rate shock.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Any

from services.portfolio_service import (
    BondInput,
    compute_portfolio_risk,
    compute_hedge,
    simulate_scenario,
    compute_portfolio_cashflows,
    enrich_bond,
)
from services.anbima_service import get_vna, get_anbima_bonds

router = APIRouter(prefix="/portfolio", tags=["portfolio"])


class BondRequest(BaseModel):
    """Single bond in the portfolio request."""
    id: str
    type: str = Field(..., description="LTN, NTN-F, NTN-B, or LFT")
    notional: float = Field(..., description="Total face value in BRL")
    quantity: int = Field(default=1, description="Number of bonds")
    rate: float = Field(..., description="Purchase rate (% p.a.)")
    settlement_date: str = Field(..., description="DD/MM/YYYY or YYYY-MM-DD")
    maturity_date: str = Field(..., description="DD/MM/YYYY or YYYY-MM-DD")
    vna: float | None = Field(default=None, description="VNA for NTN-B")
    premium_bps: float | None = Field(default=None, description="Premium/discount bps for LFT")
    current_rate: float | None = Field(default=None, description="Current market rate for MtM (% p.a.)")


class PortfolioRiskRequest(BaseModel):
    """
    Inputs:
        bonds: list of bond specifications.
    """
    bonds: list[BondRequest]


class HedgeRequest(BaseModel):
    """
    Inputs:
        bonds: list of bond specifications.
        hedge_rate_aa: float — DI futures rate (% p.a.) for the hedge vertex.
        hedge_du: int — business days to maturity of the hedge contract.
        contract_face: float — face value per DI contract (default 100,000).
    """
    bonds: list[BondRequest]
    hedge_rate_aa: float = Field(..., description="DI futures implied rate (% p.a.)")
    hedge_du: int = Field(..., description="Business days to maturity of hedge contract")
    contract_face: float = Field(default=100_000.0, description="Face value per contract")


class ScenarioRequest(BaseModel):
    """
    Inputs:
        bonds: list of bond specifications.
        shock_bps: float — parallel shift in basis points.
    """
    bonds: list[BondRequest]
    shock_bps: float = Field(..., description="Parallel shock in basis points (positive = rates up)")


def _to_bond_input(b: BondRequest) -> BondInput:
    return BondInput(
        id=b.id,
        type=b.type,
        notional=b.notional,
        quantity=b.quantity,
        rate=b.rate,
        settlement_date=b.settlement_date,
        maturity_date=b.maturity_date,
        vna=b.vna,
        premium_bps=b.premium_bps,
        current_rate=b.current_rate,
    )


class EnrichBondRequest(BaseModel):
    type: str = Field(..., description="LTN, NTN-F, NTN-B, or LFT")
    purchase_date: str | None = Field(default=None, description="Trade date (YYYY-MM-DD)")
    settlement_date: str = Field(..., description="Settlement date (YYYY-MM-DD)")
    maturity_date: str = Field(..., description="YYYY-MM-DD or DD/MM/YYYY")
    quantity: int = Field(default=1)
    input_mode: str = Field(..., description="'taxa' or 'pu'")
    rate: float | None = Field(default=None, description="Rate (% p.a.) — required when input_mode=taxa")
    pu: float | None = Field(default=None, description="PU — required when input_mode=pu")
    vna: float | None = Field(default=None, description="VNA override for NTN-B / LFT")


def _find_indicative_rate(bonds_data: dict[str, Any], bond_type: str, maturity: str) -> float | None:
    bond_type_upper = bond_type.upper().replace(" ", "-").replace("_", "-")
    for b in bonds_data.get("bonds", []):
        if b["type"].upper() == bond_type_upper and b["maturity"] == maturity:
            return b.get("indicative_rate")
    return None


@router.post("/enrich-bond")
async def enrich_bond_endpoint(req: EnrichBondRequest) -> dict[str, Any]:
    bond_type_upper = req.type.upper().replace(" ", "-").replace("_", "-")

    vna = req.vna
    vna_ref_date = None
    if vna is None and bond_type_upper in ("NTN-B", "NTNB", "LFT"):
        try:
            vna_result = await get_vna()
            vna_map = vna_result.get("vna", {})
            key = "NTN-B" if bond_type_upper in ("NTN-B", "NTNB") else "LFT"
            vna = vna_map.get(key)
            vna_ref_date = vna_result.get("reference_date")
        except Exception:
            pass

    mtm_rate: float | None = None
    anbima_ref_date: str | None = None
    try:
        anbima_data = await get_anbima_bonds()
        mtm_rate = _find_indicative_rate(anbima_data, req.type, req.maturity_date)
        anbima_ref_date = anbima_data.get("reference_date")
    except Exception:
        pass

    from datetime import date as _date
    mtm_settlement = _date.today().isoformat()

    try:
        result = enrich_bond(
            bond_type=req.type,
            settlement_date=req.settlement_date,
            maturity_date=req.maturity_date,
            quantity=req.quantity,
            input_mode=req.input_mode,
            rate=req.rate,
            pu_input=req.pu,
            vna=vna,
            mtm_settlement_date=mtm_settlement if mtm_rate is not None else None,
            mtm_rate=mtm_rate,
        )

        result["reference_date"] = anbima_ref_date or vna_ref_date
        return result
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Calculation error: {e}")


@router.post("/risk")
async def portfolio_risk(req: PortfolioRiskRequest) -> dict[str, Any]:
    """
    Computes per-bond and portfolio-level risk metrics.

    Inputs:
        req: PortfolioRiskRequest — list of bonds.

    Outputs:
        dict with bond-level risks and portfolio aggregates.
    """
    if not req.bonds:
        raise HTTPException(status_code=422, detail="Portfolio must have at least one bond.")
    try:
        bonds = [_to_bond_input(b) for b in req.bonds]
        result = compute_portfolio_risk(bonds)
        return {
            "bonds": [
                {
                    "id": br.id,
                    "type": br.type,
                    "pu": br.pu,
                    "market_value": br.market_value,
                    "du": br.du,
                    "duration_macaulay": br.duration_macaulay,
                    "duration_modified": br.duration_modified,
                    "duration_anbima_du": br.duration_anbima_du,
                    "convexity": br.convexity,
                    "dv01": br.dv01,
                    "carry_1du": br.carry_1du,
                    "notional": br.notional,
                    "quantity": br.quantity,
                    "rate": br.rate,
                    "current_rate": br.current_rate,
                }
                for br in result.bonds
            ],
            "total_dv01": result.total_dv01,
            "total_market_value": result.total_market_value,
            "weighted_duration_mod": result.weighted_duration_mod,
            "weighted_duration_anbima": result.weighted_duration_anbima,
            "weighted_convexity": result.weighted_convexity,
            "exposure_by_type": result.exposure_by_type,
            "exposure_by_maturity_bucket": result.exposure_by_maturity_bucket,
        }
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Calculation error: {e}")


@router.post("/hedge")
async def portfolio_hedge(req: HedgeRequest) -> dict[str, Any]:
    """
    Suggests DI futures hedge for the portfolio.

    Inputs:
        req: HedgeRequest — bonds + hedge parameters.

    Outputs:
        dict with hedge recommendation.
    """
    if not req.bonds:
        raise HTTPException(status_code=422, detail="Portfolio must have at least one bond.")
    try:
        bonds = [_to_bond_input(b) for b in req.bonds]
        result = compute_hedge(bonds, req.hedge_rate_aa, req.hedge_du, req.contract_face)
        return {
            "portfolio_dv01": result.portfolio_dv01,
            "hedge_dv01_per_contract": result.hedge_dv01_per_contract,
            "contracts_needed": result.contracts_needed,
            "contracts_raw": result.contracts_raw,
            "residual_dv01": result.residual_dv01,
            "direction": result.direction,
            "hedge_maturity_du": result.hedge_maturity_du,
        }
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.post("/scenario")
async def portfolio_scenario(req: ScenarioRequest) -> dict[str, Any]:
    """
    Simulates parallel rate shock on the portfolio.

    Inputs:
        req: ScenarioRequest — bonds + shock size.

    Outputs:
        dict with per-bond and total P&L estimates.
    """
    if not req.bonds:
        raise HTTPException(status_code=422, detail="Portfolio must have at least one bond.")
    try:
        bonds = [_to_bond_input(b) for b in req.bonds]
        return simulate_scenario(bonds, req.shock_bps)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=422, detail=str(e))


@router.post("/cashflows")
async def portfolio_cashflows(req: PortfolioRiskRequest) -> dict[str, Any]:
    if not req.bonds:
        raise HTTPException(status_code=422, detail="Portfolio must have at least one bond.")
    try:
        vna_data: dict[str, float] = {}
        try:
            vna_result = await get_vna()
            vna_data = vna_result.get("vna", {})
        except Exception:
            pass

        bonds = [_to_bond_input(b) for b in req.bonds]
        return compute_portfolio_cashflows(bonds, vna_override=vna_data)
    except (ValueError, TypeError) as e:
        raise HTTPException(status_code=422, detail=str(e))
