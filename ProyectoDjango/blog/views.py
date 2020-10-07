from django.shortcuts import render
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
