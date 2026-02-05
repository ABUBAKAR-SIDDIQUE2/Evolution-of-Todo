# Implementation Plan: Phase I - In-Memory Python Console App

**Branch**: `001-in-memory-python-cli` | **Date**: 2026-02-05 | **Spec**: [specs/001-in-memory-python-cli/spec.md](../spec.md)
**Input**: Feature specification from `/specs/001-in-memory-python-cli/spec.md`

## Summary

Build a minimal, production-style command-line Todo application (Python 3.13+) that stores tasks in memory for the process lifetime. This Phase I implementation focuses on a clean, layered architecture (CLI <-> App <-> Domain) using standard library tools (`argparse`) to ensure zero external dependencies for the runtime, while adhering to strict Spec-Driven Development.

## Technical Context

**Language/Version**: Python 3.13+
**Primary Dependencies**: Standard Library (`argparse`, `logging`, `dataclasses`). Dev: `pytest`, `ruff`/`flake8`.
**Storage**: In-Memory (Python `list`/`dict`). No persistence.
**Testing**: `pytest` (Unit), `subprocess` (CLI Integration). Coverage goal: ≥ 80%.
**Target Platform**: Linux / macOS / Windows (Local CLI)
**Project Type**: Single project (CLI tools)
**Performance Goals**: Instant execution (<100ms) for all commands.
**Constraints**: No file I/O, No databases, No external APIs, Single process.
**Scale/Scope**: Single user, process-lifetime data.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

*   **Principle I (SDD)**: ✅ Plan derived directly from Spec.
*   **Principle II (Tooling)**: ✅ Using Gemini CLI & Spec-Kit.
*   **Principle III (Architecture)**: ✅ Layered architecture defined (CLI/App/Domain).
*   **Principle IV (QA)**: ✅ Test-first strategy with `pytest` and coverage goals defined.
*   **Principle VII (Security)**: ✅ Input validation planned (max lengths, empty checks).
*   **Principle VIII (Phased)**: ✅ strictly Phase I scope (no persistence).

## Project Structure

### Documentation (this feature)

```text
specs/001-in-memory-python-cli/
├── plan.md              # This file
├── research.md          # Technology decisions
├── data-model.md        # Entity definitions
├── quickstart.md        # Run instructions
└── tasks.md             # Implementation tasks
```

### Source Code

```text
src/
├── cli.py               # Entrypoint: Argument parsing & routing (Interface Layer)
├── store.py             # Domain Layer: Task & TaskStore (Business Logic)
├── handlers.py          # Application Layer: Validation & Formatting
└── utils.py             # Shared utilities (Formatting, Time)

tests/
├── conftest.py          # Shared test fixtures
├── unit/
│   └── test_store.py    # Unit tests for TaskStore
└── integration/
    └── test_cli.py      # Integration tests using subprocess
```

**Structure Decision**: Single project structure with explicit layer separation (`cli` vs `store`) to facilitate future migration to backend/frontend split in Phase II.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| Layered Arch (handlers.py) | Separation of Concerns | Putting logic in `cli.py` would make Phase II reuse harder |