from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Post(models.Model):
    title = models.CharField(
        max_length=60,
    )

    content = models.TextField()

    author = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            "post_detail",
            kwargs={"post_id": self.pk},
        )
