from django.urls import include, path
from . import views

app_name = 'stations_app'

urlpatterns = [
    path(
        '',
        views.StationListView.as_view(),
        name='list_station',
    ),

    path('add_station',
        views.StationAddView.as_view(),
        name='add_station'
    ),
    path(
        'update_station/<pk>/',
        views.StationUpdateView.as_view(),
        name='update_station'
    ),
    path(
        'detail_station/<pk>/',
        views.StationDetailView.as_view(),
        name='detail_station'
    ),
    path(
        'delete_station/<pk>/',
        views.StationDeleteView.as_view(),
        name='delete_station'
    ),
]



    
