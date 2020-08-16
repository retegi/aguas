from django.urls import include,path
from . import views

app_name = 'installations_app'

urlpatterns = [
    path('',
        views.InstalacionList.as_view(),
        name='list_installation'
    ),
    path('add_installation',
        views.InstalacionAdd.as_view(),
        name='add_installation'
    ),
    path(
        'update_installation/<pk>/',
        views.InstalacionUpdateView.as_view(),
        name='update_installation'
    ),
    path(
        'detail_installation/<pk>/',
        views.InstalacionDetailView.as_view(),
        name='detail_installation'
    ),
    path(
        'delete_installation/<pk>/',
        views.InstalacionDeleteView.as_view(),
        name='delete_installation'
    ),
]