from django import forms
from .models import Incidence

class AddIncidenceForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddIncidenceForm, self).__init__(*args, **kwargs)
        self.fields['station_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['datetime_incidence'].widget.attrs.update({'class':'form-control','value':'2020-00-00 09:00:00'})    
        self.fields['typeIncidence_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['repairForecast_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['companyRepair_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['statusIncidence_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['urgencyLevel_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['billing_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_incidence'].widget.attrs.update({'class': 'form-control'})

class UpdateIncidenceForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(UpdateIncidenceForm, self).__init__(*args, **kwargs)
        self.fields['station_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['datetime_incidence'].widget.attrs.update({'class': 'form-control'})    
        self.fields['typeIncidence_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['repairForecast_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['companyRepair_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['statusIncidence_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['urgencyLevel_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['billing_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_incidence'].widget.attrs.update({'class': 'form-control'})      
