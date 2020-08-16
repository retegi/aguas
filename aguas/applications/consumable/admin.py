from django.contrib import admin
from .models import Consumable
from applications.device.models import Device
from .models import ImageConsumable
from .models import TypeConsumable

class ImageConsumableAdmin(admin.ModelAdmin):
    list_display = (
        'name_imageConsumable',
        'image_imageConsumable',
    )
admin.site.register(ImageConsumable,ImageConsumableAdmin)

class TypeConsumableAdmin(admin.ModelAdmin):
    list_display = (
        'type_typeConsumable',
        'brand_typeConsumable',
        'model_typeConsumable',
        'voltage_ouput_typeConsumable',
        'imagen_typeConsumable',
        'observations_typeConsumable',
    )
admin.site.register(TypeConsumable,TypeConsumableAdmin)


class ConsumableAdmin(admin.ModelAdmin):
    list_display = (
        'datetime_placemente_consumable',
        'type_consumable',
        'serial_num_consumable',
        'parent_device_consumable',
        'status_consumable',
        'observations_consumable',
    )
admin.site.register(Consumable,ConsumableAdmin)

