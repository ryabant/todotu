from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Board(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="boards")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name="tags")

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name", "board"], name="unique_name_board")
        ]


class Priority(models.TextChoices):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    board = models.ForeignKey(
        Board, on_delete=models.CASCADE, related_name="tasks", blank=True)
    priority = models.CharField(
        max_length=10, choices=Priority.choices, default=Priority.MEDIUM
    )
    tags = models.ManyToManyField(Tag, related_name="tasks", blank=True)
    created = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    inbox = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="tasks")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title
