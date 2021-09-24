from django.contrib import admin
from .models import ControlInterno, LinksExternos, DocumentosRectores

# Register your models here.


class LinksExternosAdmin(admin.ModelAdmin):
    list_display = ('titulo','url')


class ControlInternoAdmin(admin.ModelAdmin):
    list_display = ('titulo','documento')


class DocumentosRectoresAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'documento')


admin.site.register(LinksExternos, LinksExternosAdmin)
admin.site.register(ControlInterno, ControlInternoAdmin)
admin.site.register(DocumentosRectores, DocumentosRectoresAdmin)