from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .form import FormularioMensajeria
from .models import *


@login_required
def enviar_mensaje(request, destinatario_id, mensaje_id=None):
    destinatario = User.objects.get(id=destinatario_id)
    # mensaje_original = None
    
    # if mensaje_id:
        # mensaje_original = get_object_or_404(Mensajeria, id=mensaje_id)
    
    if request.method == 'POST':
        formulario = FormularioMensajeria(request.POST)
        if formulario.is_valid():
            mensaje = formulario.save(commit=False)
            mensaje.remitente = request.user
            mensaje.destinatario = destinatario
            
            # if mensaje_original:
            #     mensaje.mensaje_original = mensaje_original
            #     mensaje.destinatario = mensaje_original.destinatario
               
            mensaje.save()
            return redirect('mensajeria:bandeja_de_entrada')
    else:
        formulario = FormularioMensajeria()
        
    return render(request, 'mensajeria/enviar_mensaje.html', {'formulario':formulario, 'destinatario':destinatario}) #'mensaje_original':mensaje_original})

@login_required
def responder_mensaje(request,mensaje_id):
    mensaje_original = get_object_or_404(Mensajeria, id=mensaje_id)
    
    if request.method == 'POST':
        formulario = FormularioMensajeria(request.POST)
        if formulario.is_valid():
            mensaje = formulario.save(commit=False)
            mensaje.remitente = request.user
            mensaje.destinatario = mensaje_original.remitente
            mensaje.mensaje_original = mensaje_original
            mensaje.save()
            return redirect('mensajeria:bandeja_de_entrada')
    else:
        formulario = FormularioMensajeria()
    destinatario_id = mensaje_original.remitente.id
    return render(request, 'mensajeria/responder_mensaje.html', {'formulario':formulario, 'mensaje_original': mensaje_original,'destinatario_id': destinatario_id} )
    
    
def inbox(request):
    user = request.user
    mensajes_recibidos = Mensajeria.objects.filter(destinatario=user).order_by('-fecha_envio')
    return render(request, 'mensajeria/bandeja_de_entrada.html', {'mensajes_recibidos': mensajes_recibidos} )
