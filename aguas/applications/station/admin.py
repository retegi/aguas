from django.contrib import admin
from .models import Station
from .models import AreaStation
from .models import ImageStation
from .models import StatusStation
from .models import Simulator3DStation
from .models import TypeStation
from .models import CommunicationTechnologyStation
from .models import VideoStation
from .models import DocStation

class StationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name_station',
        'area_station',
        'type_station',
        'observations_station',
    )
admin.site.register(Station,StationAdmin)

class DocStationAdmin(admin.ModelAdmin):
    list_display = (
        'name_docStation',
        'url_docStation',
    )
admin.site.register(DocStation,DocStationAdmin)

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

class Simulator3DStationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
    )
admin.site.register(Simulator3DStation,Simulator3DStationAdmin)


class TypeStationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'acronym',
    )
admin.site.register(TypeStation,TypeStationAdmin)


class CommunicationTechnologyStationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'acronym',
        'url',
    )
admin.site.register(CommunicationTechnologyStation,CommunicationTechnologyStationAdmin)

class VideoStationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'url',
    )
admin.site.register(VideoStation,VideoStationAdmin)