from django.db import models
from applications.device.models import Device
from applications.consumable.models import Consumable
from applications.incidence.models import Incidence
from simple_history.models import HistoricalRecords


class TypeRepair(models.Model):
    name = models.CharField('Nombre',max_length=50)

    class Meta:
        verbose_name = 'Tipo reparación'
        verbose_name_plural = 'Tipos de reparación'
        ordering = ['name']

    def __str__(self):
        return self.name

class TypeFailure(models.Model):
    name = models.CharField('Nombre',max_length=50)

    class Meta:
        verbose_name = 'Tipo Fallo'
        verbose_name_plural = 'Tipos de fallo'
        ordering = ['name']

    def __str__(self):
        return self.name

class StatusAfterRepair(models.Model):
    name = models.CharField('Nombre',max_length=50)

    class Meta:
        verbose_name = 'Nuevo estado'
        verbose_name_plural = 'Nuevos estados'
        ordering = ['name']

    def __str__(self):
        return self.name

# Create your models here.
class Repair(models.Model):
    datetime_repair = models.DateTimeField ('Fecha actuación',null=True, blank=True)
    incidence_repair = models.ForeignKey(Incidence, related_name="incidencia_repair",on_delete=models.CASCADE,null=True, blank=True)
    affectedDevice_repair = models.ForeignKey(Device, related_name="affectedDevice_repair",on_delete=models.CASCADE,null=True, blank=True)
    typeFailure_repair = models.ForeignKey(TypeFailure, related_name="typeFailure_repair",on_delete=models.CASCADE,null=True, blank=True)
    typeRepair_repair = models.ForeignKey(TypeRepair, related_name="typeRepair_repair",on_delete=models.CASCADE,null=True, blank=True)
    removedDevice_repair = models.ForeignKey(Device, related_name="removedDevice_repair",on_delete=models.CASCADE,null=True, blank=True)
    placedDevice_repair = models.ForeignKey(Device, related_name="placedDevice_repair",on_delete=models.CASCADE,null=True, blank=True)
    removedConsumable_repair = models.ForeignKey(Consumable, related_name="removedConsumable_repair",on_delete=models.CASCADE,null=True, blank=True)
    placedConsumable_repair = models.ForeignKey(Consumable, related_name="placedConsumable_repair",on_delete=models.CASCADE,null=True, blank=True)
    statusAfterRepair_repair = models.ForeignKey(StatusAfterRepair, on_delete=models.CASCADE,null=True, blank=True)
    summary_repair = models.TextField('Resumen',null=True, blank=True)
    detail_repair = models.TextField('Detalles',null=True, blank=True)


    class meta:
        verbose_name = 'Reparación'
        verbose_name_plural = 'Reparaciones'

    def __str__(self):
        return self.summary_repair




