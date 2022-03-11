import factory
from factory.django import DjangoModelFactory
from django.contrib.auth.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    is_staff = False
    is_superuser = False
    username = factory.Sequence(lambda n: 'user%d' % n)
    password = factory.PostGenerationMethodCall('set_password', 'test')
    email = factory.LazyAttribute(lambda u: '%s@example.com' % u.username)
