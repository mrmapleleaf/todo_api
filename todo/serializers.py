from rest_framework import serializers
from .models import ToDo


class ToDoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = "__all__"
