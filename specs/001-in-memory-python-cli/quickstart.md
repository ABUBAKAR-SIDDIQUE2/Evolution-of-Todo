# Quickstart: Phase I - In-Memory Python Console App

## Prerequisites

*   Python 3.13+
*   `pip` (to install dev dependencies)

## Installation

1.  Clone the repository.
2.  Install dependencies (for testing/linting):
    ```bash
    pip install -r requirements.txt
    # OR if using pyproject.toml
    pip install .[dev]
    ```

## Running the CLI

The CLI is located in `src/cli.py`. You can run it directly:

```bash
# Add a task
python -m src.cli add "Buy milk"

# List tasks
python -m src.cli list

# Run via module (if installed)
python -m todo_cli list
```

## Running Tests

We use `pytest` for all tests.

```bash
# Run all tests
pytest

# Run only integration tests
pytest tests/integration

# Run only unit tests
pytest tests/unit

# Check coverage
pytest --cov=src
```

## Development Workflow

1.  Create a spec/feature branch.
2.  Write tests first (TDD).
3.  Implement functionality in `store.py` then `cli.py`.
4.  Run `ruff check .` to ensure code style.
