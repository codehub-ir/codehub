from .models import Event


def allEvents(request):
    return {
        'events': Event.objects.all().order_by('-created_on')[:5],
    }
