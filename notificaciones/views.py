from django.shortcuts import render
from .models import Aviso
from django.views.generic import ListView

# Create your views here.


class NotificarList(ListView):
    template_name = 'notificaciones.html'
    context_object_name = 'list_aviso'
    paginate_by = 3


    def get_queryset(self):
        return Aviso.objects.all().order_by('-created')
