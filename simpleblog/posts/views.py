from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from simpleblog.posts.forms import PostCreationForm
from simpleblog.posts.models import Post


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        "post": post,
    }

    return render(request, "posts/detail.html", context)

@login_required
def create_post(request):
    form = PostCreationForm()


    if request.method == 'POST':
        form = PostCreationForm(request.POST)
        
        if form.is_valid():
            form.instance.author = request.user
            form.save()

            return redirect(reverse('homepage'))
        
    context = {
        'form': form
    }

    return render(request, 'posts/create_post.html', context)
