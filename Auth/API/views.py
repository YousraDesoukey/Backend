from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler
from .models import Users
from .serializers import UserSerializer
import services
import requests
from django.contrib.auth.models import User

from django.shortcuts import render


class UserList(APIView):
    def get(self,request):
        users = Users.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                #7ateina hena validated data 3lshan a5od el data 2abl ma a3ml lha save

                match = Users.objects.get(email=serializer.validated_data["email"])
            except Users.DoesNotExist:
                # Unable to find a user, this is fine]
                serializer.save()
                # print ('money here come the money')
                #user must take those arguments
                user = User.objects.create_user(username=serializer.validated_data["email"],
                                                email=serializer.validated_data["email"],
                                                password=serializer.validated_data["password"])

                return Response(serializer.data, status=status.HTTP_201_CREATED)



            else:
                return Response("The Email Already Exists!", status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

