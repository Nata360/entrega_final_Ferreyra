from django.db import models

class Imagen(models.Model):
    imagen = models.ImageField(upload_to='galeria/imagenes')
    titulo = models.CharField(max_length=50)

    

    