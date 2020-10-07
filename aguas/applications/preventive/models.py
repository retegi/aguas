from django.db import models
from applications.station.models import Station
from applications.station.models import StatusStation

class RevisionPorcentage(models.Model):
    num_revisionPorcentage = models.CharField('Porcentage', max_length=30)

    class Meta:
        verbose_name = 'Porcentaje de revisión'
        verbose_name_plural = 'Porcentajes de revisión'
        ordering = ['id']
    
    def __str__(self):
        return str(self.num_revisionPorcentage)

class StatusPreventive(models.Model):
    name_statusPreventive = models.CharField('Estado', max_length=30)

    class Meta:
        verbose_name = 'Estado del preventivo'
        verbose_name_plural = 'Estados del preventivo'
        ordering = ['id']
    
    def __str__(self):
        return str(self.name_statusPreventive)

class Preventive(models.Model):
    #code_preventive = models.CharField('Código preventive', max_length=10)
    startDatetime_preventive = models.DateTimeField ('FechaComienzo Preventivo',null=True, blank=True)
    
    station_preventive = models.ForeignKey(Station, on_delete=models.CASCADE,null=True, blank=True)
    


    #Preventive Questions
    #PLC
    #autVisualInspectionOfAlarmLedStatus_preventive
    AlarmLedStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    ) 
    autVisualInspectionOfAlarmLedStatus_preventive = models.CharField('Estado de LEDs de alarma', max_length = 20, choices = AlarmLedStatus_CHOICES, default = '1', null=True, blank=True) 
    autVisualInspectionOfAlarmLedStatusNoOkDetail_preventive = models.TextField('Observaciones estado de LEDs de alarma', max_length=300, null=True, blank=True)

    #autLithiumBatteryStatus_preventive
    LithiumBatteryStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    ) 
    autLithiumBatteryStatus_preventive = models.CharField('Estado de batería de litio', max_length=40, choices = LithiumBatteryStatus_CHOICES, null=True, blank=True, default = '1')
    autLithiumBatteryStatusNoOkDetail_preventive = models.TextField('Observaciones estado de baterías de litio', max_length=300, null=True, blank=True)

    #autHardwareDiagnosis_preventive
    HardwareDiagnosisStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    autHardwareDiagnosis_preventive = models.CharField('Diagnóstico de Hardware', max_length=40, choices = HardwareDiagnosisStatus_CHOICES, null=True, blank=True, default = '1')
    autHardwareDiagnosisNoOkDetail_preventive = models.TextField('Observaciones diagnóstico de Hardware', max_length=300, null=True, blank=True)

    #autDIandAIinCCStatus_preventive
    DIandAIinCCStatusStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    autDIandAIinCCStatus_preventive = models.CharField('ED y EA que puedan estar dudosas en CC', max_length=40, null=True, blank=True, choices = DIandAIinCCStatusStatus_CHOICES, default = '1')
    autDIandAIinCCStatusNoOkDetail_preventive = models.TextField('Observaciones ED y EA que puedan estar dudosas en CC', max_length=300, null=True, blank=True)

    #autcheckRxTxOnCommunicationCards_preventive
    CheckRxTxOnCommunicationCardsStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    autcheckRxTxOnCommunicationCards_preventive = models.CharField('Comprobar Rx yTx en tarjetas de comunicaciones', max_length=40, choices = CheckRxTxOnCommunicationCardsStatus_CHOICES, default = '1', null=True, blank=True)
    autcheckRxTxOnCommunicationCardsNoOkDetail_preventive = models.TextField('Observaciones comprobar Rx yTx en tarjetas de comunicaciones', max_length=300, null=True, blank=True)







    #GENERAL
    #genventilationSystemAndThermostat_preventive
    GenventilationSystemAndThermostatStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    genventilationSystemAndThermostat_preventive = models.CharField('Sistema de ventilación y termostato', max_length=40, choices = GenventilationSystemAndThermostatStatus_CHOICES, default = '1', null=True, blank=True)
    genventilationSystemAndThermostatNoOkDetail_preventive = models.TextField('Observaciones sistema de ventilación y termostato', max_length=300, null=True, blank=True)

    #gencleaningVentilationFilters_preventive
    GencleaningVentilationFiltersStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    gencleaningVentilationFilters_preventive = models.CharField('Limpieza de filtros de ventilación', max_length=40, choices = GencleaningVentilationFiltersStatus_CHOICES, default = '1', null=True, blank=True)
    gencleaningVentilationFiltersNoOkDetail_preventive = models.TextField('Observaciones limpieza de filtros de ventilación', max_length=300, null=True, blank=True)

    #genfreeOfCorrosion_preventive
    GenfreeOfCorrosion_preventiveStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    genfreeOfCorrosion_preventive = models.CharField('Libre de corrosión', max_length=40, choices = GenfreeOfCorrosion_preventiveStatus_CHOICES, default = '1', null=True, blank=True)
    genfreeOfCorrosionNoOkDetail_preventive = models.TextField('Observaciones libre de corrosión', max_length=300, null=True, blank=True)

    #genelementCleaning_preventive
    GenelementCleaning_preventiveStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    genelementCleaning_preventive = models.CharField('Limpieza de elementos', max_length=40, choices = GenelementCleaning_preventiveStatus_CHOICES, default = '1', null=True, blank=True)
    genelementCleaningNoOkDetail_preventive = models.TextField('Observaciones limpieza de elementos', max_length=300, null=True, blank=True)

    #genupdatedSignalList_preventive
    GenupdatedSignalList_preventiveStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    genupdatedSignalList_preventive = models.CharField('Lista de señales actualizada', max_length=40, choices = GenupdatedSignalList_preventiveStatus_CHOICES, default = '1', null=True, blank=True)
    genupdatedSignalListNoOkDetail_preventive = models.TextField('Observaciones lista de señales actualizada', max_length=300, null=True, blank=True)



    #SAI
    #saistatusOfConnectorsAndLEDs_preventive
    SaiStatusOfConnectorsAndLEDsStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    saistatusOfConnectorsAndLEDs_preventive = models.CharField('Estado de conectores y Leds', max_length=40, choices = SaiStatusOfConnectorsAndLEDsStatus_CHOICES, default = '1', null=True, blank=True)
    saistatusOfConnectorsAndLEDsNoOkDetail_preventive = models.TextField('Observaciones estado de conectores y Leds', max_length=300, null=True, blank=True)

    #saiinputVoltageMeasurement_preventive
    saiinputVoltageMeasurement_preventive = models.CharField('Medida de tensión de entrada', max_length=40, null=True, blank=True)

    #saioutputVoltageToConsumption_preventive
    saioutputVoltageToConsumption_preventive = models.CharField('Comprobar tensión de salida a consumo', max_length=40, null=True, blank=True)


    #saibatteryStatus_preventive
    SaiBatteryStatus_preventiveStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    saibatteryStatus_preventive = models.CharField('Estado de las baterías', max_length=40, choices = SaiBatteryStatus_preventiveStatus_CHOICES, default = '1', null=True, blank=True)
    saibatteryStatusNoOkDetail_preventive = models.TextField('Observaciones estado de las baterías', max_length=300, null=True, blank=True)

    #saicleaning_preventive
    SaiCleaning_preventiveStatus_CHOICES = ( 
        ("1","OK"), 
        ("2","No OK"),
        ("3","NP"),
    )
    saicleaning_preventive = models.CharField('Limpieza, si procede', max_length=40, choices = SaiCleaning_preventiveStatus_CHOICES, default = '1', null=True, blank=True)
    saicleaningNoOkDetail_preventive = models.TextField('Observaciones limpieza, si procede', max_length=300, null=True, blank=True)
    status_preventive = models.ForeignKey(StatusPreventive, on_delete=models.CASCADE,null=True, blank=True)
    revisionPorcentage_preventive = models.ForeignKey(RevisionPorcentage, on_delete=models.CASCADE,null=True, blank=True)

    endDatetime_preventive = models.DateTimeField ('Fecha finalización Preventivo',null=True, blank=True)
    totalEstimatedTime_preventive = models.IntegerField('Tiempo estimado minutos', null=True, blank=True)
    observations_preventive = models.TextField('Observaciones',null=True, blank=True)

    class Meta:
        verbose_name = 'Mant Preventivo'
        verbose_name_plural = 'Mant Preventivos'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + ' - ' + ' - ' + str(self.station_preventive)



