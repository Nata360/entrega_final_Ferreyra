from django.urls import path
from galeria import views

app_name = 'galeria'

urlpatterns = [
    path('subir_imagen/', views.subir_imagen, name='subir_imagen'),
    path('galeria/imagenes', views.imagen_galeria, name='imagen_galeria'),

]
