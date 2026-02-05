# CLI Interface Contract

This document defines the user-facing contract for the `todo` CLI.

## Global Flags

*   `--verbose` / `-v`: Enable debug logging (printed to stderr).

## Commands

### 1. Add Task
*   **Usage**: `todo add <title> [--desc <description>]`
*   **Arguments**:
    *   `title` (Positional): The task title. Required.
    *   `--desc` (Optional): The task description.
*   **Output (Success)**: `Task added: [ID] <Title>`
*   **Exit Code**: 0

### 2. List Tasks
*   **Usage**: `todo list [--all | --pending | --completed] [--json]`
*   **Flags**:
    *   `--all`: Show all tasks.
    *   `--pending`: Show only pending (default).
    *   `--completed`: Show only completed.
    *   `--json`: Output raw JSON instead of table.
*   **Output (Success - Table)**:
    ```
    ID  | Title       | Status    | Created
    ----|-------------|-----------|---------------------
    1   | Buy milk    | Pending   | 2026-02-05 10:00:00
    2   | Call mom    | Completed | 2026-02-05 11:00:00
    ```
*   **Output (Success - JSON)**:
    ```json
    [{"id": 1, "title": "Buy milk", "completed": false, ...}]
    ```
*   **Exit Code**: 0

### 3. Update Task
*   **Usage**: `todo update <id> [--title <new_title>] [--desc <new_desc>]`
*   **Arguments**:
    *   `id`: Task ID.
    *   `--title`: New title.
    *   `--desc`: New description.
*   **Output (Success)**: `Task [ID] updated.`
*   **Exit Code**: 0
*   **Errors**: "Task not found" (Exit 1).

### 4. Delete Task
*   **Usage**: `todo delete <id>`
*   **Arguments**:
    *   `id`: Task ID.
*   **Output (Success)**: `Task [ID] deleted.`
*   **Exit Code**: 0
*   **Errors**: "Task not found" (Exit 1).

### 5. Toggle Task
*   **Usage**: `todo toggle <id>`
*   **Arguments**:
    *   `id`: Task ID.
*   **Output (Success)**: `Task [ID] marked as [Completed|Pending].`
*   **Exit Code**: 0
*   **Errors**: "Task not found" (Exit 1).
