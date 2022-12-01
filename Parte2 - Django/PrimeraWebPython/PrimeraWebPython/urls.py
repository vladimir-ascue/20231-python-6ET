from django.contrib import admin
from django.urls import path
from PrimeraWebPython.views import saludo, saludo2

urlpatterns = [

    path('saludo/', saludo),
    path('saludo2/', saludo2),

]
