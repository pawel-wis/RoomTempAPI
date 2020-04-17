from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from rest_framework import routers
from .views import RoomtempViewSet

router = routers.DefaultRouter()
router.register('room', RoomtempViewSet)

urlpatterns = [
    path('', include(router.urls)),
]