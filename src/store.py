from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Optional, List

@dataclass
class Task:
    id: int
    title: str
    created_at: datetime
    updated_at: datetime
    description: Optional[str] = None
    completed: bool = False

    def __post_init__(self):
        if not self.title or not self.title.strip():
            raise ValueError("Title must not be empty")
        if len(self.title) > 250:
             raise ValueError("Title must be at most 250 characters")
        if self.description and len(self.description) > 2000:
            raise ValueError("Description must be at most 2000 characters")

class TaskStore:
    def __init__(self):
        self._tasks: dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        now = datetime.now(timezone.utc)
        task = Task(
            id=self._next_id,
            title=title,
            description=description,
            created_at=now,
            updated_at=now
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def list_tasks(self, status: str = "pending") -> List[Task]:
        all_tasks = list(self._tasks.values())
        if status == "all":
            return all_tasks
        elif status == "completed":
            return [t for t in all_tasks if t.completed]
        elif status == "pending":
            return [t for t in all_tasks if not t.completed]
        return all_tasks

    def update_task(self, id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        if id not in self._tasks:
            raise ValueError(f"Task not found: {id}")
        
        task = self._tasks[id]
        if title is not None:
            if not title or not title.strip():
                 raise ValueError("Title must not be empty")
            if len(title) > 250:
                 raise ValueError("Title must be at most 250 characters")
            task.title = title
            
        if description is not None:
            if len(description) > 2000:
                raise ValueError("Description must be at most 2000 characters")
            task.description = description
            
        task.updated_at = datetime.now(timezone.utc)
        return task

    def delete_task(self, id: int) -> Task:
        if id not in self._tasks:
            raise ValueError(f"Task not found: {id}")
        return self._tasks.pop(id)

    def toggle_task(self, id: int) -> Task:
        if id not in self._tasks:
            raise ValueError(f"Task not found: {id}")
        
        task = self._tasks[id]
        task.completed = not task.completed
        task.updated_at = datetime.now(timezone.utc)
        return task
