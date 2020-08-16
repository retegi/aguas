from django import forms
from .models import Device

class AddDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddDeviceForm, self).__init__(*args, **kwargs)
        self.fields['type_device'].widget.attrs.update({'class': 'form-control','id':'type_device'})
        self.fields['communication_device'].widget.attrs.update({'class': 'form-control','id':'communications_device'})
        self.fields['brand_device'].widget.attrs.update({'class': 'form-control','id':'brand_device'})
        self.fields['model_device'].widget.attrs.update({'class': 'form-control','id':'model_device'})
        self.fields['serial_device'].widget.attrs.update({'class': 'form-control','id':'serial_device'})
        self.fields['ip_device'].widget.attrs.update({'class': 'form-control','id':'ip_device'})
        self.fields['pin_device'].widget.attrs.update({'class': 'form-control','id':'marca','id':'pin_device'})
        self.fields['puk_device'].widget.attrs.update({'class': 'form-control','id':'marca','id':'puk_device'})
        self.fields['slave_num_device'].widget.attrs.update({'class': 'form-control','id':'slave_num_device'})
        self.fields['tel_long_device'].widget.attrs.update({'class': 'form-control','id':'tel_long_device'})
        self.fields['tel_short_device'].widget.attrs.update({'class': 'form-control','id':'tel_short_device'})
        self.fields['parent_device'].widget.attrs.update({'class': 'form-control','id':'parent_device'})
        self.fields['installation_device'].widget.attrs.update({'class': 'form-control','id':'installation_device'})
        #self.fields['estacion'].widget.attrs.update({'class': 'form-control','id':'estacion'})
        self.fields['observations_device'].widget.attrs.update({'class': 'form-control','id':'observations_device'})
     