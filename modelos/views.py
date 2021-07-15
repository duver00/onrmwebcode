from django.shortcuts import render
from django.views.generic.edit import FormView, View
from .forms import SolicitudP, MovimientoAFT
# Create your views here.


class SolicitudpFormView(FormView):
    template_name = 'Pago/formulariop.html'
    form_class = SolicitudP



def solicitud_pago(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SolicitudP(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            departamento = form.cleaned_data['departamento']
            fechaemision = form.cleaned_data['fechaemision']
            concepto = form.cleaned_data['concepto']
            paguese = form.cleaned_data['paguese']
            importe = form.cleaned_data['importe']
            solicita =  form.cleaned_data['solicita']
            # redirect to a new URL:
            return render(request, 'Pago/moldelop2.htm', {'departamento':departamento, 'fechaemision':fechaemision,
                                                             'concepto':concepto,'paguese':paguese,'importe':importe,
                                                             'solicita':solicita})
            # if a GET (or any other method) we'll create a blank form
    else:
        form = SolicitudpFormView()
    return render(request, 'Pago/formulariop.html', {'form': form})

class MovimientoFormView(FormView):
    template_name = "AFT/formulariom.html"
    form_class = MovimientoAFT


def modelo_aft(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MovimientoAFT(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            inventario = form.cleaned_data['inventario']
            fecha = form.cleaned_data['fecha']
            area_equipo = form.cleaned_data['area_equipo']
            descripcion = form.cleaned_data['descripcion']
            direccion_receptor = form.cleaned_data['direccion_receptor']
            area_receptor = form.cleaned_data['area_receptor']
            nombre_tecnico = form.cleaned_data['nombre_tecnico']
            cargo_tecnico = form.cleaned_data['cargo_tecnico']
            autorizado_cargo = form.cleaned_data['autorizado_cargo']
            # redirect to a new URL:
            return render(request, 'AFT/modelom.htm', {'inventario':inventario, 'fecha':fecha,
                                                             'area_equipo': area_equipo,'descripcion': descripcion,'direccion_receptor': direccion_receptor,
                                                             'area_receptor': area_receptor, 'nombre_tecnico': nombre_tecnico, 'cargo_tecnico': cargo_tecnico,
                                                          'autorizado_cargo': autorizado_cargo})
    else:
        form = SolicitudpFormView()
    return render(request, 'AFT/formulariom.html', {'form': form})

# Creating our view, it is a class based view
