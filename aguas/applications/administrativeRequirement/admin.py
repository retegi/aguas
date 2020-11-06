from django.contrib import admin
from .models import AdministrativeRequirement
from .models import Status
from .models import Anomaly



# Register your models here.
class AdministrativeRequirementAdmin(admin.ModelAdmin):
    list_display=(
        'number_AR',
        'datetime_AR',
        'status_AR',
        'reasonRequirement_AR',
        'observations_AR',
        'file_AR',
    )
admin.site.register(AdministrativeRequirement,AdministrativeRequirementAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display=(
        'status',
        'color_status',
    )
admin.site.register(Status,StatusAdmin)

class AnomalyAdmin(admin.ModelAdmin):
    list_display=(
        'anomaly',
        'color_anomaly',
    )
admin.site.register(Anomaly,AnomalyAdmin)

