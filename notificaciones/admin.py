from django.contrib import admin
from .models import Aviso

# Register your models here.


class AvisosAdmin(admin.ModelAdmin):
    list_display = ("titulo", "created")


admin.site.register(Aviso, AvisosAdmin)