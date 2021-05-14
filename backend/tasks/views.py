from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Board, Task, Tag
from .serializers import BoardSerializer, TaskSerializer, TagSerializer
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
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=False)
    def inbox(self, request):
        inbox_tasks = super().get_queryset().filter(inbox=True)
        serializer = self.get_serializer(inbox_tasks, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def important(self, request):
        inbox_tasks = super().get_queryset().filter(important=True)
        serializer = self.get_serializer(inbox_tasks, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [
        IsAuthenticated,
    ]
