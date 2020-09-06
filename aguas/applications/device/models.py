from django.db import models
from applications.station.models import Station
from applications.installation.models import Installation
from simple_history.models import HistoricalRecords


class ImageDevice(models.Model):
    name = models.CharField('Nombre',max_length=50)
    image_device = models.ImageField(upload_to='devices/')

    class Meta:
        verbose_name = 'Imagen dispositivo'
        verbose_name_plural = 'Imagen de dispositivos'
        ordering = ['name']

    def __str__(self):
        return self.name

class CommunicationDevice(models.Model):
    name = models.CharField('Nombre',max_length=50)

    class Meta:
        verbose_name = 'Comunicación del dispositivo'
        verbose_name_plural = 'Comunicaciones de dispositivos'
        ordering = ['name']

    def __str__(self):
        return self.name

class FileDevice(models.Model):
    name = models.CharField('Nombre',max_length=50)
    url_file = models.CharField('Url',max_length=50)


    class Meta:
        verbose_name = 'Archivo dispositivo'
        verbose_name_plural = 'Archivos de dispositivo'
        ordering = ['name']

    def __str__(self):
        return self.name

class TypeDevice(models.Model):
    name = models.CharField('Nombre',max_length=50)

    class Meta:
        verbose_name = 'Tipo dispositivo'
        verbose_name_plural = 'Tipos de dispositivos'
        ordering = ['name']

    def __str__(self):
        return self.name

class BrandDevice(models.Model):
    name = models.CharField('Nombre',max_length=50)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['name']

    def __str__(self):
        return self.name

class ProductModelDevice(models.Model):
    type_device = models.ForeignKey(TypeDevice, max_length=1,on_delete=models.CASCADE,null=True, blank=True)
    brand_device = models.ForeignKey(BrandDevice, max_length=1,on_delete=models.CASCADE,null=True, blank=True)
    #brand_device = models.CharField('Marca',max_length=50,null=True, blank=True)
    model_device = models.CharField('Modelo',max_length=50,null=True, blank=True)
    communication_device = models.ForeignKey(CommunicationDevice, max_length=1,on_delete=models.CASCADE,null=True, blank=True)
    image_device = models.ForeignKey(ImageDevice, on_delete=models.CASCADE,null=True, blank=True)
    file_device = models.ForeignKey(FileDevice, on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['brand_device']

    def __str__(self):
        return self.brand_device



# Create your models here.
class Device(models.Model):
    #fecha_actuacion = models.DateTimeField ('Fecha edición',null=True, blank=True)
    product_model_device =models.ForeignKey(ProductModelDevice, on_delete=models.CASCADE,null=True, blank=True)
    serial_device = models.CharField('NºSerie',max_length=100,null=True, blank=True)
    ip_device = models.CharField('IP',max_length=100,null=True, blank=True)
    pin_device = models.CharField('PIN',max_length=100,null=True, blank=True)
    puk_device = models.CharField('PUK',max_length=100,null=True, blank=True)
    slave_num_device = models.CharField('Nº Esclavo',max_length=100,null=True, blank=True)
    tel_long_device = models.CharField('Tel LARGO',max_length=100,null=True, blank=True)
    tel_short_device = models.CharField('Tel CORTO',max_length=100,null=True, blank=True)
    parent_device =  models.ForeignKey ('self', null=True, on_delete=models.CASCADE, blank=True)
    installation_device = models.ForeignKey(Installation, on_delete=models.CASCADE,null=False, blank=False)
    observations_device = models.TextField('Observaciones',null=True, blank=True)
    #history = HistoricalRecords()

    class Meta:
        verbose_name = 'Dispositivo'
        verbose_name_plural = 'Dispositivos'
        ordering = ['installation_device']

    def __str__(self):
        return str(self.serial_device) + ' - ' + str(self.installation_device.type_installation.name) + ' - ' + str(self.installation_device.station_installation.name_station)