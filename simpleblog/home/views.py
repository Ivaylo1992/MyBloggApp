from django.shortcuts import render

from simpleblog.posts.models import Post

def index(request):
    posts = Post.objects.all()

    context = {"posts": posts}

    return render(request, "home/index.html", context=context)
