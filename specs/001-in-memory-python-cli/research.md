# Research & Decisions: Phase I - In-Memory Python Console App

**Feature**: Phase I In-Memory CLI
**Date**: 2026-02-05

## Decision 1: CLI Framework - `argparse`

### Context
We need a command-line interface to expose the Todo functionality. The hackathon rules emphasize "production-style" but also "minimal boilerplate".

### Options Considered
1.  **`argparse` (Selected)**: Python Standard Library.
2.  **`click`**: External dependency, very popular, clean API.
3.  **`typer`**: External dependency, type-hint based, modern.

### Rationale
Selected `argparse` because:
*   **Zero Dependency**: Simplifies distribution and setup for Phase I.
*   **Standard**: Every Python developer knows it or has it available.
*   **Sufficiency**: The requirement (subcommands `add`, `list`, etc.) is easily handled by `argparse` subparsers.
*   **Testability**: Can be tested via `subprocess` or by passing explicit args list to `parse_args()`.

## Decision 2: In-Memory Storage Strategy

### Context
Phase I explicitly forbids persistence. We need a way to store tasks during the process lifetime.

### Options Considered
1.  **Global List/Dict**: Simple global variable.
2.  **Singleton `TaskStore` Class (Selected)**: Encapsulated state.

### Rationale
Selected `TaskStore` class because:
*   **Encapsulation**: Hides implementation details (list vs dict) from the CLI.
*   **Testability**: We can instantiate a fresh `TaskStore` for every test, avoiding shared state issues common with globals.
*   **Future Proofing**: Easier to swap the internal list for a DB connection in Phase II (though Phase II will likely be a separate API service, the *pattern* holds).

## Decision 3: Layered Architecture (CLI vs Store vs Handlers)

### Context
How to organize the code within `src/`.

### Options Considered
1.  **Monolithic `cli.py`**: All logic inside command functions.
2.  **Layered (Selected)**: `cli.py` (Interface) -> `handlers.py` (App) -> `store.py` (Domain).

### Rationale
Selected Layered Architecture because:
*   **Reuse**: The "Domain" (`store.py`) and "App" logic can theoretically be imported by a FastAPI backend in Phase II (or at least serve as a clean reference).
*   **Testing**: Domain logic can be unit tested without mocking CLI args.
*   **Clarity**: Distinct separation between "parsing user input" and "doing the work".
