# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import SLSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from .models import SocialLoginUser
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings


class UserList2(APIView):
    def get(self, request):
        users = SocialLoginUser.objects.all()
        Serializer = SLSerializer(users, many=True)
        return Response(Serializer.data)

    def post(self, request):

        Serializer = SLSerializer(data=request.data)
        if Serializer.is_valid():
            try:
                matchemail = User.objects.get(email=Serializer.validated_data["email"])
            except User.DoesNotExist:
                return Response("Please Sign up first", status=status.HTTP_400_BAD_REQUEST)

            else:

                # print("Helaly")
                #can we add an abstract user with one to one fields 3lshan n7afez 3ala system
                # w fe nafs el wa2t yb2a m3ana Users Model with the regular databases bas added 3aliha
                #fields aktar?!
                # provider = Serializer.validated_data["provider"]

                # if matchemail.provider == provider :

                jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

                payload = jwt_payload_handler(matchemail)
                token = jwt_encode_handler(payload)

                return Response({"Token": token}, status=status.HTTP_400_BAD_REQUEST)

                # print(w)
                # print(Serializer.validated_data["email"])



                # else:
                #     # print(matchemail.password)
                #     return Response("You are not signed with us with that provider, please try again", status=status.HTTP_400_BAD_REQUEST)
                #
