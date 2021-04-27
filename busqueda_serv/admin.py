from django.contrib import admin
from .models import Directorio


# Register your models here.

class DirectorioAdmin(admin.ModelAdmin):
    list_display = ("nombre",)


admin.site.register(Directorio, DirectorioAdmin)
