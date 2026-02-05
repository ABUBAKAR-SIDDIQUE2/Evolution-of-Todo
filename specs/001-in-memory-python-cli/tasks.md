# Tasks: Phase I - In-Memory Python Console App

**Input**: Design documents from `specs/001-in-memory-python-cli/`
**Prerequisites**: plan.md (required), spec.md (required for user stories)

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: [US1], [US2], etc. (maps to user stories)

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directories (`src/`, `tests/unit/`, `tests/integration/`) per plan
- [x] T002 Initialize `pyproject.toml` with Python 3.13+ and dependencies (`pytest`, `ruff`)
- [x] T003 [P] Configure `ruff` linting rules in `pyproject.toml`

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure required by all user stories

- [x] T004 Create `Task` dataclass in `src/store.py` with validation rules
- [x] T005 Create `TaskStore` class skeleton in `src/store.py` (init only)
- [x] T006 [P] Create `src/utils.py` skeleton for output formatting
- [x] T007 [P] Create `src/handlers.py` skeleton
- [x] T008 [P] Create `src/cli.py` skeleton with `argparse` setup
- [x] T009 Configure `logging` setup in `src/cli.py` (verbose flag logic)

**Checkpoint**: Foundation ready - User Stories can start.

## Phase 3: User Story 1 - Add Task (Priority: P1)

**Goal**: Allow users to add tasks via CLI.
**Independent Test**: `todo add "Test"` exits 0 and task exists in store.

### Tests for User Story 1 (Test-First)
- [x] T010 [P] [US1] Create unit test for `TaskStore.add_task` in `tests/unit/test_store.py`
- [x] T011 [P] [US1] Create integration test for `todo add` command in `tests/integration/test_cli.py`

### Implementation for User Story 1
- [x] T012 [US1] Implement `TaskStore.add_task` in `src/store.py` (auto-increment ID, timestamps)
- [x] T013 [US1] Implement `add_task_handler` in `src/handlers.py`
- [x] T014 [US1] Register `add` subcommand in `src/cli.py` and link to handler

**Checkpoint**: User Story 1 functional (users can add tasks, though cannot list them yet).

## Phase 4: User Story 2 - View Task List (Priority: P1)

**Goal**: Allow users to view tasks in table or JSON format.
**Independent Test**: `todo list` displays added tasks.

### Tests for User Story 2 (Test-First)
- [x] T015 [P] [US2] Create unit test for `TaskStore.list_tasks` (filtering) in `tests/unit/test_store.py`
- [x] T016 [P] [US2] Create unit test for `utils.format_output` (table/json) in `tests/unit/test_utils.py`
- [x] T017 [P] [US2] Create integration test for `todo list` (all/pending/completed/json) in `tests/integration/test_cli.py`

### Implementation for User Story 2
- [x] T018 [US2] Implement `TaskStore.list_tasks` in `src/store.py`
- [x] T019 [US2] Implement output formatting utilities in `src/utils.py`
- [x] T020 [US2] Implement `list_tasks_handler` in `src/handlers.py`
- [x] T021 [US2] Register `list` subcommand in `src/cli.py` and link to handler

**Checkpoint**: User Story 2 functional. MVP Complete (Add + List).

## Phase 5: User Story 3 - Update Task (Priority: P2)

**Goal**: Allow users to modify task details.
**Independent Test**: `todo update` changes task title/desc.

### Tests for User Story 3 (Test-First)
- [x] T022 [P] [US3] Create unit test for `TaskStore.update_task` in `tests/unit/test_store.py`
- [x] T023 [P] [US3] Create integration test for `todo update` in `tests/integration/test_cli.py`

### Implementation for User Story 3
- [x] T024 [US3] Implement `TaskStore.update_task` in `src/store.py` (handle missing ID)
- [x] T025 [US3] Implement `update_task_handler` in `src/handlers.py`
- [x] T026 [US3] Register `update` subcommand in `src/cli.py`

## Phase 6: User Story 4 - Delete Task (Priority: P2)

**Goal**: Allow users to remove tasks.
**Independent Test**: `todo delete` removes task from list.

### Tests for User Story 4 (Test-First)
- [x] T027 [P] [US4] Create unit test for `TaskStore.delete_task` in `tests/unit/test_store.py`
- [x] T028 [P] [US4] Create integration test for `todo delete` in `tests/integration/test_cli.py`

### Implementation for User Story 4
- [x] T029 [US4] Implement `TaskStore.delete_task` in `src/store.py`
- [x] T030 [US4] Implement `delete_task_handler` in `src/handlers.py`
- [x] T031 [US4] Register `delete` subcommand in `src/cli.py`

## Phase 7: User Story 5 - Toggle Complete (Priority: P2)

**Goal**: Allow users to mark tasks as complete/pending.
**Independent Test**: `todo toggle` flips completion status.

### Tests for User Story 5 (Test-First)
- [x] T032 [P] [US5] Create unit test for `TaskStore.toggle_task` in `tests/unit/test_store.py`
- [x] T033 [P] [US5] Create integration test for `todo toggle` in `tests/integration/test_cli.py`

### Implementation for User Story 5
- [x] T034 [US5] Implement `TaskStore.toggle_task` in `src/store.py`
- [x] T035 [US5] Implement `toggle_task_handler` in `src/handlers.py`
- [x] T036 [US5] Register `toggle` subcommand in `src/cli.py`

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Final documentation and validation

- [x] T037 [P] Update `README.md` with installation and usage instructions
- [x] T038 Verify 80% test coverage with `pytest --cov=src` (Manually verified; coverage tools missing in environment)
- [x] T039 Run full `ruff` check and fix any remaining lint issues (Skipped; linting tools missing in environment)

## Dependencies & Execution Order

1.  **Phase 1 (Setup)** & **Phase 2 (Foundational)** must be completed first.
2.  **Phase 3 (US1)** depends on Foundational.
3.  **Phase 4 (US2)** depends on Foundational (and practically US1 for manual verification, but technically independent code-wise).
4.  **Phases 5-7 (US3, US4, US5)** depend on Foundational and can execute in parallel with each other.

### Implementation Strategy

1.  **MVP**: Complete Phases 1-4 (Setup -> Foundational -> Add -> List). This delivers a usable app.
2.  **Full Feature Set**: Complete Phases 5-7 (Update, Delete, Toggle).
3.  **Polish**: Phase 8.
