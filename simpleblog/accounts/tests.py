from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

class AccountCreationTest(TestCase):
    
    def test_a_singup_page_exists(self):
        response = self.client.get(reverse('signup_page'))

        self.assertEqual(response.status_code,HTTPStatus.OK,)
        self.assertTemplateUsed('accounts/signup.html')
        self.assertContains(response, 'Create Your Account')
