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
        self.fields['origin_watertank'].label = "Depósito de agua de origen (en su caso)"
        self.fields['observations_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['area_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['area_station'].label = "Area de la estación"
        self.fields['type_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_station'].label = "Tipo de estación"
        self.fields['communication_technology_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['communication_technology_station'].label = "Tecnología de comunicación"
        self.fields['communication_windows_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['comunication_point'].widget.attrs.update({'class': 'form-control'})
        self.fields['comunication_point'].label = "Punto de comunicación"
        self.fields['status_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['status_station'].label = "Estado de la estación"
        self.fields['simulator3D_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['simulator3D_station'].label = "Animación 3D"
        self.fields['image_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['image_station'].label = "Imágenes de la estación"
        self.fields['video_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['video_station'].label = "Videos de la estación"
        self.fields['doc_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['doc_station'].label = "Documentos/Planos"



class UpdateStationForm(forms.ModelForm):
    class Meta:
        model = Station
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(UpdateStationForm, self).__init__(*args, **kwargs)
        self.fields['communication_technology_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['communication_technology_station'].label = "Tecnología de comunicación"
        self.fields['code_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['name_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['latitude_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['longitude_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['communication_windows_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['communication_technology_station'].label = "Tecnología de comunicación"
        self.fields['area_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['area_station'].label = "Area de la estación"
        self.fields['origin_watertank'].widget.attrs.update({'class': 'form-control'})
        self.fields['origin_watertank'].label = "Depósito de agua de origen (en su caso)"
        self.fields['type_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_station'].label = "Tipo de estación"
        self.fields['comunication_point'].widget.attrs.update({'class': 'form-control'})
        self.fields['comunication_point'].label = "Punto de comunicación"
        self.fields['image_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['image_station'].label = "Imágenes de la estación"
        self.fields['status_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['status_station'].label = "Estado de la estación"
        self.fields['simulator3D_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['simulator3D_station'].label = "Animación 3D"
        self.fields['video_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['video_station'].label = "Video de estación"
        self.fields['doc_station'].widget.attrs.update({'class': 'form-control'})
        self.fields['doc_station'].label = "Documentos/Planos"

