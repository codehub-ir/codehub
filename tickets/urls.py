from django.urls import path

from .views import TicketCreateView, TicketSearchResultsView, TicketView

urlpatterns = [

    # Template URLs
    path('new-ticket/', TicketCreateView.as_view(), name='new_ticket'),
    path('ticket/<str:pk>/<str:slug>', TicketView.as_view(), name='ticket'),
    path('search/', TicketSearchResultsView.as_view(), name='ticket_search_results'),
]
