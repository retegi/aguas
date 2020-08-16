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

class InstalacionList(ListView):
    model = Installation
    template_name = 'installation/list_installation.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(station_installation__name_station__icontains = name)
        else:
            object_list = self.model.objects.all()
        return object_list

class InstalacionAdd(CreateView):
    template_name = 'installation/add_installation.html'
    model = Installation
    form_class = AddInstallationForm
    success_url = '/installation/'

class InstalacionUpdateView(UpdateView):
    template_name = "installation/update_installation.html"
    model = Installation
    fields = [
            'type_installation',
            'station_installation',
            'observations_installation',
            ]
    success_url = '/installation/'

class InstalacionDetailView(DetailView):
    model = Installation
    template_name = "installation/detail_installation.html"

class InstalacionDeleteView(DeleteView):
    model = Installation
    template_name = "installation/delete_installation.html"
    success_url = '/installation/'
