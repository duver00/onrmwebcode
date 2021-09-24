from django.db import models

# Create your models here.


class LinksExternos(models.Model):
    titulo = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.titulo


class DocumentosRectores(models.Model):
    titulo = models.CharField(max_length=50)
    documento = models.FileField(upload_to='rectores')

    def __str__(self):
        return self.titulo


class ControlInterno(models.Model):
    titulo = models.CharField(max_length=50)
    documento = models.FileField(upload_to='control')

    class Meta:
        verbose_name = 'Control Interno'

    def __str__(self):
        return self.titulo