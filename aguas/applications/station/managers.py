from django.db import models

class StationManager(models.Manager):
    """Manager para el modelo Stattion"""
    def buscar_estacion(self, kword):
        resultado = self.filter(
            name__icontains=kword
        )
        return resultado