from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    display_name = models.CharField(
        max_length=50,
    )
    email = models.EmailField(
        blank=True,
    )
    twitter = models.EmailField(
        blank=True,
    )
    github = models.EmailField(
        blank=True,
    )

    def __str__(self): return self.username
