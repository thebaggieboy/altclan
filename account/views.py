
from rest_framework import viewsets
from .serializers import UserSerializer, ProfileSerializer
from .models import Profile

from django.conf import settings
User = settings.AUTH_USER_MODEL


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer