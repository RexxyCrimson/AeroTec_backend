from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Crea las vistas aqui
# Funcion que retorna y renderiza el archivo html signup
def home(request):
    return render(request,'paginaBienvenida.html')

def signin(request):
    return render(request,'inicioSesion.html')

def signup(request):
    return render(request,'registrarse.html')