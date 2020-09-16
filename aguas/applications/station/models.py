from django.db import models
from django import forms
from .managers import StationManager

# Create your models here.

class Simulator3DStation(models.Model):
    name = models.CharField('Descripción de url', max_length=50)
    url = models.TextField('Url', max_length=500,null=True, blank=True)
    #url = models.TextField(blank=True)
    class Meta:
        verbose_name = 'Simulación 3D'
        verbose_name_plural = 'Simulaciones 3D'
    def __str__(self):
        return str(self.id) + '-' + str(self.name) + '-' + str(self.url)

class VideoStation(models.Model):
    name = models.CharField('Descripción de url', max_length=50)
    url = models.TextField('Url', max_length=500,null=True, blank=True)

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
    def __str__(self):
        return str(self.id) + '-' + str(self.name) + '-' + str(self.url)



class AreaStation(models.Model):
    name = models.CharField('Area estación', max_length=50)
    color_html_background = models.CharField('Color HTML', max_length=7,null=True, blank=True)
    class Meta:
        verbose_name = 'Area estación'
        verbose_name_plural = 'Areas de estación'
    def __str__(self):
        return str(self.id) + '-' + str(self.name)

class ImageStation(models.Model):
    name = models.CharField('Nombre',max_length=50)
    image_imageStation = models.ImageField(upload_to='stations/')

    class Meta:
        verbose_name = 'Imagen estación'
        verbose_name_plural = 'Imagen de estaciones'
        ordering = ['name']

    def __str__(self):
        return str(self.image_imageStation)

class DocStation(models.Model):
    name_docStation = models.CharField('Nombre',max_length=50)
    url_docStation = models.CharField('Url',max_length=200,null=True, blank=True)

    class Meta:
        verbose_name = 'Doc estación'
        verbose_name_plural = 'Doc de estaciones'
        ordering = ['name_docStation']

    def __str__(self):
        return str(self.name_docStation)

class StatusStation(models.Model):
    name = models.CharField('Nombre',max_length=50)
    color_html_background = models.CharField('Color HTML', max_length=7,null=True, blank=True)

    class Meta:
        verbose_name = 'Estado estación'
        verbose_name_plural = 'Estados de la estación'
        ordering = ['name']

    def __str__(self):
        return str(self.name)

class TypeStation(models.Model):
    name = models.CharField('Tipo estación', max_length=100)
    acronym = models.CharField('Acrónimo', max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = 'Tipo estación'
        verbose_name_plural = 'Tipos de estaciones'
    def __str__(self):
        return str(self.name)

class CommunicationTechnologyStation(models.Model):
    name = models.CharField('Acrónimo',max_length=100)
    acronym = models.CharField('Significado',max_length=40)
    url = models.CharField('URL',max_length=150,null=True, blank=True)

    class Meta:
        verbose_name = 'Tecnología de comunicación'
        verbose_name_plural = 'Tecnologías de comunicación'
        ordering = ['name']

    def __str__(self):
        return str(self.name)

class Station(models.Model):
    communication_technology_station = models.ForeignKey(CommunicationTechnologyStation, on_delete=models.CASCADE,null=True, blank=True,db_column='Tecnología de comunicación')
    code_station = models.CharField('Código',max_length=50,null=True, blank=True)
    name_station = models.CharField('Nombre',max_length=50,null=True, blank=True)
    latitude_station = models.CharField('Latitud',max_length=50,null=True, blank=True)
    longitude_station = models.CharField('Longitud',max_length=50,null=True, blank=True)
    observations_station = models.TextField('Observaciones',null=True, blank=True)
    communication_windows_station = models.TextField('ventana de comunicación',null=True, blank=True)
    area_station = models.ForeignKey(AreaStation, on_delete=models.CASCADE,null=True, blank=True)
    origin_watertank = models.ForeignKey ('self', null=True, on_delete=models.CASCADE, blank=True, related_name="origins_wt")
    type_station = models.ForeignKey(TypeStation, on_delete=models.CASCADE,null=True, blank=True)
    comunication_point =  models.ForeignKey ('self', null=True, on_delete=models.CASCADE, blank=True, related_name="comunications_p")
    image_station = models.ManyToManyField(ImageStation, blank=True)
    status_station =  models.ForeignKey(StatusStation, on_delete=models.CASCADE,null=True, blank=True)
    simulator3D_station =  models.ForeignKey(Simulator3DStation, on_delete=models.CASCADE,null=True, blank=True)
    video_station =  models.ManyToManyField(VideoStation, blank=True)
    doc_station =  models.ManyToManyField(DocStation, blank=True)

    objects = StationManager()

    class Meta:
        verbose_name = 'Estación'
        verbose_name_plural = 'Estaciones'

    def __str__(self):
        #return  [self.name,self.area,self.codigo]
        return str(self.name_station)







