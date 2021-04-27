from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class Directorio(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    contenido = RichTextUploadingField()

    class Meta:
        verbose_name = 'Directorio'
        verbose_name_plural = 'Directorios'

    def __str__(self):
        return self.nombre