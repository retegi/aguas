from django.shortcuts import render
from django.utils import timezone
from .models import Installation
from .models import Station
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .forms import AddInstallationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse

class InstallationListView(LoginRequiredMixin,ListView):
    model = Installation
    template_name = 'installation/list_installation.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(station_installation__name_station__icontains = name)
        else:
            object_list = self.model.objects.all()
        return object_list
    login_url = reverse_lazy('users_app:user-login')

class InstallationListByStationView(LoginRequiredMixin,ListView):
    template_name = 'installation/list_installation.html'
    def get_queryset(self):
        identifier = self.kwargs['pk']
        object_list = Installation.objects.filter(station_installation__id = identifier)
        return object_list
    login_url = reverse_lazy('users_app:user-login')

class InstallationAddView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'installation.add_installation'
    template_name = 'installation/add_installation.html'
    model = Installation
    form_class = AddInstallationForm
    success_url = '/installation/'
    login_url = reverse_lazy('users_app:user-login')

class InstallationUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'installation.update_installation'
    template_name = "installation/update_installation.html"
    model = Installation
    fields = [
            'type_installation',
            'station_installation',
            'image_installation',
            'observations_installation',
            ]
    success_url = '/installation/'
    login_url = reverse_lazy('users_app:user-login')

class InstallationDetailView(LoginRequiredMixin,DetailView):
    model = Installation
    template_name = "installation/detail_installation.html"
    login_url = reverse_lazy('users_app:user-login')

class InstallationDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'installation.delete_installation'
    model = Installation
    template_name = "installation/delete_installation.html"
    success_url = '/installation/'
    login_url = reverse_lazy('users_app:user-login')
