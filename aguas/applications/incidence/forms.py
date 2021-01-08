from django import forms
from .models import Incidence

class AddIncidenceForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddIncidenceForm, self).__init__(*args, **kwargs)
        self.fields['station_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['station_incidence'].label="ESTACIÓN con incidencia"

        self.fields['datetime_incidence'].widget.attrs.update({'class':'form-control','value':'2020-00-00 09:00:00','id':'datepicker'})
        self.fields['datetime_incidence'].label="FECHA Y HORA de la incidencia (Año-mes-día hora-minutos-segundos)"  

        self.fields['typeIncidence_incidence'].widget.attrs.update({'class': 'form-control','id':'typeIncidence_incidence','onchange':'Func_viewanotherTypeIncidence_incidence()'})
        self.fields['typeIncidence_incidence'].label="Tipo de incidencia"

        self.fields['anotherTypeIncidence_incidence'].widget.attrs.update({'name':'anotherTypeIncidence_incidence','class': 'form-control','id':'anotherTypeIncidence_incidence','onchange':'Func_viewanotherTypeIncidence_incidence()'})
        self.fields['anotherTypeIncidence_incidence'].label="Otro tipo de incidencia"

        self.fields['repairForecast_incidence'].widget.attrs.update({'class': 'form-control','value':'2020-00-00 09:00:00','id':'datepicker2'})
        self.fields['repairForecast_incidence'].label="Previsión de reparación"

        self.fields['statusIncidence_incidence'].widget.attrs.update({'class': 'form-control','value':'5'})
        self.fields['statusIncidence_incidence'].label="Estado actual de la incidencia"

        self.fields['companyRepair_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['companyRepair_incidence'].label="Compañía reparadora"

        self.fields['urgencyLevel_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['urgencyLevel_incidence'].label="Nivel de URGENCIA (0 baja y 10 crítica)"

        self.fields['billing_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['billing_incidence'].label="Estado de facturación"

        self.fields['observations_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_incidence'].label="Observaciones"

class UpdateIncidenceForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(UpdateIncidenceForm, self).__init__(*args, **kwargs)
        self.fields['station_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['station_incidence'].label="ESTACIÓN con incidencia"

        self.fields['datetime_incidence'].widget.attrs.update({'class': 'form-control','id':'datepicker'})
        self.fields['datetime_incidence'].label="FECHA Y HORA de la ncidencia (Año-mes-día hora-minutos-segundos)"  
   
        self.fields['typeIncidence_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['typeIncidence_incidence'].label="Tipo de incidencia"

        self.fields['repairForecast_incidence'].widget.attrs.update({'class': 'form-control','id':'datepicker2'})
        self.fields['repairForecast_incidence'].label="Previsión de reparación"

        self.fields['statusIncidence_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['statusIncidence_incidence'].label="Estado actual de la incidencia"

        self.fields['companyRepair_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['companyRepair_incidence'].label="Compañía reparadora"

        self.fields['urgencyLevel_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['urgencyLevel_incidence'].label="Nivel de URGENCIA (0 baja y 10 crítica)"

        self.fields['billing_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['billing_incidence'].label="Estado de facturación"

        self.fields['observations_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_incidence'].label="Observaciones"
    
