from django.shortcuts import render
from django.utils import timezone
from .models import Repair
from .models import Incidence
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from .forms import AddRepairForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse

class RepairListView(ListView):
    model = Repair
    template_name = 'repair/list_repair.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(id__icontains = name))
        else:
            object_list = self.model.objects.all()
        return object_list

"""class RepairListByIncidenceView(LoginRequiredMixin,ListView):
    template_name = 'repair/list_repair.html'
    def get_queryset(self):
        identifier = self.kwargs['pk']
        object_list = Repair.objects.filter(id = identifier)
        return object_list
    login_url = reverse_lazy('users_app:user-login')"""

class RepairListByIncidenceView(LoginRequiredMixin,ListView):
    template_name = 'repair/list_repair.html'
    def get_queryset(self):
        identifier = self.kwargs['pk']
        object_list = Repair.objects.filter(incidence_repair_id = identifier)
        ordering = ['datetime_repair']
        return object_list
    login_url = reverse_lazy('users_app:user-login')

class RepairAddView(CreateView):
    template_name = 'repair/add_repair.html'
    model = Repair
    form_class = AddRepairForm
    success_url = '/repair/'

class RepairDetailView(DetailView):
    model = Repair
    template_name = "repair/detail_repair.html"

class RepairUpdateView(UpdateView):
    model = Repair
    fields = [
            'incidence_repair',
            'affectedDevice_repair',
            'datetime_repair',
            'statusAfterRepair_repair',
            'summary_repair',
            'detail_repair',
            ]
    success_url = '/repair/'
    template_name = "repair/update_repair.html"

class RepairDeleteView(DeleteView):
    model = Repair
    template_name = "repair/delete_repair.html"
    success_url = '/repair/'

