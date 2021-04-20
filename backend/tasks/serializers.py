from rest_framework import serializers
from .models import Board, Task


class TaskSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    class Meta:
        model = Task
        fields = ["id", "body", "board", "created", "completed"]


class BoardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Board
        fields = ["id", "name", "owner", "tasks"]
