from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .models import CustomUser

# Crea las vistas aqui
# Funcion que retorna y renderiza el archivo html signup
def home(request):
    return render(request,'paginaBienvenida.html')

def signin(request):
    return render(request,'inicioSesion.html')

def signup(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellidop = request.POST.get('apellidop')
        apellidom = request.POST.get('apellidom')
        nacimiento = request.POST.get('nacimiento')
        genero = request.POST.get('genero')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        password1 = request.POST.get('pass1')

        # Validaciones basicas
        if password != password1:
            messages.error(request,"Las contraseñas no coinciden")
            return redirect('signup')
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request,"El correo ya esta registrado")
            return redirect('signup')
        
        # Crear usuario
        user = CustomUser.objects.create_user(
            first_name=nombre,
            last_name=apellidop,
            date_of_birth=nacimiento,
            gender=genero, email=email,
            password=password
        )
        user.save()
        messages.success(request,"Registro exitoso!!")
        return redirect('Menu Home')
    return render(request,'registrarse.html') # Renderisa el archivo html de registrar