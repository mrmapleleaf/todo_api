from dataclasses import dataclass
from todo.dto.ToDoItem import ToDoItem


@dataclass
class ToDoListResponse:
    todos: list[ToDoItem]
