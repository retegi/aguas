from django.contrib import admin
from .models import Map


class MapAdmin(admin.ModelAdmin):
    list_display = (
        'name_location',
        'longitude_conf_map',
        'latitude_conf_map',
        'zoom_conf_map',
        )
admin.site.register(Map,MapAdmin)