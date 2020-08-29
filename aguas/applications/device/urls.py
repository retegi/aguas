from django.urls import include, path
from . import views

app_name = 'devices_app'

urlpatterns = [
    path('',
        views.DeviceListView.as_view(),
        name='list_device'
    ),
    path('add_device',
        views.DeviceAddView.as_view(),
        name='add_device'
    ),
    path(
        'update_device/<pk>/',
        views.DeviceUpdateView.as_view(),
        name='update_device'
    ),
    path(
        'detail_device/<pk>/',
        views.DeviceDetailView.as_view(),
        name='detail_device'
    ),
    path(
        'delete_device/<pk>/',
        views.DeviceDeleteView.as_view(),
        name='delete_device'
    ),

    #Listar device según station
    path(
        'list_devices_by_station/<pk>/',
        views.DeviceListByStationView.as_view(),
        name='list_devices_by_station'
    ),
    path(
        'list_devices_by_installation/<pk>/',
        views.DeviceListByInstallationView.as_view(),
        name='list_devices_by_installation'
    )
]