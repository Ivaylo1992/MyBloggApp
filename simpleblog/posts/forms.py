from django import forms

from simpleblog.posts.models import Post

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')