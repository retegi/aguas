from django.urls import path
from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'register/',
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        '',
        views.LoginUser.as_view(),
        name='user-login',
    ),
    path(
        'logout',
        views.LogoutView.as_view(),
        name='user-logout',
    )
]