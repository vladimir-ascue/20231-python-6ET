from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Blog.views import crearCategoria, buscarCategoria, actualizarCategoria


urlpatterns = [
    path('admin/', admin.site.urls),
    path('crearCategoria/', crearCategoria),
    path('buscarCategoria/', buscarCategoria),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)