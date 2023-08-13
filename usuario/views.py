from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from usuario.form import MiFormularioDeCreacionDeUsuarios, MiFormularioDeEdicionDeDatosDeUsuario, FormularioCambioPass
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from usuario.models import InfoExtra
from .models import User

# Create your views here.

def login(request):
    if request.method == 'POST':
        
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            
            usuario = formulario.cleaned_data['username']
            contrasenia = formulario.cleaned_data['password']
            
            
            user = authenticate(username=usuario, password=contrasenia)
            
            django_login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
    
            
            return redirect('inicio:inicio')
    
        else:
            return render(request, 'usuario/login.html', {'formulario': formulario})
    
    formulario = AuthenticationForm()
    return render(request, 'usuario/login.html', {'formulario': formulario})

def registrarse(request):
    if request.method == 'POST':
        formulario = MiFormularioDeCreacionDeUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio:inicio')
        else: 
            return render(request, 'usuario/registro.html', {'formulario': formulario})
    formulario = MiFormularioDeCreacionDeUsuarios
    return render(request, 'usuario/registro.html', {'formulario': formulario})


@login_required
def editar_perfil(request):
    info_extra_user = request.user.infoextra
    if request.method == 'POST':
        formulario = MiFormularioDeEdicionDeDatosDeUsuario(request.POST, request.FILES, instance= request.user)
        if formulario.is_valid():
            
            avatar = formulario.cleaned_data.get('avatar')
            biografia = formulario.cleaned_data.get('biografia')
            if avatar:
                
                info_extra_user.avatar = avatar
                info_extra_user.save()
            if biografia:
                info_extra_user.biografia = biografia
                info_extra_user.save()
            formulario.save()
            return redirect('usuario:info_perfil')
    else:   
        formulario = MiFormularioDeEdicionDeDatosDeUsuario(initial={'avatar': info_extra_user.avatar, 'biografia': info_extra_user.biografia}, instance=request.user)
        
    return render(request, 'usuario/editar_perfil.html', {'formulario': formulario})

class ModificarPass(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuario/modificar_pass.html'
    success_url = reverse_lazy('inicio:inicio')
    form_class = FormularioCambioPass
    
def info_perfil(request, usuario_id):
    perfil_usuario = get_object_or_404(User, id=usuario_id)
    return render(request, 'usuario/info_perfil.html', {'perfil_usuario':perfil_usuario})

def info_perfil_autor(request, usuario_id):
    perfil_usuario = get_object_or_404(User, id=usuario_id)
    return render(request, 'usuario/info_perfil_autor.html', {'perfil_usuario':perfil_usuario})

