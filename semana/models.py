from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Actividad(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    resumen = RichTextUploadingField()
    date_day = models.DateField(null=False, blank=False)

    class Meta:
        verbose_name = 'Actividad del Mes'
        verbose_name_plural = 'Actividades'
        ordering = ['date_day']

    def __str__(self):
        return self.titulo
