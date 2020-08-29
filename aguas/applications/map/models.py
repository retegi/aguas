from django.db import models

# Create your models here.

class Map(models.Model):
    name_location = models.CharField('Localidad', max_length=50)
    longitude_conf_map = models.CharField('longitud', max_length=20)
    latitude_conf_map = models.CharField('latitud', max_length=20)
    zoom_conf_map = models.CharField('zoom', max_length=20)

    class Meta:
        verbose_name = 'Mapa'
        verbose_name_plural = 'Mapas'
        ordering = ['name_location']

    def __str__(self):
        return self.name_location