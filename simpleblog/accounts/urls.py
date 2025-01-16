
from django.urls import path
from simpleblog.accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup_page'),
    path('login/', views.login, name='login_page'),
]
