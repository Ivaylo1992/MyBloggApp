from django.urls import path
from simpleblog.home import views

urlpatterns = [
    path('', views.index, name='homepage'),
    
]
