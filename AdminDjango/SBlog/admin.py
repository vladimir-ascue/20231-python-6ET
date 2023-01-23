from django.contrib import admin
from SBlog.models import *

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'estado')
    search_fields = ('nombre',)

class PublicacionesAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','publicado','actualizado', 'estado')
    readonly_fields = ('meGusta', 'noMeGusta')
    search_fields = ('autor','titulo')
    list_filter = ('categoria',)


class ComentariosAdmin(admin.ModelAdmin):
    list_display = ('comentario', 'autor', 'estado')
    search_fields = ('autor',)

# Register your models here.
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Publicacion, PublicacionesAdmin)
admin.site.register(Comentario, ComentariosAdmin)
