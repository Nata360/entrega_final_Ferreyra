from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView

app_name = 'usuario'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='usuario/logout.html'), name='logout'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('perfil/info_perfil/<int:usuario_id>', views.info_perfil, name='info_perfil'),
    path('perfil/info_perfil_autor/<int:usuario_id>', views.info_perfil_autor, name='info_perfil_autor'),
    path('perfil/editar', views.editar_perfil, name='editar_perfil'),
    path('perfil/editar/password', views.ModificarPass.as_view(), name='modificar_pass')
    
    
]
