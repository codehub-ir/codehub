from django.db import models
from .constants import LANGUAGES
from .utils import generateSID


class Snippet(models.Model):

    id = models.CharField('ID', max_length=11,
                          primary_key=True, editable=False)

    title = models.CharField(max_length=50, default='')
    description = models.TextField(default='')
    body = models.TextField('Script', default='')
    lang = models.CharField('Language', max_length=250,
                            choices=LANGUAGES, default='')
    created_on = models.DateField(auto_now=True, editable=False)

    # TODO: Adding view counter using django-hitcount

    class Meta:
        pass

    def __str__(self): return self.title

    def save(self, *args, **kwargs):
        self.id = generateSID()
        super().save(*args, **kwargs)
