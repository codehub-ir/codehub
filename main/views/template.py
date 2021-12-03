from django.views.generic import TemplateView, CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.urls import reverse
from django.shortcuts import redirect

from main.models import Snippet, Ticket, Comment
from main.forms import SnippetCreateForm, TicketCreateForm, CommentCreateForm


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


class TicketView(DetailView, CreateView):
    model = Ticket
    template_name = 'ticket.html'
    form_class = CommentCreateForm

    def get_context_data(self, **kwargs):
        ticket = kwargs['object']
        if ticket.created_by == self.request.user or ticket.is_valid == 'approved':
            context = super(TicketView, self).get_context_data(**kwargs)
            context['comments'] = Comment.objects.filter(
                ticket=ticket)
            return context
        else:
            raise Http404()

    def form_valid(self, form, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            ticket = self.get_object()
            form.instance.ticket = ticket
            form.instance.created_by = user
            return super().form_valid(form)
        else:
            return redirect(reverse('login'))
