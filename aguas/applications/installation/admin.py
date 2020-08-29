from django.contrib import admin
from .models import Installation
from .models import TypeInstallation
from .models import ImageInstallation


class InstallationAdmin(admin.ModelAdmin):
    list_display = (
        'type_installation',
        'station_installation',
        'observations_installation',
    )
admin.site.register(Installation,InstallationAdmin)

class TypeInstallationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(TypeInstallation,TypeInstallationAdmin)

class ImageInstallationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(ImageInstallation,ImageInstallationAdmin)