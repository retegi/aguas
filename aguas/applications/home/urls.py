from django.urls import include, path
from . import views

#app_name = 'stations_app'

urlpatterns = [
    path('',
        views.LoginView.as_view(),
        name='login',
    ),
    path('home/',
        views.HomePageView.as_view(),
        name='home',
    )
]