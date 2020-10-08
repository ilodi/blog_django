from .models import Category, Article


def get_categories(request):

    #despues de hacer un filtro se crea una lista
    #el value_list va a crear una lista del elemento que se le pida
    # se saca en modo plano con flat=True
    categories_in_use = Article.objects.filter(public=True).values_list('categorys', flat=True)
    
    #filtar por ids .filter(id__in=x)
    #sacar solo las categorias que el id este en uno en algun post
    categories = Category.objects.filter(id__in=categories_in_use).values_list('id', 'name')

    return {
        'categories': categories,
        'ids': categories_in_use
    }
