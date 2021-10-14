from django.contrib import admin
from .models import EventosModel


# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_evento','created')


admin.site.register(EventosModel, EventosAdmin)
