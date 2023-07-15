from django.urls import path
from inicio import views

app_name = 'inicio'

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista_blogs/sin_datos', views.sin_datos, name='sin_datos'),
    path('crear_blog/', views.CrearBlog.as_view(), name='crear_blog'),
    path('lista_blogs/', views.ListaDeBlogs.as_view(), name='lista_blogs'),
]
