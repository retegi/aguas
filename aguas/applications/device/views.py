from django.shortcuts import render
from django.utils import timezone
from applications.station.models import Station
from .models import Device
from .models import ImageDevice
from .models import TypeDevice
from .models import DocDevice
from .models import CommunicationDevice
from .models import ProductModelDevice
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)

from .forms import AddDeviceForm
from .forms import UpdateDeviceForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse



class DeviceListView(LoginRequiredMixin,ListView):
    model = Device
    template_name = 'device/list_device.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(installation_device__station_installation__name_station__icontains = name) | Q(serial_device__icontains = name) | Q(product_model_device__brand_device__name__icontains = name) | Q(product_model_device__model_device__icontains = name) | Q(product_model_device__type_device__name__icontains = name))
        else:
            object_list = self.model.objects.all()
        return object_list
    login_url = reverse_lazy('users_app:user-login')


class DeviceListByStationView(LoginRequiredMixin,ListView):
    template_name = 'device/list_device.html'

    def get_queryset(self):
        identifier = self.kwargs['pk']
        object_list = Device.objects.filter(installation_device__station_installation__id = identifier)
        return object_list
    login_url = reverse_lazy('users_app:user-login')

class DeviceListByInstallationView(LoginRequiredMixin,ListView):
    template_name = 'device/list_device.html'

    def get_queryset(self):
        identifier = self.kwargs['pk']
        object_list = Device.objects.filter(installation_device__id = identifier)
        return object_list
    login_url = reverse_lazy('users_app:user-login')


class DeviceAddView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'device.add_device'
    template_name = 'device/add_device.html'
    model = Device
    form_class = AddDeviceForm
    success_url = '/device/'
    login_url = reverse_lazy('users_app:user-login')

class DeviceUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'device.update_device'
    template_name = "device/update_device.html"
    model = Device
    form_class = UpdateDeviceForm
    success_url = '/device/'
    login_url = reverse_lazy('users_app:user-login')

class DeviceDetailView(LoginRequiredMixin,DetailView):
    model = Device
    template_name = "device/detail_device.html"
    login_url = reverse_lazy('users_app:user-login')

class DeviceDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'device.delete_device'
    model = Device
    template_name = "device/delete_device.html"
    success_url = '/device/'
    login_url = reverse_lazy('users_app:user-login')

class DeviceDocDetailView(LoginRequiredMixin,DetailView):
    model = Device
    template_name = "device/doc_device.html"
    login_url = reverse_lazy('users_app:user-login')