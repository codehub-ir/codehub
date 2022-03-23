from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView

from .forms import CommentCreateForm, TicketCreateForm
from .models import Comment, Ticket


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
                ticket=ticket).order_by('-created_on')
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


class TicketSearchResultsView(ListView):
    model = Ticket
    template_name = 'ticket_search_results.html'
    context_object_name = 'tickets'
    extra_context = {
        'searched_keyword': None,
    }

    def get_queryset(self):
        key = self.request.GET.get('t')
        self.extra_context['searched_keyword'] = key

        tickets = Ticket.objects.filter(
            Q(title__icontains=key,
              is_valid='approved')
        )
        return tickets

    def get_context_data(self, **kwargs):
        context = super(TicketSearchResultsView,
                        self).get_context_data(**kwargs)
        context.update(self.extra_context)
        return context
