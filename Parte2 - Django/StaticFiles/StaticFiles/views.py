from django.template import Context, Template, loader
from django.http import HttpResponse

dominio = "http://127.0.0.1:8000/"
rutas = {"home": dominio+"home", "nosotros": dominio+"nosotros"}

def home(response):
    doc = loader.get_template("home.html")
    salida = doc.render(rutas)
    return HttpResponse(salida)


def nosotros(response):
    doc = loader.get_template("nosotros.html")
    return HttpResponse(doc.render(rutas))

