from django.shortcuts import render
from datetime import datetime
from noticias.models import Post
from galeria.models import Imagenes


# Create your views here.

# Create your views h

def home(request):
    slidesnews1 = Post.objects.all().order_by('-created')[2:3]
    slidesnews0 = Post.objects.all().order_by('-created')[3:4]
    slidesnews2 = Post.objects.all().order_by('-created')[4:5]
    slidesnews3 = Post.objects.all().order_by('-created')[5:6]
    imagenes = Imagenes.objects.all().order_by('-created')
    now = Post.objects.all().last()
    todos = Post.objects.all()
    return render(request, 'onrm2/index.html', {'titulo0': slidesnews0, 'titulo1': slidesnews1, 'titulo2': slidesnews2,
                                                'titulo3':slidesnews3,'now': now,'todos':todos,'imagenes':imagenes})


def base(request):
    actual = Post.objects.all().last()
    return render(request, 'onrm2/base2.html', {'actual': actual})
