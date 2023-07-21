from django.contrib import admin
from inicio.models import *
# Register your models here.

admin.site.register(Blog)
admin.site.register(Imagen)
class AlbunDeImagenes(admin.TabularInline):
    model = Imagen

class AlbunAdmin(admin.ModelAdmin):
    inlines = [AlbunDeImagenes]