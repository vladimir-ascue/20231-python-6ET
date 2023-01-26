
from django.template import Context, Template, loader
from django.shortcuts import render
from django.http import HttpResponse
from Blog.models import Categoria
from django.utils import timezone

dominio = "http://127.0.0.1:8000/"
rutas = {"home": dominio+"home", "nosotros": dominio+"nosotros", "portafolio":dominio+"portafolio"}

def crearCategoria(request):  ## En lugar de response usaremos request porque incluye por defecto el csrf_token
    nombre = None
    if request.method == 'POST':
        nombre = request.POST['nombre'] # Hace referencia al nombre del input del formulario de la plantilla
        if nombre:
            descripcion = request.POST['descripcion']
            estado = request.POST['estado']
            categoria = Categoria(nombre=nombre, descripcion=descripcion, estado=estado)  # Creo el objeto categoria con los datos obtenidos del POST
            categoria.save() # Guardo el objeto en la BS
            return render(request, "crearCategorias.html",
                          {"nombre": nombre, "hora": timezone.now()})
    return render(request, "crearCategorias.html")

def buscarCategoria(request):
    categoriaBuscada = None
    if request.method == 'POST':
        categoriaBuscada = request.POST['categoriaBuscada']
        if categoriaBuscada:
            categoriaEncontrada = Categoria.objects.get(nombre=categoriaBuscada)
            print(categoriaEncontrada)
            return render(request, "buscarCategoria.html", {"categoriaEncontrada": categoriaEncontrada})
    return render(request, "buscarCategoria.html")

def actualizarCategoria(request):
    return render(request, "actualizarCategoria.html")

