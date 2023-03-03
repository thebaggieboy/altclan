from django.shortcuts import render
from rest_framework import viewsets
from .models import Brand, Order, Cart, Merchandise, BrandProfile, MerchandisesList, Leads
from .serializers import(
      OrderSerializer,
      CartSerializer,
      LeadsSerializer,
      MerchandiseSerializer,
      BrandProfileSerializer,
      BrandSerializer,
      MerchandiseListSerializer
)


class MerchandiseViewSet(viewsets.ModelViewSet):
    queryset = Merchandise.objects.all()
    serializer_class = MerchandiseSerializer

class MerchandiseListViewSet(viewsets.ModelViewSet):
    queryset = MerchandisesList.objects.all()
    serializer_class = MerchandiseListSerializer

class LeadsViewSet(viewsets.ModelViewSet):
    queryset = Leads.objects.all()
    serializer_class = LeadsSerializer



class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Create your views here.
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

# Create your views here.
class BrandProfileViewSet(viewsets.ModelViewSet):
    queryset = BrandProfile.objects.all()
    serializer_class = BrandProfileSerializer


def create_merchandise_list(request):

    return render(request, 'alteclan/index.html')