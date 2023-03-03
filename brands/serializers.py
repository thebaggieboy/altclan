from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Brand, Merchandise, Order, Cart, BrandProfile, MerchandisesList, Leads
"""from django.conf import settings
User = settings.AUTH_USER_MODEL
"""
class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['brand_name', 'brand_logo', 'brand_bio']

class BrandProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BrandProfile
        fields = ['mobile_number', 'email_address', 'merchandises', 'address']


class LeadsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leads
        fields = ['brand_name', 'instagram_username', 'website_link']



class MerchandiseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Merchandise
        fields = [
            'brand', 'merchandise_name', 'merchandise_color', 'merchandise_image', 'merchandise_size', 'labels', 'collection', 'delivery_cost', 'price'
        ]

class MerchandiseListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MerchandisesList
        fields = [
            'brand',
            'merchandises'
        ]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['order_date', 'ordered', 'delivered', 'address']


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity', 'merchandises']
