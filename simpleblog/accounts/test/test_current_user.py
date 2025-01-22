from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class ProfileTest(TestCase):
    def setUp(self):
        self.url = reverse('user_profile')
        self.template_name = 'accounts/user_profile.html'
        self.username = 'TestUser'
        self.email = 'test@user.com'
        self.password = '12ivo34$$'

        UserModel.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
        )
    
    def test_current_user_profile_exists(self):
        self.client.login(
            username=self.username,
            password=self.password,
        )
        
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, self.template_name)
    
    def test_current_user_requires_login(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, expected_url='/accounts/login/?next=/accounts/user_profile/')
        