from django.urls import path

from .views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    LastLoginView
)

urlpatterns = [
    path('signup/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('profile/', UserProfileView.as_view()),
    path('lastlogin/<int:user_id>/', LastLoginView.as_view()),

]
