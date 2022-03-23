from django.urls import path

from .views import (CustomLoginView, CustomPasswordChangeView, ProfileView,
                    SignUpView)

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password/', CustomPasswordChangeView.as_view(), name='change_password'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
