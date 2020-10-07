from django.db import models
#importat
from ckeditor.fields import RichTextField


# Create your models here.
#crear paginas
class Page(models.Model):
    title = models.CharField( max_length=50, verbose_name="Título")
    #para agregar un mejor editor se cambia
    #content = models.TextField(verbose_name="Contenido")
    content = RichTextField(verbose_name="Contenido")
    slug = models.CharField(unique=True, max_length=144, verbose_name="URL amigable")
    order = models.IntegerField(default=0, verbose_name="Orden")
    visible = models.BooleanField(verbose_name="¿Visible?")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Crado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Actualizado el")
    #agregar parametros al admin ''
    class Meta():
      verbose_name="Página"
      verbose_name_plural = "Páginas"
    #method magico para convertir a str ayuda en el panel de admin
    def __str__(self):
        return self.title
    

#crear base de datos
#1.- python manage.py makemigrations
#2.- python manage.py sqlmigrate NOMBRE DE LA APP NUMERO DE MIGRACION
#3.- python manage.py migrate

#modificar modelo cuando ya esta la db
#1.-Crear migracion
#1.- python manage.py makemigrations
#2.- python manage.py sqlmigrate NOMBRE DE LA APP NUMERO DE MIGRACION
#3.- python manage.py migrate
