from django.shortcuts import redirect, render
from django.urls import reverse
from simpleblog.accounts.forms import UserRegistrationForm


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
    return render(request, 'accounts/login.html')