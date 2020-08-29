from django.contrib import admin
from .models import Incidence
from .models import StatusIncidence
from .models import TypeIncidence

class TypeIncidenceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color_html_background',
    )
admin.site.register(TypeIncidence,TypeIncidenceAdmin)

class StatusIncidenceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color_html_background',
    )
admin.site.register(StatusIncidence,StatusIncidenceAdmin)

class IncidenceAdmin(admin.ModelAdmin):
    list_display = (
        'station_incidence',
        'datetime_incidence',
        'observations_incidence',
    )
admin.site.register(Incidence,IncidenceAdmin)