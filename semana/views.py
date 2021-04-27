from django.shortcuts import render
from .models import Actividad
from django.views.generic import ListView


#  code here

class ActividadesList(ListView):
    template_name = 'Linea.html'
    context_object_name = 'list_actividades'


    def get_queryset(self):
        return Actividad.objects.all().order_by('date_day')


