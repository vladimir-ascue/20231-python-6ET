from django.db import models

# Create your models here.
class usuario(models.Model):
    tipo_documento = models.CharField(max_length=3)
    num_documento = models.CharField(max_length=11, unique=True)
    nombres = models.CharField(max_length=175)
    apellidos = models.CharField(max_length=175)
    estado = models.CharField(max_length=225)

    # python.\manage.py check { % nombreProyecto %}
    # python.\manage.py makemigrations --> Generar el archivo migration "migrations/0001-"
    # python.\manage.py sqlmigrate { % nombreProyecto %} { % numMigracion %}
    # python.\manage.py migrate

    def __str__(self):
        # return 'nombre = %s apellidos = %s' % (self.nombres, self.apellidos)
        return self.apellidos +  ', ' + self.nombres + ' - doc:' + self.num_documento

class publicacion(models.Model):
    titulo = models.CharField(max_length=250)
    cuerpo = models.CharField(max_length=1500)
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo +  ' Por: ' + self.autor.nombres