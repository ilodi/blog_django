from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Page)


#configutacion del panel
title = "Proyecto Django"
subtitle = "Panel de gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle