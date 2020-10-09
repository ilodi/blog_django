from django.shortcuts import render, get_object_or_404
#objeto que ayuda a hacer la paginacion
from django.core.paginator import Paginator
from .models import Category, Article

# Create your views here.


def list(request):
    # sacar los articulos
    # consultar
    articles = Article.objects.all()
    #para crear un paginador 
    #primero se importa paginator
    #necesita la consulta y el numero de elementos por pagina
    paginator = Paginator(article, 2)
   
   
    #recoger el numero de pagina por url
    #para recoger lo que se manda por la url mediante GET
    page = request.GET.get('page')
    #recoge el valor de la pagina que esta en url
    page_articles = paginator.get_page(page)
    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': 'page_articles'
    })


def category(request, category_id):
    #category = Category.objects.get(id=category_id)
    # agregar 404
    category = get_object_or_404(Category, id=category_id)
    # articulos que tengan la categoria
    articles = Article.objects.filter(categorys=category_id)
    return render(request, 'categories/category.html', {
        'category': category,
        'articles': articles
    })


def article(request, article_id):
    # va a hacer la consulta a Article de su campo id=article_id
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article': article
    })
