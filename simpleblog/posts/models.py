from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=60,
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    modified_at = models.DateTimeField(
        auto_now=True
    )
