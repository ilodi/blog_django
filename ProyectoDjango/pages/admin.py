from django.contrib import admin
from .models import *


# Configuración extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('create_at', 'updated_at')
    #agregar buscador
    search_fields = ('title', 'content')
    #filtro visible
    list_filter = ('visible',)
    #sacar columnas en la lista
    list_display = ('title', 'visible' )
    #ordenar por defecto
    ordering = ('-create_at',)


# Register your models here.
admin.site.register(Page, PageAdmin)


# configutacion del panel
title = "Proyecto Django"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
