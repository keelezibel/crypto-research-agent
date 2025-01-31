"""Common Logger module for the research agent application."""

from __future__ import annotations

import logging
import sys


def setup_logger(name: str = "research_agent", level: str = "") -> logging.Logger:
    """Configure and return a logger instance with consistent formatting.

    Args:
    ----
        name: The name of the logger
        level: The logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
                If None, defaults to INFO

    Returns:
    -------
        logging.Logger: Configured logger instance

    """
    # Create logger
    logger = logging.getLogger(name)

    # Set level
    log_level = getattr(logging, (level or "INFO").upper())
    logger.setLevel(log_level)

    # Avoid adding handlers if they already exist
    if not logger.handlers:
        # Create console handler
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(log_level)

        # Create formatter
        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Add formatter to handler
        handler.setFormatter(formatter)

        # Add handler to logger
        logger.addHandler(handler)

    return logger


# Create default logger instance
logger = setup_logger()
