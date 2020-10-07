from django.contrib import admin
from .models import Preventive
from .models import StatusPreventive
from .models import RevisionPorcentage
#from .models import PartPreventive
from .models import PartName
from .models import ContractPreventive
from .models import ContractedCompanyPreventive

class ContractedCompanyPreventiveAdmin(admin.ModelAdmin):
    list_display = (
        'name_contractedCompanyPrevent',
    )
admin.site.register(ContractedCompanyPreventive,ContractedCompanyPreventiveAdmin)

class ContractPreventiveAdmin(admin.ModelAdmin):
    list_display = (
        'annualPreventiveContract_ContractPreventive',
    )
admin.site.register(ContractPreventive,ContractPreventiveAdmin)

class PartNameAdmin(admin.ModelAdmin):
    list_display = (
        'name_partName',
        'acronym_partName',
    )
admin.site.register(PartName,PartNameAdmin)

class RevisionPorcentageAdmin(admin.ModelAdmin):
    list_display = (
        'num_revisionPorcentage',
    )
admin.site.register(RevisionPorcentage,RevisionPorcentageAdmin)

class StatusPreventiveAdmin(admin.ModelAdmin):
    list_display = (
        'name_statusPreventive',
    )
admin.site.register(StatusPreventive,StatusPreventiveAdmin)

class PreventiveAdmin(admin.ModelAdmin):
    list_display = (
        #'code_preventive',
        'startDatetime_preventive',
        'endDatetime_preventive',
        'station_preventive',
        'observations_preventive',
        'status_preventive',
        'revisionPorcentage_preventive',
        #QUESTIONS

        #AUTOMATA
        'autVisualInspectionOfAlarmLedStatus_preventive',
        'autLithiumBatteryStatus_preventive',
        'autHardwareDiagnosis_preventive',
        'autDIandAIinCCStatus_preventive',
        'autcheckRxTxOnCommunicationCards_preventive',

        #GENERAL
        'autVisualInspectionOfAlarmLedStatus_preventive',
        'autLithiumBatteryStatus_preventive',
        'autHardwareDiagnosis_preventive',
        'autDIandAIinCCStatus_preventive',
        'autcheckRxTxOnCommunicationCards_preventive',

        #GENERAL
        'genventilationSystemAndThermostat_preventive',
        'gencleaningVentilationFilters_preventive',
        'genfreeOfCorrosion_preventive',
        'genelementCleaning_preventive',
        'genupdatedSignalList_preventive',
        #SAI
        'saistatusOfConnectorsAndLEDs_preventive',
        'saiinputVoltageMeasurement_preventive',
        'saioutputVoltageToConsumption_preventive',
        'saibatteryStatus_preventive',
        'saicleaning_preventive',
    )
admin.site.register(Preventive,PreventiveAdmin)