from rest_framework import routers
from .views import  ProfileViewSet, UserViewSet

router = routers.DefaultRouter()

router.register(r'profile', ProfileViewSet)



