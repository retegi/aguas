from django.contrib import admin
from .models import Repair
from .models import TypeRepair
from .models import TypeFailure
from .models import StatusAfterRepair

class TypeRepairAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        )
admin.site.register(TypeRepair,TypeRepairAdmin)

class TypeFailureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(TypeFailure,TypeFailureAdmin)

class StatusAfterRepairAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(StatusAfterRepair,StatusAfterRepairAdmin)

class RepairAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )
admin.site.register(Repair,RepairAdmin)









"""class ActuacionAdmin(admin.ModelAdmin):
    list_display = (
        'fecha_actuacion',
        'incidencia',
        'dispositivo_afectado',
        'fallo',
        'actuacion',
        'solucionado',
        'resumen_actuacion',
        'detalle_actuacion',
    )

admin.site.register(Actuacion,ActuacionAdmin)"""

