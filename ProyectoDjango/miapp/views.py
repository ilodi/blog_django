from django.shortcuts import render, redirect
#contrib es el nucleo de django
#para hacer uso de mensajes flash
from django.contrib import messages
#formulario por defecto
from django.contrib.auth.forms import UserCreationForm
# importat formulario propio
from .forms import RegisterForm
#modulo de autentificacion
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title':'Inicio Django'
    })

#decorador antes de que se reinicie
def about(request):
    return render(request, 'mainapp/about.html',{
        'title':'Sobre nosotros'
    })


def register_page(request):
    #comprobar si el usuario esta identificado
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
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
     #comprobar si el usuario esta identificado
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        #logica para login
        #comprobas lo que llega  
        if request.method=='POST':
            #si llega se va a crear un formulario
            #se identifica por el name de los inputs
            username = request.POST.get('username')
            password = request.POST.get('password')

            #crear el metodo de usuario
            user = authenticate(request, username=username, password=password)

            #si es correcto
            #is no es un operador de si no esto entonces esto
            if user is not None:
                login(request, user)
                return redirect('inicio')
            else:
                #si no funciona un mensaje flash
                messages.warning(request, 'No te has podido identificar')

        return render(request, 'users/login.html',{
            'title': 'Login'
        })


def logout_user(request):
    logout(request)
    return redirect('inicio')


