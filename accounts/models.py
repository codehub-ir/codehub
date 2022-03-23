from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext as _


class User(AbstractUser):

    display_name = models.CharField(
        _('Display Name'),
        max_length=50,
    )
    email = models.EmailField(
        _('Email Address'),
    )
    twitter = models.URLField(
        _('Twitter Address'),
        blank=True,
    )
    github = models.URLField(
        _('Github Address'),
        blank=True,
    )

    def __str__(self): return self.username
