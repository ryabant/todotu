from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Board, Task
from .serializers import BoardSerializer, TaskSerializer
from .permissions import IsOwner


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset().filter(owner=user)
        return qs

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, ]
