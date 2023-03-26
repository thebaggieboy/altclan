from rest_framework import serializers
from django.conf import settings
from .models import Profile, CustomUser

User = settings.AUTH_USER_MODEL

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'first_name', 'last_name', 'email_address', 'mobile_number', 'display_picture']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
