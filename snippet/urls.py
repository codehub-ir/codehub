from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('docs/', views.docpage, name='documentation'),
    path('new/', views.new, name='new'),
    path('snippet/<str:id>', views.show, name='show'),
]
