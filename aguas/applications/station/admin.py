from django.contrib import admin
from .models import Station
#from .models import TypeStation
from .models import AreaStation
from .models import ImageStation
from .models import StatusStation
from .models import Simulator3DStation

class Simulator3DStationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
    )
admin.site.register(Simulator3DStation,Simulator3DStationAdmin)

class StationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_station',
        'area_station',
        'type_station',
        'observations_station',
    )
admin.site.register(Station,StationAdmin)


"""class TypeStationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'acronym',
    )
admin.site.register(TypeStation,TypeStationAdmin)"""

class AreaStationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color_html_background',
    )
admin.site.register(AreaStation,AreaStationAdmin)

class ImageStationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(ImageStation,ImageStationAdmin)

class StatusStationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color_html_background',
    )
admin.site.register(StatusStation,StatusStationAdmin)


