from django.urls import include, path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('',
        views.LoginView.as_view(),
        name='login',
    ),
    path('panel/',
        views.HomePageView.as_view(),
        name='panel',
    )
]