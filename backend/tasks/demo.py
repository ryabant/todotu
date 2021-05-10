from django.contrib.auth import get_user_model
from django.db import transaction

from .models import Board, Task, Tag

User = get_user_model()


@transaction.atomic
def create_demo_board(user):
    tag1 = Tag.objects.create(name="welcome", owner=user)
    board = Board.objects.create(name="Welcome!", owner=user)

    task = Task.objects.create(
        title="Add new tags by clicking the small yellow button", body="Click on small yellow button!", board=board)
    task.tags.set([tag1, ])

    task = Task.objects.create(
        title="Delete board by clicking the small red button", body="Click on small red button!", board=board)
    task.tags.set([tag1, ])

    task = Task.objects.create(
        title="Add a new board by clicking the small blue button", body="Click on small blue button!", board=board)
    task.tags.set([tag1, ])

    task = Task.objects.create(
        title="Click on me!", body="Change task and press save!", board=board)
    task.tags.set([tag1, ])

    task = Task.objects.create(
        title="Add a new task by clicking the big blue button", body="Click on big blue button!", board=board)
    task.tags.set([tag1, ])
