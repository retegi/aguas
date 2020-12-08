from django.db import models
from applications.device.models import Device
from applications.consumable.models import Consumable
from applications.incidence.models import Incidence
from applications.company.models import Company
from applications.employee.models import Employee


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
    color_html_background = models.CharField('Color HTML', max_length=7,null=True, blank=True)

    class Meta:
        verbose_name = 'Nuevo estado'
        verbose_name_plural = 'Nuevos estados'
        ordering = ['name']

    def __str__(self):
        return self.name

"""class RepairForecast(models.Model):
    date_RF = models.DateTimeField('Fecha prevista reparación',null=True, blank=True)

    class Meta:
        verbose_name = 'Fecha prevista reparación'
        verbose_name_plural = 'Fecha prevista reparaciones'
        ordering = ['date_RF']
    
    def __str__(self):
        return self.date_RF"""


# Create your models here.
class Repair(models.Model):
    startDatetime_repair = models.DateTimeField ('Fecha comienzo reparación',null=True, blank=True)
    endDatetime_repair = models.DateTimeField ('Fecha finalización reparación',null=True, blank=True)
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
    productsToInvoice_repair = models.TextField('Material a facturar',null=True, blank=True)
    company_repair = models.ForeignKey(Company, on_delete=models.CASCADE,null=True, blank=True)
    employee_preventive = models.ManyToManyField(Employee, related_name="correctives")
    

    class meta:
        verbose_name = 'Reparación'
        verbose_name_plural = 'Reparaciones'
        ordering = ['id']

    def __str__(self):
        return self.summary_repair


class ContractedCompanyRepair(models.Model):
    name_contractedCompanyRepair = models.CharField('Nombre empresa contratada Mant Correctivo', max_length=40, null=True, blank=True)

    class Meta:
        verbose_name = 'Empresa contratada mantenimiento correctivo'
        verbose_name_plural = 'Empresas contratadas mantenimiento correctivo'
        ordering = ['name_contractedCompanyRepair']

    def __str__(self):
        return str(self.name_contractedCompanyRepair)

