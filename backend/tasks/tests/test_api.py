import pytest
from django.contrib.auth import get_user_model
from rest_framework.reverse import reverse

from tasks.models import Board, Task, Tag

User = get_user_model()


# @pytest.fixture
def test_board(create_user):
    user = create_user()
    uni_board = Board.objects.create(name="University", owner=user)
    return uni_board


def test_board_create(api_client, create_user):
    assert len(Board.objects.all()) == 0

    def create_board():
        return api_client.post(reverse("board-list"), {"name": "Movies"})

    # Not authenticated
    response = create_board()
    assert response.status_code == 401
    assert len(Board.objects.all()) == 0

    # User1 should be owner after creation
    user1 = create_user()
    api_client.force_authenticate(user=user1)
    response = create_board()
    assert response.status_code == 201
    assert len(Board.objects.all()) == 1
    movies = Board.objects.get(name="Movies")
    assert movies.owner == user1

    # # User2 should not see any boards
    user2 = create_user()
    api_client.force_authenticate(user=user2)
    response = api_client.get(reverse("board-list"))
    assert response.status_code == 200
    assert len(response.data) == 0


def test_board_delete(api_client, create_user):
    user1 = create_user()
    uni_board = Board.objects.create(name="Music", owner=user1)

    def delete_uni_board():
        return api_client.delete(reverse("board-detail", kwargs={"pk": uni_board.id}))

    # Not authenticated
    response = delete_uni_board()
    assert response.status_code == 401
    assert Board.objects.filter(id=uni_board.id).exists()

    # Not owner can't delete board
    user2 = create_user()
    api_client.force_authenticate(user=user2)
    response = delete_uni_board()
    assert response.status_code == 404
    assert Board.objects.filter(id=uni_board.id).exists()

    # Owner can delete his own board
    api_client.force_authenticate(user=user1)
    response = delete_uni_board()
    assert response.status_code == 204
    assert not Board.objects.filter(id=uni_board.id).exists()
