from django.urls import path

from .views.template import HomeView, SnippetCreateView, SnippetView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('new/', SnippetCreateView.as_view(), name='new_snippet'),
    path('snippet/<str:pk>/', SnippetView.as_view(), name='snippet'),
]
