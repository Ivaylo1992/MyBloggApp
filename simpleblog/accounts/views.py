from django.shortcuts import redirect, render
from django.urls import reverse
from simpleblog.accounts.forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from simpleblog.posts.models import Post

def signup(request):
    form = UserRegistrationForm()

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect(reverse('login_page'))


    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)


def login(request):
    form = AuthenticationForm()

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                auth_login(request, user)
                
                return redirect(reverse('homepage'))


    context = {
        'form': form
    }

    return render(request, 'accounts/login.html', context)


def logout(request):
    auth_logout(request)
    return redirect(reverse('homepage'))

@login_required
def user_profile(request):
    user = request.user
    posts = Post.objects.filter(author=user).all()

    context = {
        'posts': posts,
        'user': user
    }

    return render(request, 'accounts/user_profile.html', context=context)