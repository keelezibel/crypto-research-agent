"""Configuration settings module for the research agent application.

This module provides centralized configuration management using Pydantic settings,
handling API keys, logging configuration, and other application settings loaded
from environment variables.
"""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the parent directory of the current file
ENV_PATH = Path(__file__).parent.parent / ".env"
# Common model config
common_config = SettingsConfigDict(
    env_file=ENV_PATH,
    env_file_encoding="utf-8",
)


class Settings(BaseSettings):
    """Main settings class that handles all configuration parameters.

    This class uses Pydantic's BaseSettings to load and validate configuration
    from environment variables and .env files.
    """

    model_config = common_config
    # OpenAI settings
    openai_api_key: str = Field(default="", alias="OPENAI_API_KEY")
    # Anthropic settings
    anthropic_api_key: str = Field(default="", alias="ANTHROPIC_API_KEY")
    # Logging settings
    log_level: str = Field(default="INFO", alias="LOG_LEVEL")


# Create a single settings instance
settings = Settings()


class OpenAISettings:
    """Settings class for OpenAI-specific configuration."""

    @property
    def api_key(self) -> str:
        """Get the OpenAI API key.

        Returns
        -------
            str: The OpenAI API key from settings.

        """
        return settings.openai_api_key


class AnthropicSettings:
    """Settings class for Anthropic-specific configuration."""

    @property
    def api_key(self) -> str:
        """Get the Anthropic API key.

        Returns
        -------
            str: The Anthropic API key from settings.

        """
        return settings.anthropic_api_key


class LoggerSettings:
    """Settings class for logging configuration."""

    @property
    def level(self) -> str:
        """Get the logging level.

        Returns
        -------
            str: The configured logging level from settings.

        """
        return settings.log_level
