from django.contrib import admin
from django.urls import path
from PrimeraWebPython.views import saludo, saludo2, suma2numeros, tablaN

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('saludo2/', saludo2),
    path('suma/<num1>/<num2>/', suma2numeros),
    path('tabla/<num>/', tablaN),
]
