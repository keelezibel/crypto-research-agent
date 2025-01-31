"""LiteLLM wrapper module.

Handles completions and chat interactions with language models.
"""

from __future__ import annotations

import asyncio
from typing import Any

import litellm
from litellm.utils import ModelResponse

from research_agent.llm.config import DEEPSEEK_CHAT_MODEL
from research_agent.logger import logger


async def aget_completion(
    model: str,
    llm_config: dict[str, Any],
    messages: list[dict],
) -> ModelResponse:
    """Get completion from the language model.

    Args:
    ----
        model: The name of the model to use
        llm_config: Configuration dictionary for the model
        messages: List of message dictionaries containing the conversation

    Returns:
    -------
        Model response object

    Raises:
    ------
        BadRequestError: If the API request fails

    """
    litellm.OpenAIConfig(**llm_config)
    return await litellm.acompletion(model=model, messages=messages)


if __name__ == "__main__":
    messages = [{"content": "Hello, how are you?", "role": "user"}]

    response = asyncio.run(
        aget_completion(
            model=str(DEEPSEEK_CHAT_MODEL.get("name", "deepseek/deepseek-chat")),
            llm_config=DEEPSEEK_CHAT_MODEL.get("parameters", {}),
            messages=messages,
        ),
    )
    if response.choices and response.choices[0].message:
        logger.info(response.choices[0].message.content)
