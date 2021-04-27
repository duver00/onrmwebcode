from django.contrib import admin
from .models import Actividad


# Register your models here.

class ActividadAdmin(admin.ModelAdmin):
    list_display = ("titulo", "date_day")


admin.site.register(Actividad, ActividadAdmin)
