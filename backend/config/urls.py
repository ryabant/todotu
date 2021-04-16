from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from tasks.views import BoardViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r"boards", BoardViewSet)
router.register(r"tasks", TaskViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
]
