from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from .models import CustomUser, VuelosAgendados, Vuelos, Tarjeta
from django.contrib.auth import authenticate, login
from django.core.serializers import serialize


# Crea las vistas aqui

# Pagina principal para usuarios externos
def home(request):
    return render(request,'paginaBienvenida.html')

# Inicio de sesión
def signin(request):
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

# Registro de usuario
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
            middle_name=apellidom,
            date_of_birth=nacimiento,
            gender=genero, email=email,
            password=password
        )
        user.save()
        messages.success(request,"Registro exitoso!!")
        return redirect('/signin')
    return render(request,'registrarse.html') # Renderisa el archivo html de registrar

# Menu principal una vez iniciado sesión
def menu(request):
    return render(request, 'inicioUser.html')


# Vista para reservar un vuelo
def reserva(request):
    # Obtener todos los registros de vuelos disponibles
    vuelos = Vuelos.objects.all()
    vuelo_selected = None

    # Verificar si se seleccionó un vuelo
    if request.method == 'POST':
        vuelo_id = request.POST.get('vuelo_selected')
        
        if vuelo_id:
            vuelo_selected = Vuelos.objects.get(id=vuelo_id)
            
            # Crear el vuelo agendado (insertarlo en la tabla VuelosAgendados)
            VuelosAgendados.objects.create(
                numero_vuelo=vuelo_selected.numero_vuelo,
                aerolinea=vuelo_selected.aerolinea,
                modelo_avion=vuelo_selected.modelo_avion,
                origen=vuelo_selected.origen,
                destino=vuelo_selected.destino,
                tiempo_salida=vuelo_selected.tiempo_salida,
                tiempo_llegada=vuelo_selected.tiempo_llegada,
                duracion=vuelo_selected.duracion,
                precio=vuelo_selected.precio,
                asientos_disponibles=vuelo_selected.asientos_disponibles,
                asientos_totales=vuelo_selected.asientos_totales
            )

            # Redirigir al usuario a una página de confirmación o de agradecimiento
            return redirect('/consultar')  # Cambia 'pago' por la URL que deseas redirigir

    return render(request, 'reservaVuelo.html', {
        'vuelos': vuelos,
        'vuelo_selected': vuelo_selected
    })


# Vista para agregar el metodo de pago
def pago(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        numero_tarjeta = request.POST.get('numero_tarjeta')
        vigencia = request.POST.get('vigencia')
        cvv = request.POST.get('cvv')

        # Validar datos (opcional)
        if len(numero_tarjeta) != 16 or len(cvv) != 3:
            return HttpResponse("Error: Datos inválidos. Por favor verifica e intenta nuevamente.")

        # Guardar en la base de datos
        Tarjeta.objects.create(
            numero_tarjeta=numero_tarjeta,
            vigencia=vigencia,
            cvv=cvv
        )

        return HttpResponse("¡Tarjeta guardada exitosamente!")
    else:
        return render(request, 'pago.html')

# Vista para consultar el vuelos agendados
def consultar(request):
    vuelos_agendados = VuelosAgendados.objects.all()
    return render(request, 'consultarVuelo.html', {'vuelos_agendados': vuelos_agendados})
