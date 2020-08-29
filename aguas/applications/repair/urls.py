from django.urls import include,path
from . import views

app_name = 'repairs_app'

urlpatterns = [
    path(
        '',
        views.RepairListView.as_view(),
        name='list_repair'
    ),
    path(
        'add_repair',
        views.RepairAddView.as_view(),
        name='add_repair'
    ),
    path(
        'detail_repair/<pk>/',
        views.RepairDetailView.as_view(),
        name='detail_repair'
    ),
    path(
        'update_repair/<pk>/',
        views.RepairUpdateView.as_view(),
        name='update_repair'
    ),
    path(
        'delete_repair/<pk>/',
        views.RepairDeleteView.as_view(),
        name='delete_repair'
    ),
    path(
        'list_repairs_by_incidence/<pk>/',
        views.RepairListByIncidenceView.as_view(),
        name='list_repairs_by_incidence'
    ),

]