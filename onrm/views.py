from django.shortcuts import render
from noticias.models import Post
from galeria.models import Imagenes
from eventos.models import EventosModel
from footer.models import LinksExternos, ControlInterno, DocumentosRectores


# Create your views h

def home(request):
    slidesnews1 = Post.objects.all().order_by('-created')[2:3]
    slidesnews0 = Post.objects.all().order_by('-created')[3:4]
    slidesnews2 = Post.objects.all().order_by('-created')[4:5]
    slidesnews3 = Post.objects.all().order_by('-created')[5:6]
    imagenes = Imagenes.objects.all().order_by('-created')
    todos = Post.objects.all()
    eventos = EventosModel.objects.all().order_by('fecha_evento')
    return render(request, 'onrm2/index.html', {'titulo0': slidesnews0, 'titulo1': slidesnews1, 'titulo2': slidesnews2,
                                                'titulo3': slidesnews3,'todos': todos,'imagenes': imagenes,
                                                'eventos': eventos})

