from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoItemSerializer
from todo.dto.ToDoItem import ToDoItem
from todo.responses.ToDoListResponse import ToDoListResponse


# Create your views here.
@api_view(["GET"])
def getToDoList(requqest):
    todos = ToDo.objects.all()
    todoItems = [ToDoItem.from_model(todo) for todo in todos]
    ToDoItemResponse = ToDoListResponse(todos=todoItems)

    return Response(ToDoItemResponse.__dict__)
