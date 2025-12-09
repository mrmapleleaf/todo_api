from dataclasses import dataclass
from datetime import datetime


@dataclass
class ToDoItem:
    id: int
    title: str
    is_completed: bool
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_model(todo):
        return ToDoItem(
            id=todo.id,
            title=todo.title,
            is_completed=todo.is_completed,
            created_at=todo.created_at,
            updated_at=todo.updated_at,
        )
