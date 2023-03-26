
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from core.views import *

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'brand_profile', BrandProfileViewSet)
router.register(r'leads', LeadsViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'merchandises', MerchandiseViewSet)
router.register(r'merchandise_images', MerchandiseGalleryViewSet)
router.register(r'cart', CartViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
  
    #path('api/', include('rest_framework.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   

