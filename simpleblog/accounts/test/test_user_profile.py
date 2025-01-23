from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth import get_user_model
from django.http import HttpRequest

from simpleblog.accounts.forms import ProfileUpdateForm, UserUpdateForm

UserModel = get_user_model()

class UpdateProfileTest(TestCase):
    def setUp(self):
        self.url = reverse('update_user_profile')
        self.template_name = 'accounts/update_profile.html'
        self.credentials = {
            'username': 'testuser',
            'email': 'test@user.com',
            'password': '12user34',
        }

        UserModel.objects.create_user(**self.credentials)
    

    def test_profile_update_page_exists(self):
        self.client.login(**self.credentials)
        response = self.client.get(self.url)
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, self.template_name)

        profile_form = response.context.get('profile_form', None)
        user_form = response.context.get('user_form', None)

        self.assertIsInstance(profile_form, ProfileUpdateForm)
        self.assertIsInstance(user_form, UserUpdateForm)
    

    def test_profile_and_user_update_forms_update_user(self):
        request = HttpRequest()

        request.user = UserModel.objects.get(id=1)

        request.POST = {
            'bio': 'Text for testing',
            'address': 'some address street 123',
            'first_name': 'Gosho',
            'last_name': 'Peshov',
            'username': 'testuser'
        }

        profile_form = ProfileUpdateForm(instance=request.user.profile, data={
            'bio': request.POST.get('bio', None),
            'address': request.POST.get('address', None),
        })

        user_form = UserUpdateForm(instance=request.user, data={
            'first_name': request.POST.get('first_name', None),
            'last_name': request.POST.get('last_name', None),
            'username': request.POST.get('username', None),
        })

        self.assertTrue(profile_form.is_valid())
        self.assertTrue(user_form.is_valid())
        
        user_form.save()
        profile_form.save()

        self.assertEqual(request.user.username, request.POST.get('username'))
        self.assertEqual(request.user.profile.bio, request.POST.get('bio'))



