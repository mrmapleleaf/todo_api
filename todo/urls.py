from django.urls import path
from .views import getToDoList, createToDo, getToDoDetail

urlpatterns = [
    path("todos", getToDoList, name="getToDoList"),
    path("todo/create", createToDo, name="createToDo"),
    # URLパターンとView関数のパラメータ名は同じである必要がある
    path("todo/<int:todo_id>", getToDoDetail, name="getToDoDetail"),
]
