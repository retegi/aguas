from django.urls import include,path
from . import views

app_name = 'preventive_app'

urlpatterns = [
    path(
        '',
        views.PreventiveList.as_view(),
        name='list_preventive'
    ),
    path(
        'detail_preventive/<pk>/',
        views.PreventiveDetailView.as_view(),
        name='detail_preventive'
    ),
    path('add_preventive',
        views.PreventiveAddView.as_view(),
        name='add_preventive'
    ),
    path(
        'update_preventive/<pk>/',
        views.PreventiveUpdateView.as_view(),
        name='update_preventive'
    ),
    path(
        'delete_preventive/<pk>/',
        views.PreventiveDeleteView.as_view(),
        name='delete_preventive'
    ),
    path(
        'statistics_preventive_detailed',
        views.PreventiveDetailedStatisticsListView.as_view(),
        name='statistics_preventive_detailed'
    ),
    path(
        'statistics_preventive_simplified',
        views.PreventiveSimplifiedStatisticsListView.as_view(),
        name='statistics_preventive_simplified'
    ),    
    path(
        'map_preventive',
        views.PreventiveMapListView.as_view(),
        name='map_preventive'
    ),
]