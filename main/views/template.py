from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404

from main.models import Snippet, Ticket
from main.forms import SnippetCreateForm, TicketCreateForm


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


class TicketCreateView(LoginRequiredMixin, CreateView):
    template_name = 'create_ticket.html'
    model = Ticket
    form_class = TicketCreateForm

    def form_valid(self, form):
        user = self.request.user
        form.instance.created_by = user
        return super().form_valid(form)


class TicketView(DetailView):
    model = Ticket
    template_name = 'ticket.html'

    def get_context_data(self, **kwargs):
        ticket = kwargs['object']
        if ticket.created_by == self.request.user or ticket.is_valid == 'approved':
            return super().get_context_data(**kwargs)
        else:
            raise Http404()
