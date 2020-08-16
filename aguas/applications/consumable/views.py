from django.shortcuts import render
from django.utils import timezone
from .models import Consumable
from .models import ImageConsumable
from .models import TypeConsumable
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .forms import AddConsumableForm
from django.db.models import Q

class ConsumableListView(ListView):
    model = Consumable
    template_name = 'consumable/list_consumable.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(parent_device_consumable__installation_device__station_installation__name_station__icontains = name) | Q(cons_numserie__icontains = name))
        else:
            object_list = self.model.objects.all()
        return object_list


class ConsumableAddView(CreateView):
    template_name = 'consumable/add_consumable.html'
    model = Consumable
    form_class = AddConsumableForm
    success_url = '/'

class ConsumableUpdateView(UpdateView):
    template_name = "consumable/update_consumable.html"
    model = Consumable
    fields = ['datetime_placemente_consumable',
            'type_consumable',
            'serial_num_consumable',
            'parent_device_consumable',
            'status_consumable',
            'observations_consumable',
            ]
    success_url = '/consumable/'

class ConsumableDetailView(DetailView):
    model = Consumable
    template_name = "consumable/detail_consumable.html"

class ConsumableDeleteView(DeleteView):
    model = Consumable
    template_name = "consumable/delete_consumable.html"
    success_url = '/consumable/'

