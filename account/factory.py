import factory 
from django.contrib.auth.models import User
from factory.faker import faker
from .models import Profile

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
        
