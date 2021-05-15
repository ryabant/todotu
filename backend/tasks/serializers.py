from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Board, Task, Tag


class TagSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())

    def extra_validation(self, board=None, user=None, tags=None):
        if user != board.owner:
            raise serializers.ValidationError("Must be a owner of the board!")

    def create(self, validated_data):
        user = self.context["request"].user
        board = validated_data.get("board")
        self.extra_validation(board=board, user=user)
        return super().create(validated_data)

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
        queryset=Board.objects.all(), required=False, default=None)
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True, required=False)
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

    def extra_validation(self, board=None, user=None, tags=None):
        if tags and board:
            for tag in tags:
                if tag not in board:
                    raise serializers.ValidationError(
                        "Can't set a tag that doesn't belong to the board!")
        if board and user != board.owner:
            raise serializers.ValidationError(
                "Must be a owner of the board!")

    def update(self, instance, validated_data):
        user = self.context["request"].user
        tags = validated_data.get("tags")
        board = instance.board
        self.extra_validation(board=board, user=user, tags=tags)
        return super().update(instance, validated_data)

    def create(self, validated_data):
        user = self.context["request"].user
        board = validated_data["board"]
        tags = validated_data["tags"]
        self.extra_validation(board=board, user=user, tags=tags)
        return super().create(validated_data)


class BoardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Board
        fields = ["id", "name", "owner", "tasks"]
