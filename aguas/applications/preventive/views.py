from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from .models import Preventive
from .models import ContractPreventive
from .models import ContractedCompanyPreventive
from .models import Station
from applications.map.models import Map
from applications.preventive.models import Preventive
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    View
)
from .forms import AddPreventiveForm
from .forms import UpdatePreventiveForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse

class PreventiveList(LoginRequiredMixin,ListView):
    model = Preventive
    template_name = 'preventive/list_preventive.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(id_preventive__icontains = name)|Q(code_preventive__icontains = name))
        else:
            object_list = self.model.objects.all()
        return object_list

class PreventiveDetailView(LoginRequiredMixin,DetailView):
    model = Preventive
    template_name = "preventive/detail_preventive.html"
    login_url = reverse_lazy('users_app:user-login')

class PreventiveAddView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'preventive.add_preventive'
    template_name = 'preventive/add_preventive.html'
    model = Preventive
    form_class = AddPreventiveForm
    success_url = '/preventive/'
    login_url = reverse_lazy('users_app:user-login')

class PreventiveUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'preventive.update_preventive'
    template_name = "preventive/update_preventive.html"
    model = Preventive
    form_class = UpdatePreventiveForm
    success_url = '/preventive/'
    login_url = reverse_lazy('users_app:user-login')

class PreventiveDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'preventive.delete_preventive'
    model = Preventive
    template_name = "preventive/delete_preventive.html"
    success_url = '/preventive/'
    login_url = reverse_lazy('users_app:user-login')

class PreventiveDetailedStatisticsListView(LoginRequiredMixin,ListView):
    model = Preventive
    template_name = "preventive/statistics_preventive_detailed.html"
    login_url = reverse_lazy('users_app:user-login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.model.objects.all():
            context['preventives'] = self.model.objects.all()
            context['totalCalc'] = int(self.model.objects.all().count())
            context['total'] = str(self.model.objects.all().count())
            context['january'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='1').count())
            context['february'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='2').count())
            context['march'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='3').count())
            context['april'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='4').count())
            context['may'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='5').count())
            context['june'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='6').count())
            context['july'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='7').count())
            context['august'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='8').count())
            context['september'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='9').count())
            context['october'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='10').count())
            context['november'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='11').count())
            context['december'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='12').count())
            
        if str(ContractPreventive.objects.first()):
            context['contractNumPreventives'] = str(ContractPreventive.objects.first())

        if ContractedCompanyPreventive.objects.first():
            context['name_contractedCompanyPrevent'] = ContractedCompanyPreventive.objects.first().name_contractedCompanyPrevent
        
        if ContractPreventive.objects.first():
            context['contractNumPreventivesCalc'] = ContractPreventive.objects.first().annualPreventiveContract_ContractPreventive
        
        if ContractPreventive.objects.first():
            context['differenceUntilComplete'] = context['contractNumPreventivesCalc']-context['totalCalc']

        reviewedStationsIds = self.model.objects.all().values_list('station_preventive',flat=True).distinct()
        context['reviewedStationsIds'] = self.model.objects.all().values_list('station_preventive',flat=True).distinct()

        reviewedStationsIds = self.model.objects.all().distinct().values_list('station_preventive',flat=True)
        context['notReviewedStations'] = Station.objects.exclude(id__in=reviewedStationsIds)

        return context

class PreventiveSimplifiedStatisticsListView(LoginRequiredMixin,ListView):
    model = Preventive
    template_name = "preventive/statistics_preventive_simplified.html"
    login_url = reverse_lazy('users_app:user-login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['preventives'] = self.model.objects.all()
        context['totalCalc'] = int(self.model.objects.all().count())
        context['total'] = str(self.model.objects.all().count())
        context['january'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='1').count())
        context['february'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='2').count())
        context['march'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='3').count())
        context['april'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='4').count())
        context['may'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='5').count())
        context['june'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='6').count())
        context['july'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='7').count())
        context['august'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='8').count())
        context['september'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='9').count())
        context['october'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='10').count())
        context['november'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='11').count())
        context['december'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='12').count())

        if str(ContractPreventive.objects.first()):
            context['contractNumPreventives'] = str(ContractPreventive.objects.first())
        else:
            context['contractNumPreventives'] = "Not defined"
            
        if ContractedCompanyPreventive.objects.first():
            context['name_contractedCompanyPrevent'] = ContractedCompanyPreventive.objects.first().name_contractedCompanyPrevent
        else:
            context['name_contractedCompanyPrevent'] = "Not defined"

        if ContractPreventive.objects.first():
            context['contractNumPreventivesCalc'] = ContractPreventive.objects.first().annualPreventiveContract_ContractPreventive
        else:
            context['contractNumPreventivesCalc'] = 0

        if ContractPreventive.objects.first():    
            context['differenceUntilComplete'] = context['contractNumPreventivesCalc']-context['totalCalc']
        else:
            context['differenceUntilComplete'] = 0

        reviewedStationsIds = self.model.objects.all().values_list('station_preventive',flat=True).distinct()
        context['reviewedStationsIds'] = self.model.objects.all().values_list('station_preventive',flat=True).distinct()
        reviewedStationsIds = self.model.objects.all().distinct().values_list('station_preventive',flat=True)
        context['notReviewedStations'] = Station.objects.exclude(id__in=reviewedStationsIds)
        return context        


class PreventiveMapListView(LoginRequiredMixin,ListView):
    permission_required = 'preventive.list_preventive'
    model = Preventive
    template_name = "preventive/map_preventive.html"
    login_url = reverse_lazy('users_app:user-login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.model.objects.all():
            context['preventives'] = self.model.objects.all()
            context['totalCalc'] = int(self.model.objects.all().count())
            context['total'] = str(self.model.objects.all().count())
            context['january'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='1').count())
            context['february'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='2').count())
            context['march'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='3').count())
            context['april'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='4').count())
            context['may'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='5').count())
            context['june'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='6').count())
            context['july'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='7').count())
            context['august'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='8').count())
            context['september'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='9').count())
            context['october'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='10').count())
            context['november'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='11').count())
            context['december'] = str(self.model.objects.filter(startDatetime_preventive__year='2020', startDatetime_preventive__month='12').count())
            
        if ContractPreventive.objects.first():
            context['contractNumPreventives'] = str(ContractPreventive.objects.first())
        else:
            context['contractNumPreventives'] = "Not defined"
        
        if ContractedCompanyPreventive.objects.first():
            context['name_contractedCompanyPrevent'] = ContractedCompanyPreventive.objects.first().name_contractedCompanyPrevent
        else:
            context['name_contractedCompanyPrevent'] = "Not defined"

        if ContractPreventive.objects.first():
            context['contractNumPreventivesCalc'] = ContractPreventive.objects.first().annualPreventiveContract_ContractPreventive
        else:
            context['contractNumPreventivesCalc'] = 0

        if ContractPreventive.objects.first():
            context['differenceUntilComplete'] = context['contractNumPreventivesCalc']-context['totalCalc']
        else:
            context['differenceUntilComplete'] = 0

        reviewedStationsIds = self.model.objects.all().values_list('station_preventive',flat=True).distinct()
        context['reviewedStationsIds'] = self.model.objects.all().values_list('station_preventive',flat=True).distinct()


        reviewedStationsIds = self.model.objects.all().distinct().values_list('station_preventive',flat=True)
        context['notReviewedStations'] = Station.objects.exclude(id__in=reviewedStationsIds)

        if Map.objects.all():
            context['map'] = Map.objects.all()

        return context







