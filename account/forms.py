from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'display_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('display_name',
                  'email',
                  'twitter',
                  'github',
                  )
