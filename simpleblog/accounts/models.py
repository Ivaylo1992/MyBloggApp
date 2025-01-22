from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Profile(models.Model):
    bio = models.TextField()

    profile_image = models.URLField(
        max_length=500
    )

    address = models.CharField(
        max_length=50
    )

    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    def __str__(self):
        return f'<Profile for {self.user.username}'