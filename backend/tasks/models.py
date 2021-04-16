from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Board(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name="boards")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Task(models.Model):
    body = models.TextField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name="tasks")
    created = models.DateTimeField(default=timezone.now)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.body
