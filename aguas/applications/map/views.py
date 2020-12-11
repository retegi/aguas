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

        if Map.objects.all():
            context['map'] = Map.objects.all()
        context['map'] = Map.objects.all()
        '''else:
            localidad = Map(name_location='Zarautz',longitude_conf_map='43.28419696697072',latitude_conf_map='-2.165541196252545',zoom_conf_map='13.5')
            localidad.save()
            context['map'] = localidad'''
        context['station'] = Station.objects.all()
        return context

