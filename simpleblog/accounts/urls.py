
from django.urls import path
from simpleblog.accounts import views

urlpatterns = [
    path('signup/', views.signup, name='signup_page')
]
