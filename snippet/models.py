from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from ckeditor.fields import RichTextField
from .tasks import calendar
from django.utils.translation import gettext as _

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

COLOR_THEME = [
    ('suggest1', _('red-pink')),
    ('suggest2', _('red-yellow')),
    ('suggest3', _('yellow-blue')),
    ('suggest4', _('pink-blue smooth')),
]


class Snippet(models.Model):
    SID = models.CharField(max_length=10, verbose_name=_('SID'))
    title = models.CharField(max_length=100, verbose_name=_('Title'))
    detail = models.TextField(blank=True, verbose_name=_('Details'))
    script = models.TextField(verbose_name=_('Script'))
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100,
                                verbose_name=_('Programming language'))
    pub_date = models.CharField(max_length=50,
                                verbose_name=_('Submition date'))
    link = models.URLField(verbose_name=_('URL Address'))

    def __str__(self):
        return self.title


class Suggest(models.Model):
    title = models.CharField(max_length=30, verbose_name=_('Title'))
    content = RichTextField(verbose_name=_('Content'))
    theme = models.CharField(choices=COLOR_THEME, max_length=100,
                             verbose_name=_('Style'), default='suggest1')
    pub_date = models.CharField(max_length=50, default=calendar(),
                                verbose_name=_('Submition date'))

    def __str__(self):
        return self.title
