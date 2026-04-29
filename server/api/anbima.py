"""
REST endpoints for ANBIMA daily bond pricing data.

GET /api/anbima/titulos       — all bonds from latest ANBIMA file
GET /api/anbima/titulos/{tipo} — filtered by bond type (LTN, NTN-B, etc.)
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from typing import Any

from services.anbima_service import get_anbima_bonds, get_vna

router = APIRouter(prefix="/anbima", tags=["anbima"])


@router.get("/titulos")
async def list_bonds(refresh: bool = False) -> dict[str, Any]:
    try:
        return await get_anbima_bonds(force_refresh=refresh)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))


@router.get("/titulos/{tipo}")
async def list_bonds_by_type(tipo: str, refresh: bool = False) -> dict[str, Any]:
    try:
        data = await get_anbima_bonds(force_refresh=refresh)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))

    tipo_upper = tipo.upper().replace("_", "-").replace(" ", "-")
    filtered = [b for b in data["bonds"] if b["type"].upper() == tipo_upper]

    if not filtered:
        valid = sorted({b["type"] for b in data["bonds"]})
        raise HTTPException(
            status_code=404,
            detail=f"Nenhum titulo do tipo '{tipo}'. Disponiveis: {', '.join(valid)}",
        )

    return {
        "reference_date": data["reference_date"],
        "bonds": filtered,
    }


@router.get("/vna")
async def get_vna_values(refresh: bool = False) -> dict[str, Any]:
    try:
        return await get_vna(force_refresh=refresh)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
