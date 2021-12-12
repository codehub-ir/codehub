from django.urls import path
from django.views.generic import TemplateView

from .views.template import HomeView, SnippetCreateView, SnippetView, TicketCreateView, TicketView
from .views.api import SnippetCreateAPIView, SnippetAPIView


urlpatterns = [

    # Template URLs
    path('', HomeView.as_view(), name='home'),
    path('new-snippet/', SnippetCreateView.as_view(), name='new_snippet'),
    path('snippet/<str:pk>/', SnippetView.as_view(), name='snippet'),

    path('new-ticket/', TicketCreateView.as_view(), name='new_ticket'),
    path('ticket/<str:pk>/<str:slug>', TicketView.as_view(), name='ticket'),

    # API URLs
    # -- v1.0 --
    path('api/v1/snippet', SnippetCreateAPIView.as_view()),
    path('api/v1/snippet/<str:pk>', SnippetAPIView.as_view()),

    # static pages
    path(
        'download/',
        TemplateView.as_view(template_name='download.html'),
        name='download'
    ),
]
