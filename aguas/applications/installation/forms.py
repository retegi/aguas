from django import forms
from .models import Installation

class AddInstallationForm(forms.ModelForm):
    class Meta:
        model = Installation
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddInstallationForm, self).__init__(*args, **kwargs)
        self.fields['type_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['type_installation'].label = "Tipo de instalación"
        self.fields['station_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['station_installation'].label = "Estación en la cual se situa la instalación"
        self.fields['observations_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['observations_installation'].label = "Observaciones"
        self.fields['image_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['image_installation'].label = "Imagen instalación"
        self.fields['doc_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['doc_installation'].label = "Documentos de instalación"

class UpdateInstallationForm(forms.ModelForm):
    class Meta:
        model = Installation
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(UpdateInstallationForm, self).__init__(*args, **kwargs)
        self.fields['type_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['type_installation'].label = "Tipo de instalación"
        self.fields['station_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['station_installation'].label = "Estación en la cual se situa la instalación"
        self.fields['observations_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['observations_installation'].label = "Observaciones"
        self.fields['image_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['image_installation'].label = "Imagen instalación"
        self.fields['doc_installation'].widget.attrs.update({'class': 'form-control','id':'type_installation'})
        self.fields['doc_installation'].label = "Documentos de instalación"
