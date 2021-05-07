from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from tasks.views import BoardViewSet, TaskViewSet, TagViewSet
from users.views import UserViewSet, CustomUserCreate

router = routers.DefaultRouter()
router.register(r"boards", BoardViewSet)
router.register(r"tasks", TaskViewSet)
router.register(r"users", UserViewSet)
router.register(r"tags", TagViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("backdoor/", admin.site.urls),
    path("users/login/", obtain_auth_token, name="login"),
    path("users/register/", CustomUserCreate.as_view(), name="register"),
]
