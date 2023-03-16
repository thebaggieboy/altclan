from rest_framework import routers
from .views import ReviewViewSet

router = routers.DefaultRouter()
router.register(r'reviews', ReviewViewSet)