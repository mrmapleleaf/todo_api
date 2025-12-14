from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ToDo
from todo.dto.ToDoItem import ToDoItem
from todo.responses.ToDoListResponse import ToDoListResponse
from todo.responses.ToDoResponse import ToDoResponse
from todo.forms import ToDoForm


# Create your views here.
@api_view(["GET"])
def getToDoList(requqest):
    todos = ToDo.objects.all()
    todoItems = [ToDoItem.from_model(todo) for todo in todos]
    ToDoItemResponse = ToDoListResponse.create_response(todos=todoItems)

    return Response(ToDoItemResponse)


@api_view(["POST"])
def createToDo(request):
    if request.method == "POST":
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return Response(ToDoResponse.from_model(todo))
        else:
            return Response(ToDoResponse.error_response("Invalid form data"))
    else:
        form = ToDoForm()
    return Response(ToDoResponse.error_response("Failed to create ToDo"))
