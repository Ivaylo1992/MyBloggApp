from django.urls import path

from simpleblog.posts import views

urlpatterns = (
    path("", views.index, name="homepage"),
    path("post/<int:post_id>/", views.post_detail, name="post_detail"),
    path("create/", views.create_post, name="create_post"),
)
