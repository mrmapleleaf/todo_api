from todo.dto.ToDoItem import ToDoItem


class ToDoDetailResponse:

    todo: ToDoItem

    @staticmethod
    def create_response(todo):
        return {"todo": todo}
