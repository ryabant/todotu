from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Board, Task, Tag


class TagSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    def update(self, instance, validated_data):
        try:
            return super().update(instance, validated_data)
        except IntegrityError:
            raise ValidationError("Tag already exists")

    class Meta:
        model = Tag
        fields = ["id", "name", "board"]


class TaskSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(
        queryset=Board.objects.all(), required=False)
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(), slug_field="name", many=True, required=False
    )
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "body",
            "board",
            "priority",
            "tags",
            "created",
            "important",
            "inbox",
            "completed",
            "owner"
        ]

    def extra_validation(self, board=None, user=None):
        if user != board.owner:
            raise serializers.ValidationError("Must be a owner of the board!")

    def create(self, validated_data):
        user = self.context["request"].user
        board = validated_data.get("board")
        self.extra_validation(board=board, user=user)
        return super().create(validated_data)


class BoardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Board
        fields = ["id", "name", "owner", "tasks"]
