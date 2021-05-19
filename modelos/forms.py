from django import forms

#Code below


class SolicitudP(forms.Form):
    departamento = forms.CharField(max_length=30, required=True, label= "Dirección")
    fechaemision = forms.DateField(required=True, label="Fecha de solicitud")
    concepto = forms.CharField(widget=forms.Textarea, required=True)
    paguese = forms.CharField(max_length=50, required=True, label="Páguese a")
    importe = forms.DecimalField(decimal_places=2,required=True, label="Importe total")
    solicita = forms.CharField(max_length=50,required=True, label="Solicita")


class MovimientoAFT(forms.Form):
    inventario = forms.IntegerField(max_value=5, label="Número de inventario", required=True)
    area_equipo = forms.CharField(max_length=50, label="Area del medio",required=True)
    descripcion = forms.CharField(label="Descripción del medio", required=True)
    direccion_receptor = forms.CharField(label="Dirección del receptor", required=True)
    area_receptor = forms.CharField(label="Area del receptor", required=True)
    fecha = forms.DateField(label="Fecha de movimiento", required=True)
    nombre_tecnico = forms.CharField(label="Nombre del técnico", required=False)
    cargo_tecnico = forms.CharField(label="Cargo del técnico", required=False)
    autorizado_cargo = forms.CharField(label="Autoriza")