from django.urls import path

from .views import SnippetCreateView, SnippetView, SnippetCreateAPIView, SnippetAPIView




urlpatterns = [
    # Template URLs
    path('new-snippet/', SnippetCreateView.as_view(), name='new_snippet'),
    path('snippet/<str:pk>/', SnippetView.as_view(), name='snippet'),

    # API URLs
    # -- v1.0 --
    path('api/v1/snippet', SnippetCreateAPIView.as_view()),
    path('api/v1/snippet/<str:pk>', SnippetAPIView.as_view()),
]
