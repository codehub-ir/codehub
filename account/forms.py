from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import gettext as _

from django.forms import HiddenInput

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'display_name')


class CustomUserUpdateForm(UserChangeForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = HiddenInput()

    class Meta:
        model = User
        fields = ('display_name',
                  'email',
                  'twitter',
                  'github',
                  )

    helper = FormHelper()
    helper.add_input(Submit('submit', _('Update'),
                     css_class='btn-primary crispy-submit-btn'))
