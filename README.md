# Evolution of Todo - Phase I (CLI)

A minimal, production-style in-memory Todo application built with Python 3.13+.

## Features

- **Add Task**: Add a task with a title and optional description.
- **List Tasks**: View tasks in a tabular or JSON format with filtering (all, pending, completed).
- **Update Task**: Update the title and/or description of an existing task.
- **Delete Task**: Remove a task by its ID.
- **Toggle Status**: Mark a task as completed or pending.

## Prerequisites

- Python 3.13+

## Installation

1.  Clone the repository.
2.  Install development dependencies (optional, for testing and linting):
    ```bash
    pip install .[dev]
    ```

## Usage

Run the application using `python -m src.cli`.

### Commands

- **Add a task**:
  ```bash
  python -m src.cli add "Buy groceries" --desc "Milk, eggs, bread"
  ```
- **List tasks**:
  ```bash
  # List pending tasks (default)
  python -m src.cli list
  
  # List all tasks
  python -m src.cli list --all
  
  # List in JSON format
  python -m src.cli list --all --json
  ```
- **Update a task**:
  ```bash
  python -m src.cli update 1 --title "Buy organic milk"
  ```
- **Delete a task**:
  ```bash
  python -m src.cli delete 1
  ```
- **Toggle task status**:
  ```bash
  python -m src.cli toggle 1
  ```

## Running Tests

All logic is verified using `pytest`.

```bash
python -m pytest
```

## Architecture

The project follows a layered architecture to ensure separation of concerns:
- **Interface Layer (`cli.py`)**: Handles argument parsing and user input/output using `argparse`.
- **Application Layer (`handlers.py`)**: Orchestrates the flow between the CLI and the domain logic.
- **Domain Layer (`store.py`)**: Contains the core business logic and in-memory data structures.
- **Utilities (`utils.py`)**: Provides shared formatting and helper functions.

## Limitations (Phase I)

- **In-Memory Only**: Data persists only for the duration of the process. In-process integration tests are used to verify multi-command logic.
- **Single Process**: No multi-user support or remote API access.
