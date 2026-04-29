"""
REST endpoint for direct tool invocation without LLM intermediation.

POST /api/calculate  — call any registered tool by name with parameters.
GET  /api/tools       — list all available tools with metadata.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Any

from services.tool_registry import (
    TOOL_REGISTRY,
    TOOL_METADATA,
    call_tool,
    list_tool_names,
)

router = APIRouter(tags=["calculate"])


class CalculateRequest(BaseModel):
    """
    Inputs:
        tool: str — name of the tool function to call.
        params: dict — keyword arguments for the tool.
    """
    tool: str = Field(..., description="Tool function name (e.g. 'precificar_ltn')")
    params: dict[str, Any] = Field(default_factory=dict, description="Keyword arguments")


class CalculateResponse(BaseModel):
    """
    Outputs:
        tool: str — name of the tool that was called.
        result: str — formatted result from the tool.
    """
    tool: str
    result: str


@router.post("/calculate", response_model=CalculateResponse)
async def calculate(req: CalculateRequest) -> CalculateResponse:
    """
    Calls a treasury tool directly and returns the formatted result.

    Inputs:
        req: CalculateRequest — tool name and parameters.

    Outputs:
        CalculateResponse — tool name and result string.
    """
    if req.tool not in TOOL_REGISTRY:
        raise HTTPException(
            status_code=404,
            detail=f"Tool '{req.tool}' not found. Available: {list_tool_names()}",
        )
    try:
        result = call_tool(req.tool, req.params)
    except (TypeError, ValueError) as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Tool error: {e}")
    return CalculateResponse(tool=req.tool, result=result)


@router.get("/tools")
async def list_tools() -> dict[str, Any]:
    """
    Lists all available tools with their metadata (description, parameters).

    Outputs:
        dict with 'count' and 'tools' keys.
    """
    return {
        "count": len(TOOL_METADATA),
        "tools": TOOL_METADATA,
    }
