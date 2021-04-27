from django.contrib import admin
from .models import Imagenes

# Register your models here.

class ImagenesAdmin(admin.ModelAdmin):
    list_display = ("nombre", "imagen")

admin.site.register (Imagenes, ImagenesAdmin)