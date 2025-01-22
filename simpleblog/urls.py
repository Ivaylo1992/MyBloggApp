
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('simpleblog.posts.urls')),
    path('accounts/', include('simpleblog.accounts.urls')),
    path('', include('simpleblog.home.urls')),
]
