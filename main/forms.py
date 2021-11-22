from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from django.utils.translation import gettext as _

from .models import Snippet

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SnippetCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'crispy-form-item'
            visible.field.widget.attrs['spellcheck'] = 'false'

        self.fields['body'].widget.attrs['class'] += ' code-snippet'

    class Meta:
        model = Snippet
        fields = ('title', 'description', 'body', 'lang')

    helper = FormHelper()
    helper.add_input(Submit('submit', _('Create'),
                     css_class='btn-primary crispy-form-item'))
