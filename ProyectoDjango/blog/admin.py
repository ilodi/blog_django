from django.contrib import admin
from .models import *


# solo lectura
class CategoryAdmin(admin.ModelAdmin):
    # lleva una coma para que se interprete como una tupla
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name',)


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'user')
    # el doble __ es para acceder a una propiedade de un modelo
    list_filter = ('title', 'public', 'user')
    list_display = ('title', 'public', 'user')

    # modificar algo cuando se guarde
    # los parametros son necesarios
    def save_model(self, request, obj, form, change):
        # si no me llega un usuario
        # entonces vas a guardar lo que viene en la consula
        if not obj.user_id:
            obj.user_id = request.user.id
            # si no existe algo en este caso esta propiedad
        obj.save()


# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
