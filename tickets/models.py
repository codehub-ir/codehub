from django.db import models
from .constants import VERIFICATIONS
from django_jalali.db import models as jmodels
from django.utils.text import slugify
from django.utils.translation import gettext as _
from accounts.models import User
from main.utils import generateUID
from django.urls import reverse




class Tag(models.Model):
    name = models.CharField(
        max_length=50,
    )
    description = models.CharField(
        max_length=150,
    )
    created_on = jmodels.jDateTimeField(
        auto_now=True,
        editable=False,
    )

    def __str__(self): return self.name


class Ticket(models.Model):
    id = models.CharField(
        verbose_name='ID',
        max_length=11,
        primary_key=True,
        editable=False,
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=150,
    )
    description = models.TextField(
        verbose_name=_('Description')
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name=_('Tags'),
    )
    slug = models.SlugField(
        editable=False,
    )
    is_valid = models.CharField(
        verbose_name=_('Validation'),
        choices=VERIFICATIONS,
        default='pending',
        max_length=20,
    )
    created_on = jmodels.jDateTimeField(
        auto_now=True,
        editable=False,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        #        editable=False,
        null=True,
    )

    # TODO: Adding a view counter using django-hitcount pkg

    def __str__(self): return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)

        if not self.id:
            self.id = generateUID(Ticket)

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('ticket', args=[str(self.id), str(self.slug)])


class Comment(models.Model):
    body = models.CharField(
        verbose_name=_('Comment Body'),
        max_length=250,
    )
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        editable=False,
        null=True,
    )
    created_on = jmodels.jDateTimeField(
        auto_now=True,
        editable=False,
    )

    def __str__(self):
        return f'{self.created_by} on {self.ticket}'

    def get_absolute_url(self):
        return reverse('ticket', args=[str(self.ticket.id), str(self.ticket.slug)])