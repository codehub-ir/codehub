from django.views.generic import CreateView, DetailView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView

from .models import Snippet
from .forms import SnippetCreateForm

from .serializers import SnippetSerializer
from django.shortcuts import get_object_or_404


# Template Views

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


# API Views

class SnippetCreateAPIView(CreateAPIView):
    serializer_class = SnippetSerializer


class SnippetAPIView(RetrieveAPIView):
    serializer_class = SnippetSerializer

    def get_object(self):
        requested_uid = self.kwargs['pk']
        return get_object_or_404(Snippet, id=requested_uid)