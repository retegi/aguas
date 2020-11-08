from django.urls import include,path
from . import views

app_name = 'requirement_app'

urlpatterns = [
    path(
        '',
        views.AdministrativeRequirementListView.as_view(),
        name='list_requirement'
    ),
    path(
        'add_requirement',
        views.AdministrativeRequirementCreateView.as_view(),
        name='add_requirement'
    )
]