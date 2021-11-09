from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    display_name = models.CharField(
        max_length=50,
    )
    email = models.EmailField(
        blank=True,
    )
    twitter = models.URLField(
        blank=True,
    )
    github = models.URLField(
        blank=True,
    )

    def __str__(self): return self.username
