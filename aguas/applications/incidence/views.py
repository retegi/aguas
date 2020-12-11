from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from .models import Incidence
from applications.station.models import Station
from applications.map.models import Map
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    View
)
from .forms import AddIncidenceForm
from .forms import UpdateIncidenceForm

from django.urls import reverse_lazy, reverse

#PARA IMPRIMIR EN PDF:
from django.conf import settings
from reportlab.lib.pagesizes import letter
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
#FIN PARA PDF


#PARA IMPRMIR PDF con XHTMLTOPDF
from django.http import HttpResponse
from .utils import render_to_pdf
#FIN

class IncidenceList(LoginRequiredMixin,ListView):
    model = Incidence
    template_name = 'incidence/list_incidence.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(station_incidence__name_station__icontains = name) | Q(id__icontains = name))
        else:
            object_list = self.model.objects.all()
        return object_list

#Filtra incidencias por facturados
class InvoicedIncidenceList(LoginRequiredMixin,ListView):
    model = Incidence
    template_name = 'incidence/list_incidence.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(station_incidence__name_station__icontains = name) | Q(id__icontains = name))
        else:
            object_list = self.model.objects.filter(billing_incidence__billing_conf='Envoiced')
        return object_list

#Filtra incidencias por facturados
class NotInvoicedIncidenceList(LoginRequiredMixin,ListView):
    model = Incidence
    template_name = 'incidence/list_incidence.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(station_incidence__name_station__icontains = name) | Q(id__icontains = name))
        else:
            object_list = self.model.objects.filter(billing_incidence__billing_conf='Not envoiced')
        return object_list

#Filtra incidencias por facturados
class DoNotInvoiceIncidenceList(LoginRequiredMixin,ListView):
    model = Incidence
    template_name = 'incidence/list_incidence.html'
    def get_queryset(self):
        name = self.request.GET.get('kword', '')
        if name:
            object_list = self.model.objects.filter(Q(station_incidence__name_station__icontains = name) | Q(id__icontains = name))
        else:
            object_list = self.model.objects.filter(billing_incidence__billing_conf='Not to envoice')
        return object_list


def incidence_list(ListView):
    incidences = Incidence.objects.filter(Q(solucionado='0') | Q(solucionado='2') | Q(solucionado='3'))
    return render(ListView,'incidences/list_incidence.html',{'incidences': incidences})

def incidence_list_all(request):
    incidences = Incidence.objects.filter()
    return render(request,'incidencia/incidencia_list.html',{'incidences': incidences})

class IncidenceDetailView(LoginRequiredMixin,DetailView):
    model = Incidence
    template_name = "incidence/detail_incidence.html"

class IncidenceUpdateView(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    permission_required = 'incidence.update_incidence'
    template_name = "incidence/update_incidence.html"
    model = Incidence
    form_class = UpdateIncidenceForm
    success_url = '/incidence/'
    login_url = reverse_lazy('users_app:user-login')

class IncidenceDeleteView(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = 'incidence.delete_incidence'
    model = Incidence
    template_name = "incidence/delete_incidence.html"
    success_url = '/incidence/'

class IncidenceAdd(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = 'incidence.add_incidence'
    template_name = 'incidence/add_incidence.html'
    model = Incidence
    form_class = AddIncidenceForm
    success_url = '/incidence/'


#GENERAR PDF
def some_view(pdf):    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setPageSize(('595', '842'))
    p.hAlign = 'CENTER'
    p.setLineWidth(.3)
    #Cabecera
    p.setFont('Helvetica', 22)
    p.drawString(30,730,'Título')
    p.setFont('Helvetica-Bold', 12)
    p.drawString(30,706,'Subtítulo')
    p.line(30,723,560,723)
    archivo_imagen = settings.BASE_DIR+'/blog/static/img/logo-django.png'
    p.drawImage(archivo_imagen, 30, 750, 120, 90,preserveAspectRatio=True)

    #Tabla
    p.setFont('Helvetica', 12)
    p.drawString(30,650,'Tabla:')
    #Aquí se debe mostrar la tabla

    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='incidencias.pdf')

class IncidenceMapListView(LoginRequiredMixin,ListView):
    permission_required = 'preventive.list_preventive'
    model = Incidence
    template_name = "incidence/map_incidence.html"
    login_url = reverse_lazy('users_app:user-login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['incidences'] = self.model.objects.exclude(statusIncidence_incidence__name='Reparado')
        context['totalCalc'] = int(self.model.objects.all().count())
        context['total'] = str(self.model.objects.all().count())
        context['january'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='1').count())
        context['february'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='2').count())
        context['march'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='3').count())
        context['april'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='4').count())
        context['may'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='5').count())
        context['june'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='6').count())
        context['july'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='7').count())
        context['august'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='8').count())
        context['september'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='9').count())
        context['october'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='10').count())
        context['november'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='11').count())
        context['december'] = str(self.model.objects.filter(datetime_incidence__year='2020', datetime_incidence__month='12').count())
        context['map'] = Map.objects.all()
        return context


