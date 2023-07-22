from django.contrib import admin
from inicio.models import *
# Register your models here.

class AlbunDeImagenes(admin.TabularInline):
    model = Imagen

class AlbunAdmin(admin.ModelAdmin):
    inlines = [AlbunDeImagenes]

class BlogAdmin(admin.ModelAdmin):
    list_display = ('nombre_blog', 'nombre_autor', 'apellido_autor', 'categoria', 'descripcion')
    search_fields = ('nombre_blog', 'nombre_autor', 'apellido_autor', 'categoria')

class ImagenAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'blog', 'albun', 'fecha_publicacion')
    list_filter = ('blog', 'albun')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Albun, AlbunAdmin)
admin.site.register(Imagen, ImagenAdmin)

