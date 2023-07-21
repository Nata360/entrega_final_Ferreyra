from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('blog/crear_blog/', views.CrearBlog.as_view(), name='crear_blog'),
    path('lista_blogs/', views.ListaDeBlogs.as_view(), name='lista_blogs'),
    path('blog/eliminar_blog/<int:pk>', views.EliminarBlog.as_view(), name='eliminar_blog'),
    path('blog/editar_blog/<int:pk>', views.EditarBlog.as_view(), name='editar_blog'),
    path('blog/ver_blog/<int:pk>', views.VerBlog.as_view(), name='ver_blog'),
    path('blog/ver_blog/subir_imagen/', views.subir_imagen, name='subir_imagen'),
    path('blog/ver_blog/galeria_imagenes/', views.imagen_galeria, name='imagen_galeria'),
    
    
]
