from django.urls import path
from . import views

app_name = 'consumables_app'


urlpatterns = [
    path('',
        views.ConsumableListView.as_view(),
        name='list_consumable'
    ),
    path(
        'add_consumable',
        views.ConsumableAddView.as_view(),
        name='add_consumable'
    ),
    path(
        'update_consumable/<pk>/',
        views.ConsumableUpdateView.as_view(),
        name='update_consumable'
    ),
    path(
        'detail_consumable/<pk>/',
        views.ConsumableDetailView.as_view(),
        name='detail_consumable'
    ),
    path(
        'delete_consumable/<pk>/',
        views.ConsumableDeleteView.as_view(),
        name='delete_consumable'
    ),
    path(
        'list_consumables_by_station/<pk>/',
        views.ConsumableListByStationView.as_view(),
        name='list_consumables_by_station'
    ),
    path(
        'list_consumables_by_installation/<pk>/',
        views.ConsumableListByInstallationView.as_view(),
        name='list_consumables_by_installation'
    ),
    path(
        'list_consumables_by_device/<pk>/',
        views.ConsumableListByDeviceView.as_view(),
        name='list_consumables_by_device'
    ),


]