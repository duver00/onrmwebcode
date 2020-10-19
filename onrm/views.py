from django.shortcuts import render
from datetime import datetime
from noticias.models import Post
# Create your views here.

# Create your views h


def home(request):
    now = Post.objects.all().last()
    slidenews = Post.objects.all().order_by('-created')[2:4]
    slidenews2 = Post.objects.all().order_by('-created')[4:8]
    return render(request, 'onrm/home.html',{'now':now, 'titulo':slidenews, 'titulo2':slidenews2})


def probando(request):
    now = Post.objects.all().last()
    slidenews = Post.objects.all().order_by('-created')[2:4]
    slidenews2 = Post.objects.all().order_by('-created')[4:8]
    return render(request, "prueba/slides.html",{'now':now, 'titulo':slidenews, 'titulo2':slidenews2})






