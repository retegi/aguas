from django import forms
from .models import Repair
from .models import Employee


class AddRepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(AddRepairForm, self).__init__(*args, **kwargs)
        self.fields['startDatetime_repair'].widget.attrs.update({'class': 'form-control', 'type':'date','value':'2020-00-00 09:00:00'})
        self.fields['startDatetime_repair'].label="Fecha y hora de comienzo reparación"

        self.fields['endDatetime_repair'].widget.attrs.update({'class': 'form-control', 'type':'date','value':'2020-00-00 09:00:00'})
        self.fields['endDatetime_repair'].label="Fecha y hora de finalización de reparación"

        self.fields['incidence_repair'].widget.attrs.update({'class': 'form-control', 'type':'date'})
        self.fields['incidence_repair'].label="Incidencia a reparar"

        self.fields['affectedDevice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['affectedDevice_repair'].label="Dispositivo afectado"

        self.fields['typeFailure_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['typeFailure_repair'].label="Tipo de fallo"

        self.fields['typeRepair_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['typeRepair_repair'].label="Tipo de reparación"

        self.fields['removedDevice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['removedDevice_repair'].label="Deispositivo retirado"

        self.fields['placedDevice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['placedDevice_repair'].label="Dispositivo colocado"

        self.fields['removedConsumable_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['removedConsumable_repair'].label="Consumible retirado"

        self.fields['placedConsumable_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['placedConsumable_repair'].label="Consumible colocado"

        self.fields['statusAfterRepair_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['statusAfterRepair_repair'].label="Estado de la incidencia tras reparación"

        self.fields['company_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['company_repair'].label="Compañía reparadora"

        self.fields['summary_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary_repair'].label="Resumen de la reparación"

        self.fields['detail_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['detail_repair'].label="Detalles de la reparación"

        self.fields['productsToInvoice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['productsToInvoice_repair'].label="Productos y servicios a facturar"

        self.fields['employee_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['employee_repair'].label="Operarios"

class UpdateRepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ('__all__')
    def __init__(self, *args, **kwargs):
        super(UpdateRepairForm, self).__init__(*args, **kwargs)
        self.fields['startDatetime_repair'].widget.attrs.update({'class': 'form-control', 'type':'date'})
        self.fields['startDatetime_repair'].label="Fecha y hora de comienzo reparación"

        self.fields['endDatetime_repair'].widget.attrs.update({'class': 'form-control', 'type':'date'})
        self.fields['endDatetime_repair'].label="Fecha y hora de finalización de reparación"

        self.fields['incidence_repair'].widget.attrs.update({'class': 'form-control', 'type':'date'})
        self.fields['incidence_repair'].label="Incidencia a reparar"

        self.fields['affectedDevice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['affectedDevice_repair'].label="Dispositivo afectado"

        self.fields['typeFailure_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['typeFailure_repair'].label="Tipo de fallo"

        self.fields['typeRepair_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['typeRepair_repair'].label="Tipo de reparación"

        self.fields['removedDevice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['removedDevice_repair'].label="Deispositivo retirado"

        self.fields['placedDevice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['placedDevice_repair'].label="Dispositivo colocado"

        self.fields['removedConsumable_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['removedConsumable_repair'].label="Consumible retirado"

        self.fields['placedConsumable_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['placedConsumable_repair'].label="Consumible colocado"

        self.fields['statusAfterRepair_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['statusAfterRepair_repair'].label="Estado de la incidencia tras reparación"

        self.fields['company_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['company_repair'].label="Compañía reparadora"

        self.fields['summary_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['summary_repair'].label="Resumen de la reparación"

        self.fields['detail_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['detail_repair'].label="Detalles de la reparación"

        self.fields['productsToInvoice_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['productsToInvoice_repair'].label="Productos y servicios a facturar"

        self.fields['employee_repair'].widget.attrs.update({'class': 'form-control'})
        self.fields['employee_repair'].label="Operarios"

        