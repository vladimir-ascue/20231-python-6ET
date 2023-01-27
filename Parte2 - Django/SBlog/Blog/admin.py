from django.contrib import admin
from Blog.models import Categoria, Publicacion, Comentario
from django import forms

# class CategoriaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'nombre', 'creado', 'modificado','estado')
#     search_fields = ('nombre','estado')
#     list_filter = ('estado',)

class CategoriaAdminForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {'estado':forms.Select(choices=model.ESTADOS)}

class CategoriaAdmin(admin.ModelAdmin):
    form = CategoriaAdminForm

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