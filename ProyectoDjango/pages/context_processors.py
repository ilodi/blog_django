from pages.models import Page

#para poder sacar todas la paginas guardadas desde cualquier parte
#proyecto o plantillas
#crear como una vista global
def get_pages(request):
    #consulta a la base de datos
    #extrart solo 3 datos que ya estan en el modelo
    #puedes mandar texto plano con un, flat=True
    #orden_by() para ordenar la peticion SQL
    pages = Page.objects.filter(visible=True).order_by('order').values_list('id', 'title', 'slug')

    return {
        'pages': pages
    }