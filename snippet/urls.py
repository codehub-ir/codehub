from django.urls import path, include
from .views import visual, api

urlpatterns = [
    # VISUAL
    path('', visual.index, name='home'),
    path('docs/', visual.docpage, name='documentation'),
    path('new/', visual.new, name='new'),
    path('team/', visual.team, name='team'),
    path('snippet/<str:id>/', visual.show, name='show'),

    # API
    path('api/v1/snippet/<str:SID>/', api.SnippetView.as_view()),
    path('api/v1/snippet/', api.SnippetAdd.as_view()),
    path('api/v1/team/', api.TeamView.as_view()),

    # API - ADMIN
    path('api/v1/admin/snippet/', api.AdminSnippetView.as_view()),
    path('api/v1/admin/snippet/<str:SID>/', api.AdminSnippetMod.as_view()),
    path('api/v1/admin/suggest/', api.AdminSuggestAdd.as_view()),
    path('api/v1/admin/suggest/<int:pk>', api.AdminSuggestMod.as_view()),
    path('api/v1/admin/team/', api.AdminTeamAdd.as_view()),
    path('api/v1/admin/team/<int:pk>', api.AdminTeamMod.as_view()),

    # API - Auth
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/admin/', include('rest_auth.urls')),
]
