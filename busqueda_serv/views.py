from django.shortcuts import render
from .models import Directorio

# Create your views here.
def directorio_tel(request):
    directorios = Directorio.objects.all()
    return render(request,"busqueda_serv.html",{'diretorios':directorios})