from django.db import models

from django.utils.translation import gettext as _

from django_jalali.db import models as jmodels

from accounts.models import User

from main.utils import generateUID
from .constants import LANGUAGES
from django.urls import reverse




class Snippet(models.Model):

    id = models.CharField(
        verbose_name='ID',
        max_length=11,
        primary_key=True,
        editable=False,
    )
    title = models.CharField(
        verbose_name=_('Title'),
        max_length=50,
        default='',
    )
    description = models.TextField(
        verbose_name=_('Description'),
        blank=True
    )
    body = models.TextField(
        verbose_name=_('Script'),
    )
    lang = models.CharField(
        verbose_name=_('Programming Language'),
        max_length=250,
        choices=LANGUAGES,
    )
    created_on = jmodels.jDateTimeField(
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

    class Meta:
        indexes = [models.Index(fields=['id'])]

    def __str__(self): return self.title

    def get_absolute_url(self):
        return reverse('snippet', args=[str(self.id)])

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = generateUID(Snippet)
        super().save(*args, **kwargs)

