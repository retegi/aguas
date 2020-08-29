from django.urls import include,path
from . import views

app_name = 'incidences_app'

urlpatterns = [
    path(
        '',
        views.IncidenceList.as_view(),
        name='list_incidence'
    ),
    path(
        'add_incidence',
        views.IncidenceAdd.as_view(),
        name='add_incidence'
    ),
    path(
        'detail_incidence/<pk>/',
        views.IncidenceDetailView.as_view(),
        name='detail_incidence'
    ),
    path(
        'update_incidence/<pk>/',
        views.IncidenceUpdateView.as_view(),
        name='update_incidence'
    ),
    path(
        'delete_incidence/<pk>/',
        views.IncidenceDeleteView.as_view(),
        name='delete_incidence'
    )
]