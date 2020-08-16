from django.urls import include, path
from . import views

app_name = 'devices_app'

urlpatterns = [
    path('',
        views.DeviceListView.as_view(),
        name='device_list'
    ),
    path('device_add',
        views.DeviceAddView.as_view(),
        name='device_add'
    ),
    path(
        'device_update/<pk>/',
        views.DeviceUpdateView.as_view(),
        name='device_update'
    ),
    path(
        'device_detail/<pk>/',
        views.DeviceDetailView.as_view(),
        name='device_detail'
    ),
    path(
        'device_delete/<pk>/',
        views.DeviceDeleteView.as_view(),
        name='device_delete'
    ),
]