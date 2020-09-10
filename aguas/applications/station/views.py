from django.shortcuts import render
from django.utils import timezone
from .models import Station
from .models import ImageStation
from .models import AreaStation
#from .models import TypeStation
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .forms import AddStationForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse



class StationListView(LoginRequiredMixin,ListView):
    model = Station
    template_name = 'station/list_station.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(name_station__icontains = name)|Q(type_station__acronym__icontains = name))
        else:
            object_list = self.model.objects.all()
        return object_list
    login_url = reverse_lazy('users_app:user-login')


class StationGalleryDetailView(LoginRequiredMixin,DetailView):
    model = Station
    template_name = "station/gallery_station.html"
    login_url = reverse_lazy('users_app:user-login')

class StationDocDetailView(LoginRequiredMixin,DetailView):
    model = Station
    template_name = "station/doc_station.html"
    login_url = reverse_lazy('users_app:user-login')
    

class StationAddView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'station.add_station'
    template_name = 'station/add_station.html'
    model = Station
    form_class = AddStationForm
    success_url = '/station/'
    login_url = reverse_lazy('users_app:user-login')


class StationUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'station.update_station'
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
            'type_station',
            'status_station'
            ]
    success_url = '/station/'
    login_url = reverse_lazy('users_app:user-login')

class StationDetailView(LoginRequiredMixin,DetailView):
    model = Station
    template_name = "station/detail_station.html"
    login_url = reverse_lazy('users_app:user-login')

        

class StationDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'station.delete_station'
    model = Station
    template_name = "station/delete_station.html"
    success_url = '/station/'
    login_url = reverse_lazy('users_app:user-login')







