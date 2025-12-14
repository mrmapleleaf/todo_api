from dataclasses import dataclass


@dataclass
class ToDoResponse:
    id: int
    message: str

    @staticmethod
    # DBから取得したToDoモデルをDTOに変換するメソッド
    def from_model(todo):
        return {
            "id": todo.id,
            "message": "ToDo created successfully",
        }

    @staticmethod
    def error_response(message: str):
        return {
            "id": None,
            "message": message,
        }
