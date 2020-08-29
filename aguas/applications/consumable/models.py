from django.db import models
from applications.device.models import Device
from applications.station.models import Station
from applications.installation.models import Installation

class ImageConsumable(models.Model):
    name_imageConsumable = models.CharField('Nombre',max_length=50)
    image_imageConsumable = models.ImageField(upload_to='consumibles/')

    class Meta:
        verbose_name = 'Imagen consumible'
        verbose_name_plural = 'Imagen de consumibles'
        ordering = ['name_imageConsumable']

    def __str__(self):
        return self.name_imageConsumable

# Create your models here.
class TypeConsumable(models.Model):
    CONSUMIBLE_TYPE_CHOICE = (
        ('0','Batería'),
        ('1','Otro'),
    )
    type_typeConsumable = models.CharField('TipoConsumible', max_length=1, choices=CONSUMIBLE_TYPE_CHOICE,null=True)

    brand_typeConsumable = models.CharField('Marca',max_length=50,null=True, blank=True)
    model_typeConsumable = models.CharField('Modelo',max_length=50,null=True, blank=True)
    SALIDA_VOLTAJE_TYPE_CHOICE = (
        ('0','7.2V'),
        ('1','3.6V'),
    )
    voltage_ouput_typeConsumable = models.CharField('SalidaVoltaje', max_length=1, choices=SALIDA_VOLTAJE_TYPE_CHOICE,null=True)
    imagen_typeConsumable = models.ForeignKey(ImageConsumable, on_delete=models.CASCADE,null=True, blank=True)
    observations_typeConsumable = models.CharField('Observaciones', max_length=50,null=True, blank=True)

    class meta:
        verbose_name = 'Tipo Consumible'
        verbose_name_plural = 'Tipo de Consumibles'

    def __str__(self):
        return str(self.get_type_typeConsumable_display()) + ' ' +  str(self.brand_typeConsumable) + ' ' + str(self.model_typeConsumable) + ' ' + str(self.get_voltage_ouput_typeConsumable_display())


class StatusConsumable(models.Model):
    name = models.CharField('Nombre',max_length=50)
    color_html_background = models.CharField('Color HTML incluir #', max_length=7,null=True, blank=True)

    class Meta:
        verbose_name = 'Estado consumible'
        verbose_name_plural = 'Estados del consumible'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Consumable(models.Model):
    datetime_placemente_consumable = models.DateTimeField ('FechaColocacion',null=True, blank=True)
    type_consumable = models.ForeignKey(TypeConsumable, on_delete=models.CASCADE,null=True, blank=True)
    serial_num_consumable = models.CharField('NºSerie',max_length=100,null=True, blank=True)
    parent_device_consumable = models.ForeignKey(Device, on_delete=models.CASCADE,null=True, blank=True)
    status_consumable = models.ForeignKey(StatusConsumable, on_delete=models.CASCADE,null=True, blank=True)
    observations_consumable = models.CharField('Observaciones', max_length=50,null=True, blank=True)

    class meta:
        verbose_name = 'Consumible'
        verbose_name_plural = 'Consumibles'

    def __str__(self):
        return str(self.serial_num_consumable) + '' + str(self.type_consumable) + '' + str(self.status_consumable)