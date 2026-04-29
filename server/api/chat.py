"""
REST endpoint for LLM-powered chat with treasury tool calling.

POST /api/chat — send messages, get AI response (streaming or complete).
GET  /api/models — list available models with pricing.
"""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import Any, Optional

from services.chat_service import (
    chat_completion,
    chat_stream,
    ALLOWED_MODELS,
    DEFAULT_MODEL,
    PRICING,
)

router = APIRouter(tags=["chat"])


class ChatMessage(BaseModel):
    role: str = Field(..., description="'user' or 'assistant'")
    content: str = Field(..., description="Message content")


class ChatRequest(BaseModel):
    messages: list[ChatMessage]
    stream: bool = Field(default=True, description="Stream response via SSE")
    model: Optional[str] = Field(default=None, description="Model override")


class ChatResponse(BaseModel):
    response: str


@router.post("/chat")
async def chat(req: ChatRequest) -> Any:
    msgs = [{"role": m.role, "content": m.content} for m in req.messages]

    if not msgs:
        raise HTTPException(status_code=422, detail="At least one message is required.")

    try:
        if req.stream:
            return StreamingResponse(
                chat_stream(msgs, model=req.model),
                media_type="text/event-stream",
                headers={
                    "Cache-Control": "no-cache",
                    "X-Accel-Buffering": "no",
                },
            )
        else:
            result = await chat_completion(msgs, model=req.model)
            return ChatResponse(response=result)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Chat error: {e}")


@router.get("/models")
async def list_models() -> dict:
    models = []
    for m in ALLOWED_MODELS:
        input_price, output_price = PRICING.get(m, (0, 0))
        models.append({
            "id": m,
            "input_price_per_1m": input_price,
            "output_price_per_1m": output_price,
            "default": m == DEFAULT_MODEL,
        })
    return {"models": models, "default": DEFAULT_MODEL}
