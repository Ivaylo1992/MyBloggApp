from django.shortcuts import render
from simpleblog.accounts.forms import UserRegistrationForm


def signup(request):
    form = UserRegistrationForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/signup.html', context)
