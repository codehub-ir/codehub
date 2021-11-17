from django.urls import path

from .views import CustomPasswordChangeView, ProfileView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password/', CustomPasswordChangeView.as_view(), name='change_password'),
]
