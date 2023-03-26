
from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile, CustomUser

from django.conf import settings
#User = settings.AUTH_USER_MODEL


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
