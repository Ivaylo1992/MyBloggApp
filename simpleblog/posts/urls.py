from django.urls import path

from simpleblog.posts import views

urlpatterns = (path("", views.index, name="homepage"),)
