from django.contrib import admin
from .models import Station
from .models import TypeStation
from .models import AreaStation

class StationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_station',
        'area_station',
        'observations_station',
    )
admin.site.register(Station,StationAdmin)


class TypeStationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'acronym',
    )
admin.site.register(TypeStation,TypeStationAdmin)

class AreaStationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color_html_background',
    )
admin.site.register(AreaStation,AreaStationAdmin)


