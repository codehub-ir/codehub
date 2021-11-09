from django.db import models
from django.urls import reverse

from .constants import LANGUAGES
from .utils import generateSID
from account.models import User


class Snippet(models.Model):

    id = models.CharField(
        verbose_name='ID',
        max_length=11,
        primary_key=True,
        editable=False,
    )
    title = models.CharField(
        max_length=50,
        default='',
    )
    description = models.TextField(
        null=True,
    )
    body = models.TextField(
        verbose_name='Script',
        null=True,
    )
    lang = models.CharField(
        verbose_name='Language',
        max_length=250,
        choices=LANGUAGES,
        null=True,
    )
    created_on = models.DateField(
        auto_now=True,
        editable=False,
    )

    # TODO: Adding a view counter using django-hitcount pkg

    class Meta:
        indexes = [models.Index(fields=['id'])]

    def __str__(self): return self.title

    def get_absolute_url(self):
        return reverse('snippet_detail', args=[self.id])

    def save(self, *args, **kwargs):
        self.id = generateSID()
        super().save(*args, **kwargs)


class Ticket(models.Model):
    pass


class Comment(models.Model):
    pass


class Tag(models.Model):
    pass
