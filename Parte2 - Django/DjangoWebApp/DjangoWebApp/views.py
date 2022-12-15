from django.template import Context, Template, loader
from django.http import HttpResponse

rutaTemplates = "D:/OneDrive/Documentos/Trabajo/Clientes/khipu/Python/2023-1 6ET/20231-python-6ET/Parte2 - Django/"

def landing(response):
    doc = open( rutaTemplates + "DjangoWebApp/plantillas/landing.html" )
    plant = Template( doc.read() )
    doc.close()
    datos = {"nombre": "Vladimir"}
    contexto = Context(datos)
    salida = plant.render(contexto)
    return HttpResponse(salida)

def contacto(response):
    doc = loader.get_template("formulario.html")
    salida = doc.render()
    return HttpResponse(salida)

def portafolio(response):
    doc = loader.get_template("portafolio.html")
    return HttpResponse(doc.render())

def productos(response):
    return HttpResponse(loader.get_template("productos.html").render())

def home(response):
    return HttpResponse(loader.get_template("home.html").render())

