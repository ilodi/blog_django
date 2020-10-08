from django.shortcuts import render, get_object_or_404
from .models import Category, Article

# Create your views here.


def list(request):
    # sacar los articulos
    # consultar
    articles = Article.objects.all()
    return render(request, 'articles/list.html', {
        'title': 'Articulos',
        'articles': articles
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
