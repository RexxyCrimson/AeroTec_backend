from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Crea las vistas aqui
# Funcion que retorna y renderiza el archivo html signup
def home(request):
    return render(request,'paginaBienvenida.html')

def signup(request):

    if request.method == 'GET':
        return render(request,'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Registro de usuario
            try:
                user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
                )
                user.save()
                return HttpResponse('Usuario creado correctamente!!!')
            except:
                return HttpResponse('El usuario ya existe!!')
        return HttpResponse('Las contraseñas no coinciden')