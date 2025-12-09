from django.urls import path
from .views import getToDoList

urlpatterns = [path("todos/", getToDoList, name="getToDoList")]
