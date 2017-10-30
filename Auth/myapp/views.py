# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import LoginSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Users
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings


class UserList2(APIView):

    def get(self, request):
        users = Users.objects.all()
        Serializer = LoginSerializer(users, many=True)
        return Response(Serializer.data,status=status.HTTP_201_CREATED )

    def post(self, request):

        Serializer = LoginSerializer(data=request.data)
        if Serializer.is_valid():
            try:
                matchemail = User.objects.get(email=Serializer.validated_data["email"])
            except User.DoesNotExist:
                return Response({"Error": "Please Sign up first"}, status=status.HTTP_201_CREATED)

            else:

                # print("Helaly")
                Serializer.save()
                password = Serializer.validated_data["password"]
                w=authenticate(username=Serializer.validated_data["email"] , password=password)

                # print(w)
                # print(Serializer.validated_data["email"])

                if not w==None :

                    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                    Serializer.save()
                    payload = jwt_payload_handler(matchemail)
                    token = jwt_encode_handler(payload)

                    return Response({"token": token}, status=status.HTTP_201_CREATED)

                else:
                    # print(matchemail.password)
                    return Response({"Error": "Please Sign up first"}, status=status.HTTP_201_CREATED)

