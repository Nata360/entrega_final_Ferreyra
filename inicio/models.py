from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    nombre_blog = models.CharField(max_length=20)
    nombre_autor = models.CharField(max_length=20)
    apellido_autor = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, max_length=100)
    
    def __str__(self):
        return f'Blog: {self.nombre_blog} por {self.nombre_autor}'
    
class Albun(models.Model):
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __unicode__(self,):
        return self.titulo

class AlbunImagen(models.Model):
    albun = models.ForeignKey(Albun, related_name='imagenes', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='albun/imagenes')
    def __unicode__(self,):
        return str(self.imagen)