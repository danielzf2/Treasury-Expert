"""
Chat service: orchestrates OpenAI with function calling against treasury tools.
Handles the LLM conversation loop: user message -> LLM -> tool calls -> results -> LLM -> response.

Inputs:
    Messages list (OpenAI chat format) and streaming flag.

Outputs:
    Complete response string or async generator of SSE chunks.
"""

from __future__ import annotations

import json
import logging
import os
from typing import Any, AsyncGenerator

from openai import AsyncOpenAI

from services.tool_registry import TOOL_REGISTRY, TOOL_METADATA, call_tool

log = logging.getLogger("treasury-chat")

SYSTEM_PROMPT = """Você é um especialista em tesouraria e renda fixa brasileira com 20 anos de experiência.
Você tem acesso a ferramentas de cálculo para precificação de títulos públicos (LTN, NTN-F, NTN-B, LFT),
derivativos (DI futuro, DOL, DAP, FRC), swaps, câmbio, risco (duration, DV01, convexidade), opções,
e uma base de conhecimento com documentos de referência sobre mercado financeiro brasileiro.

Regras de conteúdo:
- Responda em português brasileiro.
- Para temas quantitativos: (1) intuição econômica, (2) fórmula, (3) exemplo numérico.
- Apresente todo conteúdo como conhecimento próprio.
- NUNCA mencione "o livro", "a fonte", "o autor", "segundo a referência", "de acordo com o documento" ou variações. Você sabe isso.
- Números no padrão brasileiro: 1.234.567,89
- Taxas sempre com base indicada: 12,75% a.a.
- Use as ferramentas disponíveis para buscar informações e fazer cálculos quando necessário.

Regras de formatação:
- Use markdown rico: **negrito**, *itálico*, tabelas, listas.
- Fórmulas matemáticas: use notação LaTeX com delimitadores $...$ (inline) e $$...$$ (bloco centralizado). A interface renderiza KaTeX.
- OBRIGATÓRIO para frações: sempre use \\frac{numerador}{denominador} para que fique empilhado (numerador em cima, denominador embaixo). NUNCA use "/" para dividir em fórmulas.
- Use notação matemática profissional: \\cdot para multiplicação, \\times quando apropriado, \\left( \\right) para parênteses grandes, \\sum, \\prod, \\sqrt{}, subscripts e superscripts.
  Exemplo inline: a duration modificada é $D_{mod} = \\frac{D_{mac}}{1+y}$
  Exemplo bloco:
  $$PU = \\frac{VF}{\\left(1 + y\\right)^{\\frac{du}{252}}}$$
  Exemplo com somatório:
  $$PU = \\sum_{i=1}^{n} \\frac{CF_i}{\\left(1 + y\\right)^{\\frac{du_i}{252}}}$$
- Para fluxogramas (processos, etapas), use blocos mermaid com graph TD.
  REGRAS OBRIGATÓRIAS para mermaid:
  1. Labels CURTOS (máximo 5-6 palavras por nó)
  2. NUNCA coloque fórmulas, parênteses (), colchetes [], chaves {}, ^, /, +, * dentro dos labels
  3. Use aspas duplas nos labels para evitar erros de parsing: A["Obter dados"]
  4. Sem acentos nos labels (use "Calculo" em vez de "Cálculo")
  Exemplo:
  ```mermaid
  graph TD
    A["Dados de entrada"] --> B["Obter VNA base"]
    B --> C["Calcular VNA pro-rata"]
    C --> D["Contar dias uteis"]
    D --> E["Descontar fluxos"]
    E --> F["Somar valores presentes"]
    F --> G["Preco PU final"]
  ```
- NUNCA use mermaid para gráficos numéricos, charts, plots ou visualização de dados.
- NUNCA use gráficos ASCII ou diagramas com caracteres (*, |, +, ---).
- Para dados numéricos, SEMPRE use tabelas markdown. Se pedirem gráfico, apresente em tabela.
"""


