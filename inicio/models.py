from django.db import models

# Create your models here.
class Blog(models.Model):
    nombre_blog = models.CharField(max_length=20)
    nombre_autor = models.CharField(max_length=20)
    apellido_autor = models.CharField(max_length=20)
    categoria = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, max_length=100)
    
    def __str__(self):
        return f'Blog: {self.nombre_blog} por {self.nombre_autor}'