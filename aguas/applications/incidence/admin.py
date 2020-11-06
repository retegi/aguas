from django.contrib import admin
from .models import Incidence
from .models import StatusIncidence
from .models import TypeIncidence
from .models import UrgencyLevelIncidence
#from .models import RepairForecast


"""class RepairForecastAdmin(admin.ModelAdmin):
    list_display = (
        'date_RF',
        'incidence_RF',
    )
admin.site.register(RepairForecast,RepairForecastAdmin)"""

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

class UrgencyLevelIncidenceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color_html_background',
        'meaning',
    )
admin.site.register(UrgencyLevelIncidence,UrgencyLevelIncidenceAdmin)

class IncidenceAdmin(admin.ModelAdmin):
    list_display = (
        'station_incidence',
        'datetime_incidence',
        'repairForecast_incidence',
        'companyRepair_incidence',
        'observations_incidence',
    )
admin.site.register(Incidence,IncidenceAdmin)