def _build_openai_tools() -> list[dict[str, Any]]:
    """
    Converts the tool registry into OpenAI function calling format.

    Outputs:
        list of tool definitions in OpenAI's expected schema.
    """
    tools = []
    for name, meta in TOOL_METADATA.items():
        tools.append({
            "type": "function",
            "function": {
                "name": name,
                "description": meta["description"],
                "parameters": meta["parameters"],
            },
        })
    return tools


def _get_client() -> AsyncOpenAI:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY not set. Chat requires an OpenAI API key.")
    return AsyncOpenAI(api_key=api_key)


DEFAULT_MODEL = "gpt-4.1-mini"

ALLOWED_MODELS = [
    "gpt-4.1-mini",
    "gpt-4.1",
    "gpt-4.1-nano",
    "gpt-4o",
    "gpt-4o-mini",
    "gpt-5.4",
    "gpt-5.4-mini",
    "gpt-5.4-nano",
]

PRICING: dict[str, tuple[float, float]] = {
    "gpt-5.4":      (2.50, 15.00),
    "gpt-5.4-mini": (0.75,  4.50),
    "gpt-5.4-nano": (0.20,  1.25),
    "gpt-4.1":      (2.00,  8.00),
    "gpt-4.1-mini": (0.40,  1.60),
    "gpt-4.1-nano": (0.10,  0.40),
    "gpt-4o":       (2.50, 10.00),
    "gpt-4o-mini":  (0.15,  0.60),
}


def _resolve_model(model: str | None) -> str:
    if model and model in ALLOWED_MODELS:
        return model
    return os.environ.get("OPENAI_MODEL", DEFAULT_MODEL)


def _estimate_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    input_price, output_price = PRICING.get(model, (2.50, 10.00))
    return (prompt_tokens * input_price + completion_tokens * output_price) / 1_000_000


async def chat_completion(
    messages: list[dict[str, str]],
    max_tool_rounds: int = 5,
    model: str | None = None,
) -> str:
    """
    Non-streaming chat completion with automatic tool calling.

    Inputs:
        messages: list[dict] — conversation history in OpenAI format.
        max_tool_rounds: int — max rounds of tool calling before returning.
        model: str | None — model override (validated against ALLOWED_MODELS).

    Outputs:
        str — final assistant response.
    """
    client = _get_client()
    model = _resolve_model(model)
    openai_tools = _build_openai_tools()

    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    for _ in range(max_tool_rounds):
        response = await client.chat.completions.create(
            model=model,
            messages=full_messages,
            tools=openai_tools if openai_tools else None,
            tool_choice="auto" if openai_tools else None,
        )

        choice = response.choices[0]

        if choice.finish_reason == "tool_calls" and choice.message.tool_calls:
            full_messages.append(choice.message.model_dump())

            for tc in choice.message.tool_calls:
                fn_name = tc.function.name
                try:
                    fn_args = json.loads(tc.function.arguments)
                except json.JSONDecodeError:
                    fn_args = {}

                try:
                    result = call_tool(fn_name, fn_args)
                except Exception as e:
                    result = f"Erro na ferramenta {fn_name}: {e}"

                full_messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": result,
                })
            continue

        return choice.message.content or ""

    return "Limite de chamadas de ferramentas atingido. Tente reformular sua pergunta."


