from django.contrib.auth import get_user_model
from django.db import transaction

from .models import Board, Task

User = get_user_model()


@transaction.atomic
def create_demo_board(user):
    board = Board.objects.create(name="Demo", owner=user)
    task = Task.objects.create(title="Test 1", board=board)
    task = Task.objects.create(title="Test 2", board=board)
