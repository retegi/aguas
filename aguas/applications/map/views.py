from django.shortcuts import render
from django.utils import timezone
from .models import Map
from applications.station.models import Station
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    TemplateView,
)

from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
        

class HomeMapView(ListView):
    model = Map
    template_name = "map/index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map'] = Map.objects.all()
        context['station'] = Station.objects.all()

        """context['ebap'] = Station.objects.filter(type_station = 1)
        context['rdap'] = Station.objects.filter(type_station = 2)
        context['ESAP'] = Station.objects.filter(type_station = 3)
        context['DRAP'] = Station.objects.filter(type_station = 4)
        context['DRAR'] = Station.objects.filter(type_station = 5)
        context['ECS'] = Station.objects.filter(type_station = 6)
        context['EDAR'] = Station.objects.filter(type_station = 7)
        context['DDAP'] = Station.objects.filter(type_station = 8)
        context['PLVM'] = Station.objects.filter(type_station = 9)
        context['CC'] = Station.objects.filter(type_station = 10)
        context['REP'] = Station.objects.filter(type_station = 11)"""
        return context






