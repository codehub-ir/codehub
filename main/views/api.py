from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from main.models import Snippet, Event
from main.serializers import SnippetSerializer, EventSerializer

from django.shortcuts import get_object_or_404


class SnippetCreateAPIView(CreateAPIView):
    serializer_class = SnippetSerializer


class SnippetAPIView(RetrieveAPIView):
    serializer_class = SnippetSerializer

    def get_object(self):
        requested_uid = self.kwargs['pk']
        return get_object_or_404(Snippet, id=requested_uid)


class ListEventsAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('-created_on')
