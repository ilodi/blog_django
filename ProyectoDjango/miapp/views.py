from django.shortcuts import render, redirect
#formulario por defecto
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio Django'
    })

def about(request):
    return render(request, 'mainapp/about.html',{
        'title':'Sobre nosotros'
    })

def register_page(request):
    #llamar form
    register_form = UserCreationForm()

    #comprovar antes de registrar
    #si hay un methodo post se le mandara a la 
    #funcion que extiendes del form
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        #si sale correctamente
        if register_form.is_valid():
            #guardas el formulario
            register_form.save()
            #si todo sale bien se redireccionara
            return redirect('inicio')

    return render(request, 'users/register.html',{
       'title':'Registro' ,
       'register_form':register_form
    })