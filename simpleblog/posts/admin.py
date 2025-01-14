from django.contrib import admin

from simpleblog.posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin): ...
