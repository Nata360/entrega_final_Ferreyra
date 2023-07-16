from django.contrib import admin
from .models import Albun, AlbunImagen
# Register your models here.

class AlbunImagenEnLinea(admin.TabularInline):
    model = AlbunImagen
    extra = 5
    
class AlbunAdmin(admin.ModelAdmin):
    inlines = [AlbunImagenEnLinea, ]