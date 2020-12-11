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
        'invoiced_list_incidence',
        views.InvoicedIncidenceList.as_view(),
        name='invoiced_list_incidence'
    ),
    path(
        'not_invoiced_list_incidence',
        views.NotInvoicedIncidenceList.as_view(),
        name='not_invoiced_list_incidence'
    ),
    path(
        'do_not_envoice_list_incidence',
        views.DoNotInvoiceIncidenceList.as_view(),
        name='do_not_envoice_list_incidence'
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
    ),
    path(
        'map_incidence',
        views.IncidenceMapListView.as_view(),
        name='map_incidence'
    ),
]