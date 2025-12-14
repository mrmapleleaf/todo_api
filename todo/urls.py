from django.urls import path
from .views import getToDoList, createToDo

urlpatterns = [
    path("todos/", getToDoList, name="getToDoList"),
    path("todo/create/", createToDo, name="createToDo"),
]
