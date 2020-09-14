from django.db import models
from applications.station.models import Station
from applications.station.models import Installation
from applications.station.models import Device
from applications.station.models import Consumable


class BatteryLevel(models.Model):
    vols_batteryLevel = models.DecimalField('Vols', max_length=10)
    
# Create your models here.
class Preventive(models.Model):
    code_preventive = models.CharField('Código preventive', max_length=10)
    datetime_preventive = models.DateTimeField ('FechaIncidencia',null=True, blank=True)
    station_preventive = models.ForeignKey(Station, on_delete=models.CASCADE,null=True, blank=True)

    batteryLevel_preventive = models.ForeignKey(BatteryLevel, on_delete=models.CASCADE,null=True, blank=True)

    observations_preventive = models.TextField('Observaciones',null=True, blank=True)

    class Meta:
        verbose_name = 'Mant Preventivo'
        verbose_name_plural = 'Mant Preventivos'
        ordering = ['codigo_preventive']

    def __str__(self):
        return str(self.id) + ' - ' + str(self.code_preventive)




