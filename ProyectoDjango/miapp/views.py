from django.shortcuts import render, redirect
#contrib es el nucleo de django
#para hacer uso de mensajes flash
from django.contrib import messages
#formulario por defecto
from django.contrib.auth.forms import UserCreationForm
# importat formulario propio
from .forms import RegisterForm


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
    #llamar form por defecto
   # register_form = UserCreationForm()

    #hacer uso de formulario propio
    register_form = RegisterForm()

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
            ##mensajes flash solo duran una actualizacion en pantalla
            messages.success(request, 'Te has registrado correctamente')
            return redirect('inicio')

    return render(request, 'users/register.html',{
       'title':'Registro' ,
       'register_form':register_form
    })

def login_page(request):
    return render(request, 'users/login.html',{
        'title': 'Login'
    })