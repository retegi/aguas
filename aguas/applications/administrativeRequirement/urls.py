from django.urls import include,path
from . import views

app_name = 'requirement_app'

urlpatterns = [
    path(
        '',
        views.AdministrativeRequirementListView.as_view(),
        name='list_requirement'
    )
]