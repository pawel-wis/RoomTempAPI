from django.shortcuts import render
from .models import Roomtemp
from .serializers import RoomtempSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class RoomtempViewSet(ModelViewSet):
    queryset = Roomtemp.objects.all()
    serializer_class = RoomtempSerializer

    def create(self, request, *args, **kwargs):
        err_msg = {'error': ''}
        if "temperature" in request.data.keys() and "humidity" in request.data.keys():
            if "secret" in request.data.keys():
                secret = request.data['secret']
                if secret != '1234':
                    err_msg['error'] = 'Wrong sercret'
                    return Response(err_msg, status=status.HTTP_401_UNAUTHORIZED)
                
                tmp = float(request.data['temperature'])
                hum = int(request.data['humidity'])
                new_room_temp = Roomtemp(temperature=tmp, humidity=hum)
                new_room_temp.save()
                return Response(new_room_temp, status=status.HTTP_201_CREATED)
        else:
            err_msg['error'] = 'Wrong request'
            return Response(err_msg, status=status.HTTP_400_BAD_REQUEST)
