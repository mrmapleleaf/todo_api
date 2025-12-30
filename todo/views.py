from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ToDo
from todo.dto.ToDoItem import ToDoItem
from todo.responses.ToDoListResponse import ToDoListResponse
from todo.responses.ToDoResponse import ToDoResponse
from todo.responses.ToDoDetailResponse import ToDoDetailResponse
from todo.forms import ToDoForm
from django.shortcuts import get_object_or_404


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
        form = ToDoForm(request.data)

        print("form:", form)

        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return Response(
                ToDoResponse.create_response(todo), status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                ToDoResponse.error_response("Invalid form data"),
                status=status.HTTP_400_BAD_REQUEST,
            )
    else:
        form = ToDoForm()
    return Response(
        ToDoResponse.error_response("Failed to create ToDo"),
        status=status.HTTP_400_BAD_REQUEST,
    )


@api_view(["GET"])
def getToDoDetail(request, todo_id):
    todo = get_object_or_404(ToDo, id=todo_id)
    return Response(ToDoDetailResponse.create_response(ToDoItem.from_model(todo)))
