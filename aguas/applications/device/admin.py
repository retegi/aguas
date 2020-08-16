from django.contrib import admin
from .models import Device
from .models import TypeDevice
from .models import ImageDevice


class TypeDeviceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(TypeDevice,TypeDeviceAdmin)

class ImageDeviceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(ImageDevice,ImageDeviceAdmin)

class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        'type_device',
        'brand_device',
        'model_device',
        'serial_device',
        'ip_device',
        'image_device',
        #'estacion',
    )
admin.site.register(Device,DeviceAdmin)