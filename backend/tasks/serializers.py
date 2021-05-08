from rest_framework import serializers
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

    def to_representation(self, value):
        return f"{value.name}"


class TaskSerializer(serializers.ModelSerializer):
    board = serializers.PrimaryKeyRelatedField(queryset=Board.objects.all())
    tags = TagSerializer(many=True, required=False)

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
        user = self.context["request"].user
        tags_data = validated_data.pop("tags")
        task = Task.objects.create(**validated_data)

        for tag_data in tags_data:
            tag = Tag.objects.create(owner=user, **tag_data)
            task.tags.add(tag)

        return task


class BoardSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, required=False)
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Board
        fields = ["id", "name", "owner", "tasks"]
