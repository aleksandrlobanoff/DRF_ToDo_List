from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .apps import TasksConfig
from .views import TaskViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)

app_name = TasksConfig.name

urlpatterns = [
    path('api/', include(router.urls)),
]