async def chat_stream(
    messages: list[dict[str, str]],
    max_tool_rounds: int = 5,
    model: str | None = None,
) -> AsyncGenerator[str, None]:
    """
    Streaming chat completion with tool calling support.
    Yields SSE-formatted chunks.

    Inputs:
        messages: list[dict] — conversation history.
        max_tool_rounds: int — max tool calling rounds.
        model: str | None — model override (validated against ALLOWED_MODELS).

    Outputs:
        AsyncGenerator[str, None] — SSE data chunks.
    """
    client = _get_client()
    model = _resolve_model(model)
    openai_tools = _build_openai_tools()

    full_messages = [{"role": "system", "content": SYSTEM_PROMPT}] + messages

    total_prompt_tokens = 0
    total_completion_tokens = 0

    for _ in range(max_tool_rounds):
        stream = await client.chat.completions.create(
            model=model,
            messages=full_messages,
            tools=openai_tools if openai_tools else None,
            tool_choice="auto" if openai_tools else None,
            stream=True,
            stream_options={"include_usage": True},
        )

        collected_content = ""
        tool_calls_acc: dict[int, dict[str, str]] = {}
        finish_reason = None

        async for chunk in stream:
            if chunk.usage:
                total_prompt_tokens += chunk.usage.prompt_tokens
                total_completion_tokens += chunk.usage.completion_tokens

            delta = chunk.choices[0].delta if chunk.choices else None
            finish_reason = chunk.choices[0].finish_reason if chunk.choices else None

            if delta and delta.content:
                collected_content += delta.content
                yield f"data: {json.dumps({'type': 'content', 'content': delta.content})}\n\n"

            if delta and delta.tool_calls:
                for tc_delta in delta.tool_calls:
                    idx = tc_delta.index
                    if idx not in tool_calls_acc:
                        tool_calls_acc[idx] = {"id": "", "name": "", "arguments": ""}
                    if tc_delta.id:
                        tool_calls_acc[idx]["id"] = tc_delta.id
                    if tc_delta.function:
                        if tc_delta.function.name:
                            tool_calls_acc[idx]["name"] = tc_delta.function.name
                        if tc_delta.function.arguments:
                            tool_calls_acc[idx]["arguments"] += tc_delta.function.arguments

        if tool_calls_acc:
            assistant_msg: dict[str, Any] = {
                "role": "assistant",
                "content": collected_content or None,
                "tool_calls": [
                    {
                        "id": tc["id"],
                        "type": "function",
                        "function": {"name": tc["name"], "arguments": tc["arguments"]},
                    }
                    for tc in tool_calls_acc.values()
                ],
            }
            full_messages.append(assistant_msg)

            for tc in tool_calls_acc.values():
                fn_name = tc["name"]
                yield f"data: {json.dumps({'type': 'tool_call', 'tool': fn_name})}\n\n"
                try:
                    fn_args = json.loads(tc["arguments"])
                except json.JSONDecodeError:
                    fn_args = {}
                try:
                    result = call_tool(fn_name, fn_args)
                except Exception as e:
                    result = f"Erro na ferramenta {fn_name}: {e}"

                full_messages.append({
                    "role": "tool",
                    "tool_call_id": tc["id"],
                    "content": result,
                })
                yield f"data: {json.dumps({'type': 'tool_result', 'tool': fn_name, 'result': result[:500]})}\n\n"

            continue

        cost = _estimate_cost(model, total_prompt_tokens, total_completion_tokens)
        usage_data = {
            "type": "usage",
            "prompt_tokens": total_prompt_tokens,
            "completion_tokens": total_completion_tokens,
            "total_tokens": total_prompt_tokens + total_completion_tokens,
            "estimated_cost_usd": round(cost, 6),
            "model": model,
        }
        yield f"data: {json.dumps(usage_data)}\n\n"
        yield f"data: {json.dumps({'type': 'done'})}\n\n"
        return

    cost = _estimate_cost(model, total_prompt_tokens, total_completion_tokens)
    usage_data = {
        "type": "usage",
        "prompt_tokens": total_prompt_tokens,
        "completion_tokens": total_completion_tokens,
        "total_tokens": total_prompt_tokens + total_completion_tokens,
        "estimated_cost_usd": round(cost, 6),
        "model": model,
    }
    yield f"data: {json.dumps(usage_data)}\n\n"
    yield f"data: {json.dumps({'type': 'done'})}\n\n"
