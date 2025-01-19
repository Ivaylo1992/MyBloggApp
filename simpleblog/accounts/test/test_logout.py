from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class LogoutTest(TestCase):
    def setUp(self):
        self.username = 'testuser123'
        self.email = 'testuser123@gmail.com'
        self.password = 'testpassword##123'

        UserModel.objects.create_user(
            username = self.username,
            email=self.email,
            password=self.password
        )

    def test_logout_view_logs_out_user(self):
        self.client.login(username=self.username, password=self.password)

        self.assertTrue('_auth_user_id' in self.client.session)

        response = self.client.get(reverse('logout_page'))

        self.assertFalse('_auth_user_id' in response)