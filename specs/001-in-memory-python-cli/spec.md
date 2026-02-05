# Feature Specification: Phase I - In-Memory Python Console App

**Feature Branch**: `001-in-memory-python-cli`
**Created**: 2026-02-05
**Status**: Draft
**Input**: User description: "Build a minimal, production-style command-line Todo application (Python 3.13+) that stores tasks in memory..."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add Task (Priority: P1)

As a user, I want to add a task with a title and optional description so I can track it later.

**Why this priority**: Core functionality; without adding tasks, the system has no data to operate on.

**Independent Test**: Can be tested by adding a task and verifying the command succeeds (exit code 0).

**Acceptance Scenarios**:

1. **Given** an empty task store, **When** I run `todo add "Buy apples" --desc "green"`, **Then** exit code is 0 AND `todo list --all` shows a task with title "Buy apples" and completed false.
2. **Given** any task store, **When** I run `todo add "Buy milk"`, **Then** exit code is 0 AND the task is added with an empty description.
3. **Given** any task store, **When** I run `todo add ""` (empty title), **Then** exit code is 1 AND an error message is displayed.

---

### User Story 2 - View Task List (Priority: P1)

As a user, I want to list all tasks and see their id, title, short description, created time, and completion status.

**Why this priority**: Essential for visibility; users need to see what they have tracked.

**Independent Test**: Can be tested by adding sample tasks and verifying the list output contains them.

**Acceptance Scenarios**:

1. **Given** 3 tasks (1 complete, 2 pending), **When** I run `todo list --pending`, **Then** only the 2 pending tasks are listed.
2. **Given** 3 tasks (1 complete, 2 pending), **When** I run `todo list --all`, **Then** all 3 tasks are listed.
3. **Given** 3 tasks (1 complete, 2 pending), **When** I run `todo list --completed`, **Then** only the 1 completed task is listed.
4. **Given** no tasks, **When** I run `todo list`, **Then** an empty table (or "No tasks found") message is displayed.

---

### User Story 3 - Update Task (Priority: P2)

As a user, I want to update a task's title and/or description by task id.

**Why this priority**: Allows correction and refinement of tasks.

**Independent Test**: Can be tested by creating a task, updating it, and verifying the changes persist.

**Acceptance Scenarios**:

1. **Given** a task with id 2 and title "Old", **When** I run `todo update 2 --title "New"`, **Then** `todo list --all` shows id 2 with title "New".
2. **Given** a task with id 2, **When** I run `todo update 2 --desc "New Desc"`, **Then** the description is updated while the title remains unchanged.
3. **Given** no task with id 99, **When** I run `todo update 99 --title "Ghost"`, **Then** exit code is 1 AND a "Task not found" error is displayed.

---

### User Story 4 - Delete Task (Priority: P2)

As a user, I want to delete a task by id.

**Why this priority**: Users need to remove erroneous or obsolete tasks.

**Independent Test**: Can be tested by creating a task, deleting it, and verifying it is gone.

**Acceptance Scenarios**:

1. **Given** a task with id 5, **When** I run `todo delete 5`, **Then** `todo list --all` does not include id 5.
2. **Given** no task with id 99, **When** I run `todo delete 99`, **Then** exit code is 1 AND a "Task not found" error is displayed.

---

### User Story 5 - Toggle Complete (Priority: P2)

As a user, I want to mark a task complete or incomplete by id.

**Why this priority**: Core workflow; marks the "doing" of the todo item.

**Independent Test**: Can be tested by toggling a task and checking its status in the list.

**Acceptance Scenarios**:

1. **Given** task id 3 is pending, **When** I run `todo toggle 3`, **Then** task id 3 is completed.
2. **Given** task id 3 is completed, **When** I run `todo toggle 3`, **Then** task id 3 is pending.
3. **Given** no task with id 99, **When** I run `todo toggle 99`, **Then** exit code is 1 AND a "Task not found" error is displayed.

---

### Edge Cases

- **Duplicate Titles**: System ALLOWS tasks with identical titles (IDs distinguish them).
- **Max Length**:
    - Title > 250 chars: Should be truncated or rejected (Goal: Rejected with error).
    - Description > 2000 chars: Should be truncated or rejected (Goal: Rejected with error).
- **Concurrency**: Not applicable for Phase I (single process, in-memory).
- **Persistence**: Data is lost when the process exits (Design constraint).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide a CLI entrypoint `src/cli.py` executable via `python -m todo_cli`.
- **FR-002**: System MUST store tasks in-memory for the duration of the process.
- **FR-003**: System MUST support `add`, `list`, `update`, `delete`, and `toggle` commands.
- **FR-004**: System MUST output list results in a human-readable table format by default.
- **FR-005**: System MUST support a `--json` flag for `list` command to output machine-parsable JSON.
- **FR-006**: System MUST return exit code 0 for success, 1 for user error, and 2 for internal error.
- **FR-007**: System MUST validate input (non-empty title, max lengths).

### Key Entities

- **Task**:
    - `id` (int, auto-increment unique)
    - `title` (str, max 250)
    - `description` (str, optional, max 2000)
    - `completed` (bool, default False)
    - `created_at` (datetime, UTC)
    - `updated_at` (datetime, UTC)

- **TaskStore**:
    - Manages the in-memory dictionary/list of Tasks.
    - Handles ID generation.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Users can perform all 5 basic operations (Add, List, Update, Delete, Toggle) via CLI commands.
- **SC-002**: CLI commands execute instantly (<100ms) for typical usage.
- **SC-003**: 100% of functional requirements are verifiable via automated integration tests.
- **SC-004**: Codebase achieves minimum 80% test coverage (unit + integration).
- **SC-005**: CLI provides helpful error messages for invalid inputs (no stack traces users).