class PartName(models.Model):
    name_partName = models.CharField('nombre', max_length=40)
    acronym_partName = models.CharField('acrónimo', max_length=12, null=True, blank=True)

    class Meta:
        verbose_name = 'Nombre de parte de revisión'
        verbose_name_plural = 'Nombres de partes de revisión'
        ordering = ['name_partName']

    def __str__(self):
        return str(self.name_partName)


class ContractPreventive(models.Model):
    annualPreventiveContract_ContractPreventive = models.IntegerField('Cantidad de preventivos en contrato', null=True, blank=True)
    
    class Meta:
        verbose_name = 'Contrato mantenimiento preventivo'
        verbose_name_plural = 'contratos mantenimientos preventivos'
        ordering = ['annualPreventiveContract_ContractPreventive']

    def __str__(self):
        return str(self.annualPreventiveContract_ContractPreventive)


class ContractedCompanyPreventive(models.Model):
    name_contractedCompanyPrevent = models.CharField('Nombre empresa contratada Mant Preventivo', max_length=40, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Empresa contratada mantenimiento preventivo'
        verbose_name_plural = 'Empresas contratadas mantenimiento preventivo'
        ordering = ['name_contractedCompanyPrevent']

    def __str__(self):
        return str(self.name_contractedCompanyPrevent)









