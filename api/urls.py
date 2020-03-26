from django.urls import path
from . import views

urlpatterns = [
    path('v1/snippet/<str:SID>', views.DetailSnippet.as_view()),
    path('v1/snippet/', views.AddSnippet.as_view()),
]
