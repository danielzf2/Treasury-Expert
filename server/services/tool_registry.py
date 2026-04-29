"""
Registry of all tool functions available in the treasury MCP server.
Auto-collects public functions from each tools module for direct invocation
by the REST API (without going through the MCP protocol).

Inputs:
    None (auto-discovery on import).

Outputs:
    TOOL_REGISTRY: dict[str, Callable] — maps tool name to Python function.
    TOOL_METADATA: dict[str, dict] — maps tool name to {description, parameters}.
"""

from __future__ import annotations

import inspect
import sys
from pathlib import Path
from typing import Any, Callable

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tools import (
    titulos_publicos, curva_juros,
    futuros_di, futuros_dol, futuros_dap, futuros_frc,
    swaps, cambio, risco, opcoes,
    conversoes_taxas, calculo_financeiro, convencoes,
    dias_uteis, inflacao_implicita, cambio_produtos,
    risco_mercado, credito_privado, estrategias,
)

_TOOL_MODULES = [
    titulos_publicos, curva_juros,
    futuros_di, futuros_dol, futuros_dap, futuros_frc,
    swaps, cambio, risco, opcoes,
    conversoes_taxas, calculo_financeiro, convencoes,
    dias_uteis, inflacao_implicita, cambio_produtos,
    risco_mercado, credito_privado, estrategias,
]

_SKIP_NAMES = {"register"}

TOOL_REGISTRY: dict[str, Callable[..., str]] = {}
TOOL_METADATA: dict[str, dict[str, Any]] = {}


def _python_type_to_json(annotation: Any) -> str:
    mapping = {
        int: "number",
        float: "number",
        str: "string",
        bool: "boolean",
    }
    return mapping.get(annotation, "string")


def _build_metadata(func: Callable) -> dict[str, Any]:
    """Build JSON-Schema-like metadata from function signature + docstring."""
    sig = inspect.signature(func)
    doc = inspect.getdoc(func) or ""

    params: dict[str, Any] = {}
    required: list[str] = []

    for name, p in sig.parameters.items():
        ptype = _python_type_to_json(p.annotation) if p.annotation != inspect.Parameter.empty else "string"
        param_info: dict[str, Any] = {"type": ptype}
        if p.default is not inspect.Parameter.empty:
            param_info["default"] = p.default
        else:
            required.append(name)
        params[name] = param_info

    return {
        "description": doc.split("\n")[0] if doc else func.__name__,
        "parameters": {
            "type": "object",
            "properties": params,
            "required": required,
        },
    }


def _collect_tools() -> None:
    for mod in _TOOL_MODULES:
        for name, obj in inspect.getmembers(mod, inspect.isfunction):
            if name.startswith("_") or name in _SKIP_NAMES:
                continue
            if obj.__module__ != mod.__name__:
                continue
            TOOL_REGISTRY[name] = obj
            TOOL_METADATA[name] = _build_metadata(obj)


_collect_tools()


def list_tool_names() -> list[str]:
    """Returns sorted list of all available tool names."""
    return sorted(TOOL_REGISTRY.keys())


def call_tool(name: str, params: dict[str, Any]) -> str:
    """
    Calls a tool by name with the given parameters.

    Inputs:
        name: str — tool function name.
        params: dict — keyword arguments for the tool.

    Outputs:
        str — formatted result from the tool function.

    Raises:
        KeyError if tool name not found.
        TypeError/ValueError if parameters are invalid.
    """
    if name not in TOOL_REGISTRY:
        raise KeyError(f"Tool '{name}' not found. Available: {list_tool_names()}")
    return TOOL_REGISTRY[name](**params)
