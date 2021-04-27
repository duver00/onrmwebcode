from django.db import models


# Create your models here.
class Imagenes(models.Model):
    imagen = models.ImageField(upload_to='galeria')
    nombre = models.CharField(max_length=50, unique=True)
    created = models.DateField(null=False, blank=False)

    class Meta:
        verbose_name = "Galeria"
        verbose_name_plural = "Imagenes"
        ordering = ['-created']

    def __str__(self):
        return self.nombre

