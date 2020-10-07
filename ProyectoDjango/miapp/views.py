from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio Django'
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title':'Sobre nosotros'
    })