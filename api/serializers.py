from rest_framework import serializers
from .models import Roomtemp

class RoomtempSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roomtemp
        fields = ['id', 'temperature', 'humidity']
