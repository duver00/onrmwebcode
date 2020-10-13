from django.shortcuts import render
from datetime import datetime
from noticias.models import Post
# Create your views here.

# Create your views h


def home(request):
    now = Post.objects.all().last()
    noticias = Post.objects.all()
    return render(request, "onrm/home.html", {"now": now, "titulo": noticias})






