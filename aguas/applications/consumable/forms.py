from django import forms
from .models import Consumable
from .models import TypeConsumable
from .models import ImageConsumable
from .models import StatusConsumable

class AddConsumableForm(forms.ModelForm):
    class Meta:
        model = Consumable
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddConsumableForm, self).__init__(*args, **kwargs)
        self.fields['datetime_placemente_consumable'].widget.attrs.update({'class': 'form-control'})
        self.fields['type_model_consumable'].widget.attrs.update({'class': 'form-control'})
        self.fields['serial_num_consumable'].widget.attrs.update({'class': 'form-control'})
        self.fields['parent_device_consumable'].widget.attrs.update({'class': 'form-control'})
        self.fields['status_consumable'].widget.attrs.update({'class': 'form-control'})
        self.fields['observations_consumable'].widget.attrs.update({'class': 'form-control'})
        
     