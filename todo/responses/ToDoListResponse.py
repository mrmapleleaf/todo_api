from dataclasses import dataclass
from todo.dto.ToDoItem import ToDoItem


@dataclass
class ToDoListResponse:
    todos: list[ToDoItem]

    @staticmethod
    def create_response(todos: list[ToDoItem]):
        return {"todos": [todo for todo in todos]}
