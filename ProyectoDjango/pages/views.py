from django.shortcuts import render
# hacer consulta
from .models import Page
# decoradores de la auth
from django.contrib.auth.decorators import login_required


# decoradores antes de comenzar el metodo
# parametros a mandar a donde quieres que te lleve
@login_required(login_url="login")
def page(request, slug):
    # hacer consulta filtrar x = y
    page = Page.objects.get(slug=slug)
    return render(request, 'pages/page.html', {
        "page": page
    })
