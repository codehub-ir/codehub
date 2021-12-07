from django.urls import path
from django.views.generic import TemplateView

from .views.template import HomeView, SnippetCreateView, SnippetView, TicketCreateView, TicketView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new-snippet/', SnippetCreateView.as_view(), name='new_snippet'),
    path('snippet/<str:pk>/', SnippetView.as_view(), name='snippet'),

    path('new-ticket/', TicketCreateView.as_view(), name='new_ticket'),
    path('ticket/<str:pk>/<str:slug>',
         TicketView.as_view(), name='ticket'),

    # static pages
    path(
        'download/',
        TemplateView.as_view(template_name='download.html'),
        name='download'
    ),
]
