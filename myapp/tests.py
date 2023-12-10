
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_login(self):
        # Ваш тест для входу тут
        pass

    def test_user_registration(self):
        # Ваш тест для реєстрації тут
        pass

    def test_admin_only_view(self):
        # Ваш тест для адмінського view тут
        pass

    def test_custom_validations(self):
        # Ваш тест для кастомних валідацій тут
        pass
