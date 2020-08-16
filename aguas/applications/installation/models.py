from django.db import models
from applications.station.models import Station

# Create your models here.
class TypeInstallation(models.Model):
    name = models.CharField('Nombre',max_length=50)

    class Meta:
        verbose_name = 'TipoInstalación'
        verbose_name_plural = 'TipoInstalaciones'
        ordering = ['name']

    def __str__(self):
        return self.name

class Installation(models.Model):
    type_installation = models.ForeignKey(TypeInstallation, on_delete=models.CASCADE,null=True)
    station_installation = models.ForeignKey(Station, on_delete=models.CASCADE,null=True, blank=True)
    observations_installation = models.TextField('Observaciones',null=True, blank=True)

    class Meta:
        verbose_name = 'Instalación'
        verbose_name_plural = 'Instalaciones'
        ordering = ['station_installation']

    def __str__(self):
        return str(self.station_installation) + ' - ' + str(self.type_installation)

