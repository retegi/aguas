from django import forms
from .models import Station

class CrearEstacionForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(CrearEstacionForm, self).__init__(*args, **kwargs)
        self.fields['code_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['name_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['latitude_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitude_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['origin_watertank'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['area_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['comunication_point'].widget.attrs.update({'class': 'form-control'})

        


