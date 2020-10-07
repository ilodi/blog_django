from .models import Category

#para poder sacar todas la paginas guardadas desde cualquier parte
#proyecto o plantillas
#crear como una vista global
def get_categories(request):
    #consulta a la base de datos
    #extrart solo 3 datos que ya estan en el modelo
    #puedes mandar texto plano con un, flat=True
    #orden_by() para ordenar la peticion SQL
    categories = Category.objects.values_list('id', 'name')

    return {
        'categories': categories
    }