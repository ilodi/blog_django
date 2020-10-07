from django.db import models
from ckeditor.fields import RichTextField
# 1.- Importar modelo
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Creado el")

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default='null', verbose_name="Cover", upload_to="articles")
    public = models.BooleanField(verbose_name="¿Publicado?")
    # Relacion de uno a uno 
    # relacion con modelo Django por defecto
    # 2.- Como este valor se extiende de otro modelo se ura
    # 3.- ForeignKey(Su modelo necesario)
    # on_delete que va a pasar al borrar este modelo
    # models.CASCADE ejemplo si se borra el usuario se borara sus articulos
    # models.PROTECT al borrar el usuario este no se borrara
    user = models.ForeignKey(User,editable=False, verbose_name="Usuario", on_delete=models.CASCADE)
   # Relacion de uno a muchos
   # primer parametro con que modelo se va relacionar
    categorys = models.ManyToManyField(Category, verbose_name="Categorias", blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Editado")

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        #orden decendente
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
