# Data Model: Phase I - In-Memory Python Console App

## Entities

### Task

Represents a single todo item.

| Field | Type | Required | Default | Constraints | Description |
|-------|------|----------|---------|-------------|-------------|
| `id` | `int` | Yes | Auto-gen | Unique, > 0 | Unique identifier |
| `title` | `str` | Yes | - | Max 250 chars, Non-empty | Short summary of the task |
| `description` | `str` | No | `None` | Max 2000 chars | Detailed notes |
| `completed` | `bool` | Yes | `False` | - | Completion status |
| `created_at` | `datetime` | Yes | Now (UTC) | - | Timestamp of creation |
| `updated_at` | `datetime` | Yes | Now (UTC) | - | Timestamp of last update |

**Python Definition (Draft)**:
```python
@dataclass
class Task:
    id: int
    title: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    completed: bool = False
```

## Validation Rules

1.  **Title**: Must not be empty or whitespace only. Truncate or reject if > 250 chars (Reject preferred per Spec).
2.  **Description**: Truncate or reject if > 2000 chars (Reject preferred per Spec).
3.  **IDs**: Auto-incrementing integer starting at 1. Unique within the process lifetime.

## State Transitions

*   **Pending -> Completed**: via `toggle` command.
*   **Completed -> Pending**: via `toggle` command.
