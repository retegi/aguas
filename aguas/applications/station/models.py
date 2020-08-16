from django.db import models
from django import forms
from .managers import StationManager

# Create your models here.

class TypeStation(models.Model):
    name = models.CharField('Tipo estación', max_length=50)
    acronym = models.CharField('Acrónimo', max_length=50,null=True, blank=True)
    class Meta:
        verbose_name = 'Tipo estación'
        verbose_name_plural = 'Tipos de estación'
    def __str__(self):
        return str(self.id) + '-' + str(self.name) + '-' + str(self.acronym)

class AreaStation(models.Model):
    name = models.CharField('Area estación', max_length=50)
    color_html_background = models.CharField('Color HTML', max_length=7,null=True, blank=True)
    class Meta:
        verbose_name = 'Area estación'
        verbose_name_plural = 'Areas de estación'
    def __str__(self):
        return str(self.id) + '-' + str(self.name)

class Station(models.Model):
    #timestamp_station = models.DateTimeField ('Fecha edición',null=True, blank=True)
    code_station = models.CharField('Código',max_length=50,null=True, blank=True)
    name_station = models.CharField('Nombre',max_length=50,null=True, blank=True)
    latitude_station = models.CharField('Latitud',max_length=50,null=True, blank=True)
    longitude_station = models.CharField('Longitud',max_length=50,null=True, blank=True)
    observations_station = models.TextField('Observaciones',null=True, blank=True)
    area_station = models.ForeignKey(AreaStation, on_delete=models.CASCADE,null=True, blank=True)
    origin_watertank = models.ForeignKey ('self', null=True, on_delete=models.CASCADE, blank=True, related_name="origins_wt")
    type_station = models.ForeignKey(TypeStation, on_delete=models.CASCADE,null=True, blank=True)
    comunication_point =  models.ForeignKey ('self', null=True, on_delete=models.CASCADE, blank=True, related_name="comunications_p")
    
    objects = StationManager()

    class Meta:
        verbose_name = 'Estación'
        verbose_name_plural = 'Estaciones'

    def __str__(self):
        #return  [self.name,self.area,self.codigo]
        return str(self.id) + '-' + str(self.name_station)







