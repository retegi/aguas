from django.shortcuts import render
from django.utils import timezone
from .models import Device, ImageDevice
from .models import TypeDevice
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .forms import AddDeviceForm
from django.db.models import Q

"""def dispositivo_list(request):
    dispositivos = Dispositivo.objects.filter().order_by('marca')
    images = ImagenDispositivo.objects.all()
    historicos = Dispositivo.history.all()
    return render(request, 'dispositivo/dispositivo_list.html', {'dispositivos': dispositivos, 'images':images, 'historicos':historicos})"""

class DeviceListView(ListView):
    model = Device
    template_name = 'device/list_device.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(installation_device__station__name__icontains = name) | Q(serial_device__icontains = name))
        else:
            object_list = self.model.objects.all()
        return object_list

class DeviceAddView(CreateView):
    template_name = 'device/add_device.html'
    model = Device
    form_class = AddDeviceForm
    success_url = '/'

class DeviceUpdateView(UpdateView):
    template_name = "device/update_device.html"
    model = Device
    fields = [
            'type_device',
            'communication_device',
            'brand_device',
            'model_device',
            'serial_device',
            'ip_device',
            'pin_device',
            'puk_device',
            'slave_num_device',
            'tel_long_device',
            'tel_short_device',
            'parent_device',
            'installation_device',
            #'estacion',
            'image_device',
            'observations_device',
            ]
    success_url = '/device/'

class DeviceDetailView(DetailView):
    model = Device
    template_name = "device/detail_device.html"

class DeviceDeleteView(DeleteView):
    model = Device
    template_name = "device/delete_device.html"
    success_url = '/device/'