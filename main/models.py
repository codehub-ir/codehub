from accounts.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext as _
from django_jalali.db import models as jmodels

#from .constants import  VERIFICATIONS



class Event(models.Model):
    title = models.CharField(
        max_length=150,
    )
    body = models.TextField(blank=True)
    created_on = jmodels.jDateTimeField(
        auto_now=True,
        editable=False,
    )

    def __str__(self):
        return self.title
