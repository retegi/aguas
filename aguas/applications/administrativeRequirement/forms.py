from django import forms
from .models import AdministrativeRequirement

class AddAdministrativeRequirementForm(forms.ModelForm):
    class Meta:
        model = AdministrativeRequirement
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddAdministrativeRequirementForm, self).__init__(*args, **kwargs)
        self.fields['number_AR'].widget.attrs.update({'class': 'form-control'})
        self.fields['datetime_AR'].widget.attrs.update({'class': 'form-control'})    
        self.fields['file_AR'].widget.attrs.update({'class': 'form-control'})
        self.fields['address_AR'].widget.attrs.update({'class': 'form-control'})
        self.fields['anomaly_AR'].widget.attrs.update({'class': 'form-control'})
        self.fields['status_AR'].widget.attrs.update({'class': 'form-control'})
        self.fields['reasonRequirement_AR'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_AR'].widget.attrs.update({'class': 'form-control'})

