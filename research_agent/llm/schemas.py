"""Schemas for LiteLLM responses and token usage."""

from pydantic import BaseModel


class TokenUsage(BaseModel):
    """Token usage for a given request."""

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class LLMResponse(BaseModel):
    """LLM response for a given request."""

    id: str
    created: int
    model: str
    system_fingerprint: str
    content: str
    role: str
    object: str
    usage: TokenUsage
