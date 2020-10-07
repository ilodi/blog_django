from django.shortcuts import render
#hacer consulta
from .models import Page

# Create your views here.
#saque una sola vista por pagina
def page(request, slug):
    #hacer consulta filtrar x = y
    page = Page.objects.get(slug=slug)
    return render(request, 'pages/page.html', {
        "page" : page
    })