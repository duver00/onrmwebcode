from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Post(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    resumen = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200,unique=True)
    contenido = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='noticias')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['created']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('detalles', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.titulo)
        return super().save(*args, **kwargs)