from django.urls import include, path
from . import views

app_name = 'stations_app'

urlpatterns = [
    path('',
        views.StationList.as_view(),
        name='station_list',
    ),

    path('station_add',
        views.StationAdd.as_view(),
        name='station_add'
    ),
    path(
        'update_station/<pk>/',
        views.StationUpdateView.as_view(),
        name='station_update'
    ),
    path(
        'detail_station/<pk>/',
        views.StationDetailView.as_view(),
        name='detalle_estacion'
    ),
    path(
        'delete_station/<pk>/',
        views.StationDeleteView.as_view(),
        name='eliminar_estacion'
    ),
    #path('',
    #    views.StationList,
    #    name='station_list',
    #)"""
]



    
