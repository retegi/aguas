from django.urls import include,path
from . import views

app_name = 'maps_app'

urlpatterns = [
    path(
        '',
        views.HomeMapView.as_view(),
        name='home_map'
    ),
]