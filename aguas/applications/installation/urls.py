from django.urls import include,path
from . import views

app_name = 'installations_app'

urlpatterns = [
    path('',
        views.InstallationListView.as_view(),
        name='list_installation'
    ),
    path('add_installation',
        views.InstallationAddView.as_view(),
        name='add_installation'
    ),
    path(
        'update_installation/<pk>/',
        views.InstallationUpdateView.as_view(),
        name='update_installation'
    ),
    path(
        'detail_installation/<pk>/',
        views.InstallationDetailView.as_view(),
        name='detail_installation'
    ),
    path(
        'delete_installation/<pk>/',
        views.InstallationDeleteView.as_view(),
        name='delete_installation'
    ),
    path(
        'list_installations_by_station/<pk>/',
        views.InstallationListByStationView.as_view(),
        name='list_installations_by_station'
    ),
]