from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Board, Task, Tag


class TagSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    def update(self, instance, validated_data):
        try:
            return super().update(instance, validated_data)
        except IntegrityError:
            raise ValidationError("Tag already exists")

    class Meta:
        model = Tag
        fields = ["id", "name", "owner"]


class TaskSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(), slug_field="name", many=True, required=False
    )

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
            "completed",
        ]

    def create(self, validated_data):
        tags = validated_data["tags"]
        return super().create(validated_data)


class BoardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Board
        fields = ["id", "name", "owner", "tasks"]
