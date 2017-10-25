from rest_framework import serializers
from .models import Users
from django.core.files.base import ContentFile



from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = Users
        fields="__all__"



