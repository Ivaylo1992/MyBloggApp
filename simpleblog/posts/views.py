from django.shortcuts import render

from simpleblog.posts.models import Post


def index(request):
    posts = Post.objects.all()

    context = {"posts": posts}

    return render(request, "posts/index.html", context=context)


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        "post": post,
    }

    return render(request, "posts/detail.html", context)
