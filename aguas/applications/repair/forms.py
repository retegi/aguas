from django import forms
from .models import Repair


class AddRepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddRepairForm, self).__init__(*args, **kwargs)
        self.fields['datetime_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['affectedDevice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['typeFailure_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['typeRepair_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['removedDevice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['placedDevice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['removedConsumable_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['placedConsumable_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['statusAfterRepair_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['detail_repair'].widget.attrs.update({'class': 'form-control'})

        