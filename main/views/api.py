from rest_framework.generics import CreateAPIView, RetrieveAPIView
from main.models import Snippet
from main.serializers import SnippetSerializer

from django.shortcuts import get_object_or_404


class SnippetCreateAPIView(CreateAPIView):
    serializer_class = SnippetSerializer


class SnippetAPIView(RetrieveAPIView):
    serializer_class = SnippetSerializer

    def get_object(self):
        requested_uid = self.kwargs['pk']
        return get_object_or_404(Snippet, id=requested_uid)
