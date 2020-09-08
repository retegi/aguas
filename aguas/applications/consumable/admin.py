from django.contrib import admin
from .models import Consumable
from applications.device.models import Device
from .models import ImageConsumable
from .models import TypeModelConsumable
from .models import TypeConsumable
from .models import StatusConsumable
from .models import VoltageOutputConsumable



class ImageConsumableAdmin(admin.ModelAdmin):
    list_display = (
        'name_imageConsumable',
        'image_imageConsumable',
    )
admin.site.register(ImageConsumable,ImageConsumableAdmin)

class VoltageOutputConsumableAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(VoltageOutputConsumable,VoltageOutputConsumableAdmin)

class TypeModelConsumableAdmin(admin.ModelAdmin):
    list_display = (
        'type_consumable_typeConsumable',
        'brand_typeConsumable',
        'model_typeConsumable',
        'VoltageOutput_typeConsumable',
        'observations_typeConsumable',
    )
admin.site.register(TypeModelConsumable,TypeModelConsumableAdmin)

class TypeConsumableAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(TypeConsumable,TypeConsumableAdmin)

class ConsumableAdmin(admin.ModelAdmin):
    list_display = (
        'datetime_placemente_consumable',
        'serial_num_consumable',
        'parent_device_consumable',
        'status_consumable',
        'observations_consumable',
    )
admin.site.register(Consumable,ConsumableAdmin)

class StatusConsumableAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'color_html_background',
    )
admin.site.register(StatusConsumable,StatusConsumableAdmin)

