.PHONY: format check test clean

# Format and lint code
format:
	poetry run ruff check --fix .
	poetry run ruff format .

# Check code without modifying
check:
	poetry run ruff check .

# Run tests
test:
	poetry run pytest -v --cov=research_agent tests/
# Install dependencies and pre-commit hooks
setup:
	poetry install
	poetry run pre-commit install

# Run all checks and tests
all: format check test