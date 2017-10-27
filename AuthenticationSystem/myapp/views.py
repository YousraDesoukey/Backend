# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import UserSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Users
from rest_framework.response import Response
from rest_framework import status


class UserList(APIView):
    def get(self, request):
        users = Users.objects.all()
        Serializer = UserSerializer(users, many=True)
        return Response(Serializer.data)

    def post(self, request):

        Serializer = UserSerializer(data=request.data)
        if Serializer.is_valid():
            try:
                matchemail = Users.objects.get(email=Serializer.validated_data["email"])
            except Users.DoesNotExist:
                return Response("Please Sign up first", status=status.HTTP_400_BAD_REQUEST)

            else:
                print("Helaly")
                password = Serializer.validated_data["password"]
                if (password == matchemail.password):
                    return Response("Token", status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response("Wrong password please try again", status=status.HTTP_400_BAD_REQUEST)

