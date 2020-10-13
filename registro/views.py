from django.shortcuts import render

# Create your views here.


def registro(request):
    return render(request, "registro.html")


def lminera(request):
    return render(request, "legislacion/Legislacion Minera.html")


def lpetrolera(request):
    return render(request, "legislacion/legislacion_petro.html")


def lotras(request):
    return render(request, "legislacion/legislacion_otras.html")


def dminerales(request):
    return render(request, "derechos/dminerales.html")


def dhidrocarburos(request):
    return render(request,"derechos/dhidrocarburos.html")


def sreconocimiento(request):
    return  render(request,"solicitudes/preconocimiento.html")

def scminera(request):
    return render(request, "solicitudes/cminera.html")