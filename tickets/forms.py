from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms.models import ModelForm
from django.utils.translation import gettext as _

from .models import Comment, Ticket


class TicketCreateForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # <input type="checkbox" class="btn-check" id="btn-check-outlined" autocomplete="off">
        # <label class="btn btn-outline-primary" for="btn-check-outlined">Single toggle</label><br>

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'crispy-form-item'
            visible.field.widget.attrs['spellcheck'] = 'false'

        self.fields['description'].widget.attrs['placeholder'] = _(
            'How can I convert `count` variable in..')

    class Meta:
        model = Ticket
        fields = ('title', 'description', 'tags')

    helper = FormHelper()
    helper.add_input(Submit('submit', _('Create'),
                     css_class='btn-primary crispy-form-item'))


class CommentCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'crispy-form-item'
            visible.field.widget.attrs['spellcheck'] = 'false'

    class Meta:
        model = Comment
        fields = ('body',)

    helper = FormHelper()
    helper.add_input(Submit('submit', _('Comment'),
                     css_class='btn-primary crispy-form-item'))
