from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'display_name')


class CustomUserUpdateForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('display_name',
                  'email',
                  'twitter',
                  'github',
                  )
