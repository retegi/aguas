from django.contrib import admin

from .models import ImageDevice
from .models import CommunicationDevice
from .models import DocDevice
from .models import TypeDevice
from .models import ProductModelDevice
from .models import Device
from .models import BrandDevice



class ImageDeviceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(ImageDevice,ImageDeviceAdmin)


class BrandDeviceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(BrandDevice,BrandDeviceAdmin)



class CommunicationDeviceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(CommunicationDevice,CommunicationDeviceAdmin)



class DocDeviceAdmin(admin.ModelAdmin):
    list_display = (
        'name_docDevice',
        'url_docDevice',
    )
admin.site.register(DocDevice,DocDeviceAdmin)



class TypeDeviceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
admin.site.register(TypeDevice,TypeDeviceAdmin)



class ProductModelDeviceAdmin(admin.ModelAdmin):
    list_display = (
        #'type_device',
        'brand_device',
        'model_device',
    )
admin.site.register(ProductModelDevice,ProductModelDeviceAdmin)


class DeviceAdmin(admin.ModelAdmin):
    list_display = (
        #'product_device',
        'serial_device',
        'ip_device',
    )
admin.site.register(Device,DeviceAdmin)