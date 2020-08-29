from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
from .models import Incidence
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DetailView,
    DeleteView,
    View
)
from .forms import AddIncidenceForm

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
    model = Incidence
    fields = [
            'typeIncidence_incidence',
            'station_incidence',
            'datetime_incidence',
            'observations_incidence',
            'statusIncidence_incidence',
            ]
    success_url = '/incidence/'
    template_name = "incidence/update_incidence.html"

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


"""class ListaIncidenciasListView(ListView):
    model = Incidencia
    template_name = "incidencia/pdf_incidencia_list.html"
    context_object_name = 'incidencias'

class ListIncidenciasPdf(View):
    def get(self, request, *args, **kwargs):
        incidencias = Incidencia.objects.filter(Q(solucionado='0') | Q(solucionado='2') | Q(solucionado='3'))
        data = {
            'incidencias': incidencias
        }
        pdf = render_to_pdf('incidencia/pdf_incidencia_list.html', data)
        return HttpResponse(pdf, content_type='application/pdf')"""


