from django.contrib import admin
from django.urls import path
from DjangoWebApp.views import landing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', landing),
]
