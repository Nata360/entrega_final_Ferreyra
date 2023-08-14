from django.urls import path
from .import views

app_name = 'mensajeria'

urlpatterns = [
    path('enviar_mensaje/<int:destinatario_id>/', views.enviar_mensaje, name='enviar_mensaje'),
    path('responder_mensaje/<int:mensaje_id>/', views.responder_mensaje, name='responder_mensaje'),
    path('bandeja_de_entrada/', views.inbox, name='bandeja_de_entrada' )
    
]
