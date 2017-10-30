from rest_framework import serializers
from .models import UserSocial
from django.core.files.base import ContentFile



from rest_framework import serializers



class AuthSerializer(serializers.ModelSerializer):


    class Meta:
        model = UserSocial
        fields="__all__"



