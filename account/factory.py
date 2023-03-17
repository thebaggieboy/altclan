import factory 
from django.conf import settings
from factory.faker import faker
from .models import Profile, CustomUser

User = settings.AUTH_USER_MODEL
FAKE = faker.Faker()

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    email = factory.Faker('email')

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    #email_address = factory.Faker('email')
    mobile_number = factory.Faker('phone_number')
    #user = factory.SubFactory(UserFactory)




