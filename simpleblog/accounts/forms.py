from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from simpleblog.accounts.models import Profile

UserModel = get_user_model()

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'address')


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('first_name', 'last_name', 'username')
        read_only_fields = ('username',)
