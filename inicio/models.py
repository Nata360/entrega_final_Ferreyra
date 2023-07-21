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
    
class Imagen(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='galeria/imagenes')
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True, max_length=500)
    
    def __str__(self):
        return f'Imagen: {self.titulo}'

