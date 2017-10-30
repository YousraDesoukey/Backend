from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler
from .models import UserSocial
from .serializers import AuthSerializer
from rest_framework_jwt.settings import api_settings

# import services
import requests
from django.contrib.auth.models import User

from django.shortcuts import render


class UserSocialList(APIView):
    def get(self,request):
        users = UserSocial.objects.all()
        serializer = AuthSerializer(users,many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer = AuthSerializer(data=request.data)
        if serializer.is_valid():
            try:
                #7ateina hena validated data 3lshan a5od el data 2abl ma a3ml lha save

                match = UserSocial.objects.get(email=serializer.validated_data["email"])
            except UserSocial.DoesNotExist:
                # Unable to find a user, this is fine]
                serializer.save()
                # print ('money here come the money')
                #user must take those arguments
                user = User.objects.create_user(username=serializer.validated_data["email"],
                                                email=serializer.validated_data["email"],
                                               )
                # user.password.valid=True
                # print(user.objects.get())

                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)

                dict={"token":token}
                # dict=dict+{"token":token}
                # print(dict)

                return Response(dict, status=status.HTTP_201_CREATED)
                # return Response(dict, status=status.HTTP_201_CREATED)



            else:
                return Response("The facebook account already Exists!", status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

