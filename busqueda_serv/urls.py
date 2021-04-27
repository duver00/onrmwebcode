from django.urls import path
from busqueda_serv import views

urlpatterns = [
    path('directorio/', views.directorio_tel, name='telefonico'),
]