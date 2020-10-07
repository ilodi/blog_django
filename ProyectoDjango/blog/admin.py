from django.contrib import admin
from .models import *


# solo lectura
class CategoryAdmin(admin.ModelAdmin):
    # lleva una coma para que se interprete como una tupla
    readonly_fields = ('created_at',)


class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'user')

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
