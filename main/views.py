from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from tickets.models import Ticket

from .models import Event
from .serializers import EventSerializer


# Template Views
class HomeView(ListView):
    template_name = 'home.html'
    model = Ticket
    queryset = Ticket.objects.filter(
        is_valid='approved').order_by('-created_on')[:5]
    context_object_name = 'tickets'


# API Views
class ListEventsAPIView(ListAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all().order_by('-created_on')[:5]
