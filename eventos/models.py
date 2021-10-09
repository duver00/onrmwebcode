from django.db import models


# Create your models here.

class EventosModel(models.Model):
    titulo = models.CharField(max_length=50)
    fecha_evento = models.DateField()
    hora = models.TimeField(default='08:00')
    lugar_evento = models.CharField(max_length=20)
    resumen_evento = models.CharField(max_length=50)
    created = models.DateField(auto_now=True)

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"
        ordering = ['fecha_evento']

    def __str__(self):
        return self.titulo

