from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100,null=False,unique=True)
    descripcion = models.CharField(max_length=500, null=True)
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True, max_length=25)
    estado = models.CharField(max_length=25, default='inactivo')
    def __str__(self):
        return self.nombre + " - " + self.estado;

class Publicacion(models.Model):
    categoria = models.ManyToManyField(Categoria)
    titulo = models.CharField(max_length=75, unique=True, null=False)
    contenido = models.TextField(null=False)
    imagen = models.ImageField(null=True, upload_to="blog");
    publicado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True, max_length=25)
    meGusta = models.IntegerField(default=0)
    noMeGusta = models.IntegerField(default=0)
    estado = models.CharField(max_length=25, default='inactivo')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f'%s (%s)' % (self.titulo, self.autor)

class Comentario(models.Model):
    comentario = models.TextField(null=False)
    publicado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    meGusta = models.IntegerField(default=0)
    noMeGusta = models.IntegerField(default=0)
    estado = models.CharField(max_length=25, default='inactivo')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

    def __str__(self):
        return f'%s dijo: %s. %s' % (self.autor, self.comentario, self.publicado)
