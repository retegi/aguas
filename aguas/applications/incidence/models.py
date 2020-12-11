from django.db import models
from applications.station.models import Station
from applications.company.models import Company

class TypeIncidence(models.Model):
    name = models.CharField('Tipo de incidencia', max_length=50)
    color_html_background = models.CharField('Color fondo html incluir #', max_length=20)

    class Meta:
        verbose_name = 'Tipo de incidencia'
        verbose_name_plural = 'Tipos de incidencia'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class StatusIncidence(models.Model):
    name = models.CharField('Tipo de incidencia', max_length=50)
    color_html_background = models.CharField('Color fondo html incluir #', max_length=20)

    class Meta:
        verbose_name = 'Estado de incidencia'
        verbose_name_plural = 'Estados de incidencia'
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class UrgencyLevelIncidence(models.Model):
    name = models.CharField('Nivel de urgencia', max_length=50)
    color_html_background = models.CharField('Color fondo html incluir #', max_length=20)
    meaning = models.CharField('Significado', max_length=50,null=True, blank=True)

    class Meta:
        verbose_name = 'Nivel de urgencia'
        verbose_name_plural = 'Niveles de urgencia'
        ordering = ['-id']

    def __str__(self):
        return str(self.name)

"""class RepairForecast(models.Model):
    date_RF = models.DateTimeField('Fecha prevista reparación',null=True, blank=True)
    incidence_RF = models.ForeignKey(Incidence, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Fecha prevista reparación'
        verbose_name_plural = 'Fecha prevista reparaciones'
        ordering = ['date_RF']
    
    def __str__(self):
        return str(self.date_RF)"""

class Billing(models.Model):
    STATUS_CONF = (
        ('Envoiced', 'Envoiced'),
        ('Not envoiced', 'Not envoiced'),
        ('Not to envoice', 'Not to envoice'),
    )
    billing_status = models.CharField('Estado facturación', max_length=50, null=True, blank=True)
    html_color = models.CharField('HTML color', max_length=15, null=True, blank=True)
    billing_conf = models.CharField(max_length=20, choices=STATUS_CONF, null=True, blank=True)

    class Meta:
        verbose_name = 'Estado de facturación'
        verbose_name_plural = 'Estados de facturación'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + ' - ' + str(self.billing_status)

class Incidence(models.Model):
    station_incidence = models.ForeignKey(Station, on_delete=models.CASCADE,null=True, blank=True)
    datetime_incidence = models.DateTimeField ('FechaIncidencia',null=True, blank=True)
    observations_incidence = models.TextField('Observaciones',null=True, blank=True)
    typeIncidence_incidence = models.ForeignKey(TypeIncidence, on_delete=models.CASCADE,null=True, blank=True)
    statusIncidence_incidence = models.ForeignKey(StatusIncidence, on_delete=models.CASCADE,null=True, blank=True)
    repairForecast_incidence = models.DateTimeField('Fecha previsión reparación', null=True, blank=True)
    companyRepair_incidence = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    urgencyLevel_incidence = models.ForeignKey(UrgencyLevelIncidence, on_delete=models.CASCADE,null=True, blank=True)
    billing_incidence = models.ForeignKey(Billing, on_delete=models.CASCADE,null=True, blank=True)

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'
        ordering = ['id']

    def __str__(self):
        return str(self.station_incidence) + ' ' + ' - Incidencia: ' +  str(self.id)

