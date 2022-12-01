from django.template import Context, Template
from django.http import HttpResponse

rutaTemplates = "D:/OneDrive/Documentos/Trabajo/Clientes/khipu/Python/2023-1 6ET/20231-python-6ET/Parte2 - Django/"


def landing(response):
    doc = open(rutaTemplates + "DjangoWebApp/plantillas/landing.html")
    plant = Template(doc.read())
    doc.close()
    datos = {"nombre": "Vladimir"}
    contexto = Context(datos)
    salida = plant.render(contexto)
    return HttpResponse(salida)
