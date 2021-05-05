from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, RegistrationSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class UserViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAuthenticated]


@api_view(
    [
        "POST",
    ]
)
def registration_view(request):
    if request.method == "POST":
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data["username"] = user.username
            token = Token.objects.get(user=user).key
            data["token"] = token
        else:
            data = serializer.errors
    return Response(data)
