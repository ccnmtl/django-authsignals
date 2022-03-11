from django.test import TestCase
from django.contrib.auth.models import User

from .factories import UserFactory


class BasicTest(TestCase):
    def setUp(self):
        UserFactory(username='testadmin1')
        UserFactory(username='user1')

    def test_login_as_new_superuser(self):
        self.client.login(username='testadmin1', password='test')

        u = User.objects.get(username='testadmin1')
        self.assertTrue(u.is_superuser)

    def test_login_as_user(self):
        self.client.login(username='user1', password='test')

        u = User.objects.get(username='user1')
        self.assertFalse(u.is_superuser)
