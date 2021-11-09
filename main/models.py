from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django_jalali.db import models as jmodels

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
    created_on = jmodels.jDateField(
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


class Tag(models.Model):
    name = models.CharField(
        max_length=50,
    )
    description = models.CharField(
        max_length=150,
    )
    created_on = jmodels.jDateField(
        auto_now=True,
        editable=False,
    )

    def __str__(self): return self.name


class Ticket(models.Model):
    title = models.CharField(
        max_length=150,
    )
    description = models.TextField()
    tags = models.ManyToManyField(
        Tag,
    )
    slug = models.SlugField(
        editable=False,
    )
    is_valid = models.BooleanField(
        default=False,
    )
    created_on = jmodels.jDateField(
        auto_now=True,
        editable=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
    )

    # TODO: Adding a view counter using django-hitcount pkg

    def __str__(self): return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Comment(models.Model):
    body = models.CharField(
        max_length=250,
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
    )
    is_valid = models.BooleanField(
        default=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
    )
    created_on = jmodels.jDateField(
        auto_now=True,
        editable=False,
    )

    def __str__(self):
        return f'{self.created_by} on {self.ticket}'
