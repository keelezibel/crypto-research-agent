"""Research Agent package initialization."""

from research_agent.logger import setup_logger
from research_agent.settings import settings

# Configure logger with settings
logger = setup_logger(level=settings.log_level)
