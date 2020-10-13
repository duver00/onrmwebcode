"""registro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from registro import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('legilacion/minera', views.lminera, name='lminera'),
    path('legislacion/petrolera', views.lpetrolera, name='lpetrolera'),
    path('legislacion/otras', views.lotras, name='lotras'),
    path('derechos/mineros',views.dminerales, name='dmineros'),
    path('derechos/hidrocarburos',views.dhidrocarburos, name='dpetroleo'),
    path('solicitudes/reonocimiento',views.sreconocimiento, name='reconocimiento'),
    path('solicitudes/concesion',views.scminera, name='concesiones')
]
