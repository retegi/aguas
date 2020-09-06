from django import forms
from .models import Station

class AddStationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddStationForm, self).__init__(*args, **kwargs)
        self.fields['code_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['name_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['latitude_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitude_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['origin_watertank'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['area_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['communication_technology_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['communication_windows_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['comunication_point'].widget.attrs.update({'class': 'form-control'})
        self.fields['status_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['simulator3D_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['image_station'].widget.attrs.update({'class': 'form-control'})


        


