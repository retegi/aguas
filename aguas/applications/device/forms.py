from django import forms
from .models import Device

class AddDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddDeviceForm, self).__init__(*args, **kwargs)
        self.fields['product_model_device'].widget.attrs.update({'class': 'form-control','id':'type_device'})
        self.fields['product_model_device'].label= "Tipo de ptroducto y modelo del dispositivo"
        self.fields['serial_device'].widget.attrs.update({'class': 'form-control','id':'serial_device'})
        self.fields['serial_device'].label= "Número de serie del dispositivo"
        self.fields['ip_device'].widget.attrs.update({'class': 'form-control','id':'ip_device'})
        self.fields['ip_device'].label= "IP del dispositivo"
        self.fields['pin_device'].widget.attrs.update({'class': 'form-control','id':'marca','id':'pin_device'})
        self.fields['pin_device'].label="PIN del dispositivo"
        self.fields['puk_device'].widget.attrs.update({'class': 'form-control','id':'marca','id':'puk_device'})
        self.fields['puk_device'].label="PUK del dispositivo"
        self.fields['slave_num_device'].widget.attrs.update({'class': 'form-control','id':'slave_num_device'})
        self.fields['slave_num_device'].label="Número de esclavo del dispositivo (Si lo tiene)"
        self.fields['tel_long_device'].widget.attrs.update({'class': 'form-control','id':'tel_long_device'})
        self.fields['tel_long_device'].label="Teléfono LARGO del dispositivo"
        self.fields['tel_short_device'].widget.attrs.update({'class': 'form-control','id':'tel_short_device'})
        self.fields['tel_short_device'].label="Teléfono CORTO del dispositivo"
        self.fields['parent_device'].widget.attrs.update({'class': 'form-control','id':'parent_device'})
        self.fields['parent_device'].label="Dispositivo PADRE"
        self.fields['installation_device'].widget.attrs.update({'class': 'form-control','id':'installation_device'})
        self.fields['installation_device'].label="Instalación en la cual está situado"
        self.fields['observations_device'].widget.attrs.update({'class': 'form-control','id':'observations_device'})
        self.fields['observations_device'].label="Observaciones"


class UpdateDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(UpdateDeviceForm, self).__init__(*args, **kwargs)
        self.fields['product_model_device'].widget.attrs.update({'class': 'form-control','id':'type_device'})
        self.fields['product_model_device'].label= "Tipo de ptroducto y modelo del dispositivo"
        self.fields['serial_device'].widget.attrs.update({'class': 'form-control','id':'serial_device'})
        self.fields['serial_device'].label= "Número de serie del dispositivo"
        self.fields['ip_device'].widget.attrs.update({'class': 'form-control','id':'ip_device'})
        self.fields['ip_device'].label="IP de dispositivo"
        self.fields['pin_device'].widget.attrs.update({'class': 'form-control','id':'marca','id':'pin_device'})
        self.fields['pin_device'].label="PIN del dispositivo"
        self.fields['puk_device'].widget.attrs.update({'class': 'form-control','id':'marca','id':'puk_device'})
        self.fields['puk_device'].label="PUK del dispositivo"
        self.fields['slave_num_device'].widget.attrs.update({'class': 'form-control','id':'slave_num_device'})
        self.fields['slave_num_device'].label="Número ESCLAVO del dispositivo"
        self.fields['tel_long_device'].widget.attrs.update({'class': 'form-control','id':'tel_long_device'})
        self.fields['tel_long_device'].label="Teléfono LARGO del dispositivo"
        self.fields['tel_short_device'].widget.attrs.update({'class': 'form-control','id':'tel_short_device'})
        self.fields['tel_short_device'].label="Teléfono CORTO del dispositivo"
        self.fields['parent_device'].widget.attrs.update({'class': 'form-control','id':'parent_device'})
        self.fields['parent_device'].label="Dispositivo PADRE"
        self.fields['installation_device'].widget.attrs.update({'class': 'form-control','id':'installation_device'})
        self.fields['installation_device'].label="Instalación en el cual está colocado el dispositivo"
        self.fields['observations_device'].widget.attrs.update({'class': 'form-control','id':'observations_device'})
        self.fields['observations_device'].label="Observaciones"



 
     