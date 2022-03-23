from django.urls import path
from django.views.generic import TemplateView

from .views import HomeView, ListEventsAPIView
from .constants import REDOC_DESCRIPTION

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title='CodeHub RESTful API Service Documentation',
        default_version='v1',
        description=REDOC_DESCRIPTION,
        contact=openapi.Contact(email='lnxpylnxpy@gmail.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    # Template URLs
    path('', HomeView.as_view(), name='home'),

    # API URLs
    # -- v1.0 --
    path('api/v1/event', ListEventsAPIView.as_view()),
    path('api/v1/docs', schema_view.with_ui('redoc',
         cache_timeout=0), name='api_docs_v1'),

    # static pages
    path(
        'download/',
        TemplateView.as_view(template_name='download.html'),
        name='download'
    ),
    path(
        'development/',
        TemplateView.as_view(template_name='development.html'),
        name='development'
    ),
]
