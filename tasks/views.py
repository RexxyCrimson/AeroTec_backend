from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth import authenticate, login

# Crea las vistas aqui

def home(request): # Pagina principal para usuarios externos
    return render(request,'paginaBienvenida.html')

def signin(request): # Inicio de sesión
    if request.method == 'POST':
        email = request.POST.get('correo')
        password = request.POST.get('clave')
        user = authenticate(request, username=email, password=password)  # username se refiere al campo de usuario/email
        
        if user is not None:
            login(request, user)
            return redirect('/menu')  # Redirige a la página de inicio del usuario
        else:
            messages.error(request, 'Correo o contraseña incorrectos')

    return render(request, 'inicioSesion.html')

def signup(request): # Registro de usuario
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
            middle_name=apellidom,
            date_of_birth=nacimiento,
            gender=genero, email=email,
            password=password
        )
        user.save()
        messages.success(request,"Registro exitoso!!")
        return redirect('/signin')
    return render(request,'registrarse.html') # Renderisa el archivo html de registrar

def menu(request): # Menu principal una vez iniciado sesión
    return render(request, 'inicioUser.html')

def vuelos_disponibles(request): # Vista para ver la tabla de vuelos disponibles
    return render(request, 'vuelos_disponibles.html')

def reserva(request): # Vista para reservar un vuelo
    return render(request, 'reservaVuelo.html')

def pago(request): # Vista para agregar el metodo de pago
    return render(request, 'pago.html')

def consultar(request): # Vista para consultar el vuelo agendado FALTA
    return render(request, 'consultarVuelo.html')