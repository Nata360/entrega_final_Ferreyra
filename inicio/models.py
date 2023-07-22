from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Blog(models.Model):
    nombre_blog = models.CharField(max_length=20)
    nombre_autor = models.CharField(max_length=20)
    apellido_autor = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, max_length=100)
    
    def __str__(self):
        return f'Blog: {self.nombre_blog} por {self.nombre_autor}'

class Albun(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Albun: {self.titulo} por {self.autor} - Fecha de creación {self.fecha_creacion}'
    
class Imagen(models.Model):
    albun = models.ForeignKey(Albun, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='galeria/imagenes')
    titulo = models.CharField(max_length=50)
    descripcion = RichTextField(null=True, max_length=800)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Imagen: {self.titulo}'

