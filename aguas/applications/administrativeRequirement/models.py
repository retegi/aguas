from django.db import models
from applications.streetMap.models import StreetMap
from applications.streetMap.models import Address


#from .models import Address

class Anomaly(models.Model):
    anomaly = models.CharField('Anomalía', max_length=50, null=True, blank=True)
    color_anomaly = models.CharField('Color anomalía', max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = 'Anomalía'
        verbose_name_plural = 'Anomalías'
        ordering = ['anomaly']

    def __str__(self):
        return self.anomaly

class Status(models.Model):
    status = models.CharField('Situación', max_length=30, null=True, blank=True)
    color_status = models.CharField('Color situación', max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = 'Situación'
        verbose_name_plural = 'Situaciones'
        ordering = ['status']
    
    def __str__(self):
        return self.status


class AdministrativeRequirement(models.Model):
    number_AR = models.CharField('Número', max_length=50,null=True, blank=True)
    datetime_AR = models.DateTimeField ('FechaRoa',null=True, blank=True)
    file_AR = models.FileField(upload_to='administrativeRequirement/')
    address_AR = models.ManyToManyField(Address)
    #contact_AR = models.ForeignKey(Contact, on_delete=models.CASCADE,null=True, blank=True)
    anomaly_AR = models.ManyToManyField(Anomaly)
    status_AR = models.ForeignKey(Status, on_delete=models.CASCADE,null=True, blank=True)
    reasonRequirement_AR = models.TextField('Motivo requerimiento', max_length=1000, null=True, blank=True)
    observations_AR = models.TextField('Observaciones', max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = 'Requerimiento'
        verbose_name_plural = 'Requerimientos'
        ordering = ['number_AR']

    def __str__(self):
        return self.number_AR