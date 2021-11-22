from django.views.generic import TemplateView, CreateView, DetailView
from main.models import Snippet

from main.forms import SnippetCreateForm


class HomeView(TemplateView):
    template_name = 'home.html'


class SnippetCreateView(CreateView):
    model = Snippet
    template_name = 'create_snippet.html'
    form_class = SnippetCreateForm


class SnippetView(DetailView):
    model = Snippet
    template_name = 'snippet.html'
