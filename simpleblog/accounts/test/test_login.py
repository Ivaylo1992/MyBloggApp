from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from simpleblog.accounts.forms import UserRegistrationForm


class LoginTest(TestCase):
    def test_login_page_exists(self):
        response = self.client.get(reverse('login_page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/login.html')