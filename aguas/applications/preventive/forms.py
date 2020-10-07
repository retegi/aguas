from django import forms
from .models import Preventive


class AddPreventiveForm(forms.ModelForm):
    class Meta:
        model = Preventive
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddPreventiveForm, self).__init__(*args, **kwargs)
        #VARIOUS1
        #self.fields['code_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['startDatetime_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['station_preventive'].widget.attrs.update({'class': 'form-control'})
        
        #PLC - IF "No OK show textarea"
        #autVisualInspectionOfAlarmLedStatus_preventive
        self.fields['autVisualInspectionOfAlarmLedStatus_preventive'].widget.attrs.update({'name':'autVisualInspectionOfAlarmLedStatus_preventive','class': 'form-control','id':'autVisualInspectionOfAlarmLedStatus_preventive','onchange':'Func_autVisualInspectionOfAlarmLedStatus_preventive()'})
        self.fields['autVisualInspectionOfAlarmLedStatusNoOkDetail_preventive'].widget.attrs.update({'name':'autVisualInspectionOfAlarmLedStatusNoOkDetail_preventive','class': 'form-control','id':'autVisualInspectionOfAlarmLedStatusNoOkDetail_preventive'})
        
        #autLithiumBatteryStatus_preventive
        self.fields['autLithiumBatteryStatus_preventive'].widget.attrs.update({'name':'autLithiumBatteryStatus_preventive','class': 'form-control','id':'autLithiumBatteryStatus_preventive','onchange':'Func_autLithiumBatteryStatus_preventive()'})
        self.fields['autLithiumBatteryStatusNoOkDetail_preventive'].widget.attrs.update({'name':'autLithiumBatteryStatusNoOkDetail_preventive','class':'form-control','id':'autLithiumBatteryStatusNoOkDetail_preventive'})
        
        #autHardwareDiagnosis_preventive
        self.fields['autHardwareDiagnosis_preventive'].widget.attrs.update({'name':'autHardwareDiagnosis_preventive','class': 'form-control','id':'autHardwareDiagnosis_preventive','onchange':'Func_autHardwareDiagnosis_preventive()'})
        self.fields['autHardwareDiagnosisNoOkDetail_preventive'].widget.attrs.update({'name':'autHardwareDiagnosisNoOkDetail_preventive','class': 'form-control','id':'autHardwareDiagnosisNoOkDetail_preventive'})
        
        #autDIandAIinCCStatus_preventive
        self.fields['autDIandAIinCCStatus_preventive'].widget.attrs.update({'name':'autDIandAIinCCStatus_preventive','class': 'form-control','id':'autDIandAIinCCStatus_preventive','onchange':'Func_autDIandAIinCCStatus_preventive()'})
        self.fields['autDIandAIinCCStatusNoOkDetail_preventive'].widget.attrs.update({'name':'autDIandAIinCCStatusNoOkDetail_preventive','class': 'form-control','id':'autDIandAIinCCStatusNoOkDetail_preventive'})

        #autcheckRxTxOnCommunicationCards
        self.fields['autcheckRxTxOnCommunicationCards_preventive'].widget.attrs.update({'name':'autcheckRxTxOnCommunicationCards_preventive','class': 'form-control','id':'autcheckRxTxOnCommunicationCards_preventive','onchange':'Func_autcheckRxTxOnCommunicationCards_preventive()'})
        self.fields['autcheckRxTxOnCommunicationCardsNoOkDetail_preventive'].widget.attrs.update({'name':'autcheckRxTxOnCommunicationCardsNoOkDetail_preventive','class': 'form-control','id':'autcheckRxTxOnCommunicationCardsNoOkDetail_preventive'})

        #GENERAL
        #genventilationSystemAndThermostat_preventive
        self.fields['genventilationSystemAndThermostat_preventive'].widget.attrs.update({'name':'genventilationSystemAndThermostat_preventive','class': 'form-control','id':'genventilationSystemAndThermostat_preventive','onchange':'Func_genventilationSystemAndThermostat_preventive()'})
        self.fields['genventilationSystemAndThermostatNoOkDetail_preventive'].widget.attrs.update({'name':'genventilationSystemAndThermostatNoOkDetail_preventive','class': 'form-control','id':'genventilationSystemAndThermostatNoOkDetail_preventive'})

        #gencleaningVentilationFilters_preventive
        self.fields['gencleaningVentilationFilters_preventive'].widget.attrs.update({'name':'gencleaningVentilationFilters_preventive','class': 'form-control','id':'gencleaningVentilationFilters_preventive','onchange':'Func_gencleaningVentilationFilters_preventive()'})
        self.fields['gencleaningVentilationFiltersNoOkDetail_preventive'].widget.attrs.update({'name':'gencleaningVentilationFiltersNoOkDetail_preventive','class': 'form-control','id':'gencleaningVentilationFiltersNoOkDetail_preventive'})

        #genfreeOfCorrosion_preventive
        self.fields['genfreeOfCorrosion_preventive'].widget.attrs.update({'name':'genfreeOfCorrosion_preventive','class': 'form-control','id':'genfreeOfCorrosion_preventive','onchange':'Func_genfreeOfCorrosion_preventive()'})
        self.fields['genfreeOfCorrosionNoOkDetail_preventive'].widget.attrs.update({'name':'genfreeOfCorrosionNoOkDetail_preventive','class': 'form-control','id':'genfreeOfCorrosionNoOkDetail_preventive'})

        #genelementCleaning_preventive
        self.fields['genelementCleaning_preventive'].widget.attrs.update({'name':'genelementCleaning_preventive','class': 'form-control','id':'genelementCleaning_preventive','onchange':'Func_genelementCleaning_preventive()'})
        self.fields['genelementCleaningNoOkDetail_preventive'].widget.attrs.update({'name':'genelementCleaningNoOkDetail_preventive','class': 'form-control','id':'genelementCleaningNoOkDetail_preventive'})

        #genupdatedSignalList_preventive
        self.fields['genupdatedSignalList_preventive'].widget.attrs.update({'name':'genupdatedSignalList_preventive','class': 'form-control','id':'genupdatedSignalList_preventive','onchange':'Func_genupdatedSignalList_preventive()'})
        self.fields['genupdatedSignalListNoOkDetail_preventive'].widget.attrs.update({'name':'genupdatedSignalListNoOkDetail_preventive','class': 'form-control','id':'genupdatedSignalListNoOkDetail_preventive'})
        
        #SAI
        self.fields['saistatusOfConnectorsAndLEDs_preventive'].widget.attrs.update({'name':'saistatusOfConnectorsAndLEDs_preventive','class': 'form-control','id':'saistatusOfConnectorsAndLEDs_preventive','onchange':'Func_saistatusOfConnectorsAndLEDs_preventive()'})
        self.fields['saistatusOfConnectorsAndLEDsNoOkDetail_preventive'].widget.attrs.update({'name':'saistatusOfConnectorsAndLEDsNoOkDetail_preventive','class': 'form-control','id':'saistatusOfConnectorsAndLEDsNoOkDetail_preventive'})

        #saiinputVoltageMeasurement_preventive
        self.fields['saiinputVoltageMeasurement_preventive'].widget.attrs.update({'class': 'form-control'})
        
        #saioutputVoltageToConsumption_preventive
        self.fields['saioutputVoltageToConsumption_preventive'].widget.attrs.update({'class': 'form-control'})

        #saibatteryStatus_preventive
        self.fields['saibatteryStatus_preventive'].widget.attrs.update({'name':'saibatteryStatus_preventive','class': 'form-control','id':'saibatteryStatus_preventive','onchange':'Func_saibatteryStatus_preventive()'})
        self.fields['saibatteryStatusNoOkDetail_preventive'].widget.attrs.update({'name':'saibatteryStatusNoOkDetail_preventive','class': 'form-control','id':'saibatteryStatusNoOkDetail_preventive'})

        #saicleaning_preventive
        self.fields['saicleaning_preventive'].widget.attrs.update({'name':'saicleaning_preventive','class': 'form-control','id':'saicleaning_preventive','onchange':'Func_saicleaning_preventive()'})
        self.fields['saicleaningNoOkDetail_preventive'].widget.attrs.update({'name':'saicleaningNoOkDetail_preventive','class': 'form-control','id':'saicleaningNoOkDetail_preventive'})

        #/Preventive Questions

        #VARIOUS2
        self.fields['status_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['endDatetime_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['totalEstimatedTime_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['revisionPorcentage_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_preventive'].widget.attrs.update({'class': 'form-control'})



class UpdatePreventiveForm(forms.ModelForm):
    class Meta:
        model = Preventive
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(UpdatePreventiveForm, self).__init__(*args, **kwargs)
        #VARIOUS1
        #self.fields['code_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['startDatetime_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['station_preventive'].widget.attrs.update({'class': 'form-control'})
        
        #Preventive Questions
        #AUTOMATAS
        self.fields['autVisualInspectionOfAlarmLedStatus_preventive'].widget.attrs.update({'class': 'form-control','id':'autVisualInspectionOfAlarmLedStatus_preventive'})
        self.fields['autLithiumBatteryStatus_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['autHardwareDiagnosis_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['autDIandAIinCCStatus_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['autcheckRxTxOnCommunicationCards_preventive'].widget.attrs.update({'class': 'form-control'})
        #GENERAL
        self.fields['genventilationSystemAndThermostat_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['gencleaningVentilationFilters_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['genfreeOfCorrosion_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['genelementCleaning_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['genupdatedSignalList_preventive'].widget.attrs.update({'class': 'form-control'})
        #SAI
        self.fields['saistatusOfConnectorsAndLEDs_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['saiinputVoltageMeasurement_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['saioutputVoltageToConsumption_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['saibatteryStatus_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['saicleaning_preventive'].widget.attrs.update({'class': 'form-control'})
        #/Preventive Questions

        #VARIOUS2
        self.fields['status_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['endDatetime_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['revisionPorcentage_preventive'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_preventive'].widget.attrs.update({'class': 'form-control'})
        
