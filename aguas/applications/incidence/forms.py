from django import forms
from .models import Incidence


class AddIncidenceForm(forms.ModelForm):
    class Meta:
        model = Incidence
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddIncidenceForm, self).__init__(*args, **kwargs)
        self.fields['station_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['datetime_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['typeIncidence_incidence'].widget.attrs.update({'class': 'form-control'})
        self.fields['statusIncidence_incidence'].widget.attrs.update({'class': 'form-control'})
        