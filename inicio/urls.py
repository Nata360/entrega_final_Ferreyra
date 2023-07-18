from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista_blogs/sin_datos', views.sin_datos, name='sin_datos'),
    path('blog/crear_blog/', views.CrearBlog.as_view(), name='crear_blog'),
    path('lista_blogs/', views.ListaDeBlogs.as_view(), name='lista_blogs'),
    path('blog/eliminar_blog/<int:pk>', views.EliminarBlog.as_view(), name='eliminar_blog'),
    path('blog/editar_blog/<int:pk>', views.EditarBlog.as_view(), name='editar_blog'),
    path('blog/ver_blog/<int:pk>', views.VerBlog.as_view(), name='ver_blog'),
    # path('blog/home_view/', views.home_view, name='home_view'),
    # path('blog/crear_albun/', views.crear_albun, name= 'crear_albun'),
    # path('blog/subir_imagen', views.subir_imagen_view, name='subir_imagen_view')
    
]
