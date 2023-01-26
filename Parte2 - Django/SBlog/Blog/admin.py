from django.contrib import admin
from Blog.models import Categoria, Publicacion, Comentario

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'creado', 'modificado','estado')
    search_fields = ('nombre',)
    list_filter = ('estado',)

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'autor', 'publicado', 'estado')
    readonly_fields = ('id', 'meGusta', 'noMeGusta', 'autor') # Para que los campos sean de solo lectura
    search_fields = ('estado',) # Para el cuadro de busqueda
    list_filter = ('categoria','autor','estado') # Para mostrar el panel de filtro de la derecha

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'comentario','publicacion', 'actualizado', 'autor', 'estado',)
    search_fields = ('publicacion', 'actualizado', 'autor', 'estado',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Publicacion, PublicacionAdmin)
admin.site.register(Comentario, ComentarioAdmin)