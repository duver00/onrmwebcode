from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, ListView
from noticias import models
from  django.http import HttpResponse
# Create your views here.


class PostList(ListView):
    template_name = 'noticias/noticias.html'
    context_object_name = 'list_news'
    paginate_by = 3

    def get_queryset(self):
        return Post.objects.all().order_by('-created')


class PostDetail(DetailView):
    model = Post
    template_name = 'noticias/opennoticias.html'
    context_object_name = 'noticia'


def Scanbutton(request):

        if request.GET.get('scan'):

            titulo = request.GET.get("scan")
            noticias = models.Post.objects.all().filter(titulo__icontains=titulo)
            return render(request, "noticias/lista_busqueda.html", {"noticias": noticias, "query": titulo})

        else:

            return render(request,"noticias/no_busqueda.html")




