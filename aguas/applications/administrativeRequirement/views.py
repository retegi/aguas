from django.shortcuts import render
from django.utils import timezone
from .models import AdministrativeRequirement

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
)
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse

class AdministrativeRequirementListView(LoginRequiredMixin,ListView):
    model = AdministrativeRequirement
    template_name = 'administrativeRequirement/list_administrativeRequirement.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(number_AR__icontains = name)|Q(status_AR__icontains = name))
        else:
            object_list = self.model.objects.all()
        return object_list
    login_url = reverse_lazy('users_app:user-login')