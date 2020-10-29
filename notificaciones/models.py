from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Aviso(models.Model):
    titulo = models.CharField(max_length=255)
    contenido = RichTextUploadingField()
    created = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Aviso'
        verbose_name_plural = 'Avisos'
        ordering = ['created']

    def __str__(self):
        return self.titulo