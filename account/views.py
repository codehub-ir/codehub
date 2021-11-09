from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .forms import CustomUserCreationForm, CustomUserUpdateForm
from .models import User


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class ProfileView(UpdateView):
    model = User
    form_class = CustomUserUpdateForm
    template_name = "profile.html"
    success_url = reverse_lazy('profile')

    def get_object(self, *args, **kwargs):
        user = User.objects.get(username=self.request.user)
        return user
