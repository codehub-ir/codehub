from django.views.generic import TemplateView, CreateView, DetailView

from main.models import Snippet

from account.models import User

from main.forms import SnippetCreateForm


class HomeView(TemplateView):
    template_name = 'home.html'


class SnippetCreateView(CreateView):
    model = Snippet
    template_name = 'create_snippet.html'
    form_class = SnippetCreateForm

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            user = self.request.user
            form.instance.created_by = user
        return super().form_valid(form)


class SnippetView(DetailView):
    model = Snippet
    template_name = 'snippet.html'
