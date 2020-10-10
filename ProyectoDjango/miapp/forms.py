#para hacer formularios personalizados
from django import forms
from django.core import validators

#importat formulario por defecto
from django.contrib.auth.forms import UserCreationForm
#importat modelos
from django.contrib.auth.models import User

#crear formulario
class RegisterForm(UserCreationForm):
    class Meta:
        #para que se forme solo en base a un modelo
        model = User
        #que campos va a tener el usuario
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2'
        ]