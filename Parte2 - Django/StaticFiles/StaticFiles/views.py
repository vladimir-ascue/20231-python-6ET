from idlelib.pyshell import use_subprocess

from django.template import Context, Template, loader
from django.http import HttpResponse
from blog.models import usuario

dominio = "http://127.0.0.1:8000/"
rutas = {"home": dominio+"home", "nosotros": dominio+"nosotros", "portafolio":dominio+"portafolio"}

def home(response):
    doc = loader.get_template("home.html")
    salida = doc.render(rutas)
    return HttpResponse(salida)

def nosotros(response):
    doc = loader.get_template("nosotros.html")
    return HttpResponse(doc.render(rutas))

def portafolio(response):
    return HttpResponse(loader.get_template("portafolio.html").render(rutas))
