from django.urls import path
from .views import getToDoList, createToDo, getToDoDetail

urlpatterns = [
    path("todos/", getToDoList, name="getToDoList"),
    path("todo/create/", createToDo, name="createToDo"),
    path("todo/<int:todo_id>", getToDoDetail, name="getToDoDetail"),
]
