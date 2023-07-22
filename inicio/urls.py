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
    path('blog/lista_albunes/', views.ListaAlbun.as_view(), name='lista_albun'),
    path('blog/crear_albun/<int:pk>', views.CrearAlbun.as_view(), name='crear_albun'),
    path('blog/lista_albunes/ver_albun/<int:pk>', views.VerAlbun.as_view(), name='ver_albun'),
    path('blog/ver_blog/subir_imagen/', views.SubirImagen.as_view(), name='subir_imagen'),
    path('blog/ver_blog/galeria_imagenes/<int:pk>', views.imagen_galeria, name='imagen_galeria'),
    
]
