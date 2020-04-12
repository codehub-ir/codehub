from django.urls import path, include
from . import views

urlpatterns = [
    # VISUAL
    path('', views.index, name='home'),
    path('docs/', views.docpage, name='documentation'),
    path('new/', views.new, name='new'),
    path('team/', views.team, name='team'),
    path('snippet/<str:id>/', views.show, name='show'),

    # API
    path('api/v1/snippet/<str:SID>/', views.SnippetView.as_view()),
    path('api/v1/snippet/', views.SnippetAdd.as_view()),
    path('api/v1/team/', views.TeamView.as_view()),

    # API - ADMIN
    path('api/v1/admin/snippet/', views.AdminSnippetView.as_view()),
    path('api/v1/admin/suggest/', views.AdminSuggestAdd.as_view()),
    path('api/v1/admin/team/', views.AdminTeamAdd.as_view()),

    # API - Auth
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/admin/', include('rest_auth.urls')),
]
