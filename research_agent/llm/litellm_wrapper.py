"""LiteLLM wrapper module.

Handles completions and chat interactions with language models.
"""

from __future__ import annotations

import asyncio
from typing import Any

import litellm
from litellm.utils import ModelResponse

from research_agent.llm.config import BASE_MODEL
from research_agent.logger import logger


async def aget_completion(
    model: str, llm_config: dict[str, Any], messages: list[dict]
) -> ModelResponse:
    """Get completion from the language model.

    Args:
        model: The name of the model to use
        llm_config: Configuration dictionary for the model
        messages: List of message dictionaries containing the conversation

    Returns:
        Model response object

    Raises:
        BadRequestError: If the API request fails
    """
    litellm.OpenAIConfig(**llm_config)
    return await litellm.acompletion(model=model, messages=messages)


async def aget_completion_with_tools(
    model: str, llm_config: dict[str, Any], messages: list[dict], tools: list[dict]
) -> ModelResponse:
    """Get completion with tools from the language model.

    Args:
        model: The name of the model to use
        llm_config: Configuration dictionary for the model
        messages: List of message dictionaries containing the conversation
        tools: List of tool dictionaries available to the model

    Returns:
        Model response object

    Raises:
        BadRequestError: If the API request fails
    """
    litellm.OpenAIConfig(**llm_config)
    return await ModelResponse(
        litellm.acompletion(
            model=model,
            messages=messages,
            tools=tools,
        )
    )


async def aget_chat_completion_with_tools(
    model: str, llm_config: dict[str, Any], messages: list[dict], tools: list[dict]
) -> ModelResponse:
    """Get chat completion with tools from the language model.

    Args:
        model: The name of the model to use
        llm_config: Configuration dictionary for the model
        messages: List of message dictionaries containing the conversation
        tools: List of tool dictionaries available to the model

    Returns:
        Model response object or stream wrapper

    Raises:
        BadRequestError: If the API request fails
    """
    litellm.OpenAIConfig(**llm_config)
    return await ModelResponse(
        litellm.acompletion(
            model=model,
            messages=messages,
            tools=tools,
        )
    )


if __name__ == "__main__":
    messages = [{"content": "Hello, how are you?", "role": "user"}]

    response = asyncio.run(
        aget_completion(
            model=str(BASE_MODEL.get("name", "gpt-4-mini")),
            llm_config=BASE_MODEL.get("parameters", {}),
            messages=messages,
        )
    )
    if response.choices and response.choices[0].message:
        logger.info(response.choices[0].message.content)
