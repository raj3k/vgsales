from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet, GameViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'games', GameViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
