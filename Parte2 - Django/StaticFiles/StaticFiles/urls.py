from django.contrib import admin
from django.urls import path
from StaticFiles.views import home, nosotros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('nosotros/', nosotros),
]
