"""LLM configuration module."""

BASE_MODEL = {
    "name": "openai/gpt-4o-mini",
    "parameters": {
        "temperature": 0.0,
    },
}

VISION_MODEL = {
    "name": "openai/gpt-4o",
}

REASONING_MODEL = {
    "name": "openai/o1-mini",
}
