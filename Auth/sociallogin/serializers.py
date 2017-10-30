from rest_framework import serializers
from .models import SocialLoginUser
from django.core.files.base import ContentFile



from rest_framework import serializers



class SLSerializer(serializers.ModelSerializer):


    class Meta:
        model = SocialLoginUser
        fields="__all__"



