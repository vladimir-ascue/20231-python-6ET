from django.contrib import admin
from django.urls import path
from DjangoWebApp.views import landing, contacto, portafolio, productos, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', landing),
    path('contacto/', contacto),
    path('portafolio/', portafolio),
    path('productos/', productos),
    path('home2/', home),
]
