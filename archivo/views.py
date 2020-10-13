from django.shortcuts import render

# Create your views here.


def archivo(request):
    return render(request,"archivo.html")


def cpresencial(request):
    return render(request,"ConsultaP/consultap.html")


def entregap(request):
    return render(request,"EntregaP/epresencial.html")

def epersonalizada(request):
    return render(request,"EntregaPersonalizada/epersonalizada.html")