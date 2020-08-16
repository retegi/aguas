from django.shortcuts import render
from django.utils import timezone
#from dispositivo.models import Dispositivo
from .models import Station
#from incidencia.models import Incidencia
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .forms import CrearEstacionForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

class StationList(LoginRequiredMixin,ListView):
    model = Station
    template_name = 'station/list_station.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(name_station__icontains = name)
        else:
            object_list = self.model.objects.all()
        return object_list
    login_url = reverse_lazy('users_app:user-login')


class StationAdd(LoginRequiredMixin,CreateView):
    template_name = 'station/add_station.html'
    model = Station
    form_class = CrearEstacionForm
    success_url = '/station/'
    login_url = reverse_lazy('users_app:user-login')


class StationUpdateView(LoginRequiredMixin,UpdateView):
    template_name = "station/update_station.html"
    model = Station
    fields = [
            'code_station',
            'name_station',
            'area_station',
            'type_station',
            'latitude_station',
            'longitude_station',
            'origin_watertank',
            'comunication_point',
            'type_station'
            ]
    success_url = '/station/'
    login_url = reverse_lazy('users_app:user-login')

class StationDetailView(LoginRequiredMixin,DetailView):
    model = Station
    template_name = "station/detail_station.html"
    login_url = reverse_lazy('users_app:user-login')

        

class StationDeleteView(LoginRequiredMixin,DeleteView):
    model = Station
    template_name = "station/delete_station.html"
    success_url = '/station/'
    login_url = reverse_lazy('users_app:user-login')







