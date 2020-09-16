from django.shortcuts import render
from django.utils import timezone
from .models import Consumable
from .models import ImageConsumable
from .models import TypeConsumable
from .models import TypeModelConsumable
from .models import StatusConsumable
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .forms import AddConsumableForm
from .forms import UpdateConsumableForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse

class ConsumableListView(LoginRequiredMixin,ListView):
    model = Consumable
    template_name = 'consumable/list_consumable.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(parent_device_consumable__installation_device__station_installation__name_station__icontains = name)|Q(serial_num_consumable__icontains = name)|Q(type_model_consumable__brand_typeConsumable__icontains = name)|Q(type_model_consumable__model_typeConsumable__icontains = name)|Q(status_consumable__name__icontains = name)|Q(type_model_consumable__type_consumable_typeConsumable__name__icontains = name))
        else:
            object_list = self.model.objects.all()
        return object_list
    login_url = reverse_lazy('users_app:user-login')


class ConsumableListByStationView(LoginRequiredMixin,ListView):
    template_name = 'consumable/list_consumable.html'
    def get_queryset(self):
        identifier = self.kwargs['pk']
        object_list = Consumable.objects.filter(parent_device_consumable__installation_device__station_installation__id = identifier)
        return object_list
    login_url = reverse_lazy('users_app:user-login')

class ConsumableListByInstallationView(LoginRequiredMixin,ListView):
    template_name = 'consumable/list_consumable.html'
    def get_queryset(self):
        identifier = self.kwargs['pk']
        object_list = Consumable.objects.filter(parent_device_consumable__installation_device__id = identifier)
        return object_list
    login_url = reverse_lazy('users_app:user-login')

class ConsumableListByDeviceView(LoginRequiredMixin,ListView):
    template_name = 'consumable/list_consumable.html'
    def get_queryset(self):
        identifier = self.kwargs['pk']
        object_list = Consumable.objects.filter(parent_device_consumable__id = identifier)
        return object_list
    login_url = reverse_lazy('users_app:user-login')


class ConsumableAddView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'consumable.add_consumable'
    template_name = 'consumable/add_consumable.html'
    model = Consumable
    form_class = AddConsumableForm
    success_url = '/consumable/'
    login_url = reverse_lazy('users_app:user-login')

class ConsumableUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'consumable.update_consumable'
    template_name = "consumable/update_consumable.html"
    model = Consumable
    form_class = UpdateConsumableForm
    success_url = '/consumable/'
    login_url = reverse_lazy('users_app:user-login')

class ConsumableDetailView(LoginRequiredMixin,DetailView):
    model = Consumable
    template_name = "consumable/detail_consumable.html"
    login_url = reverse_lazy('users_app:user-login')

class ConsumableDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'consumable.delete_consumable'
    model = Consumable
    template_name = "consumable/delete_consumable.html"
    success_url = '/consumable/'
    login_url = reverse_lazy('users_app:user-login')

