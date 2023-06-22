from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth import authenticate

# Create your views here.

def home(request):
    return render(request, 'home.html')

def quienes_somos(request):
    return render(request, 'about_we.html')

def noticias(request):
    return render(request, 'noticias.html')

def tiempo(request):
    return render(request, 'tiempo.html')

def registro(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        try:
            username = request.POST['user']
            if User.objects.filter(username=username).exists():
                error_message = 'El usuario ya existe'
                return HttpResponse(f"<script>alert('{error_message}'); window.location.href='/register/';</script>")

            if request.POST['password1'] == request.POST['password2']:
                user = User.objects.create_user(username=username, password=request.POST['password1'])
                user_profile = UserProfile(user=user, password=request.POST['password1'])
                user_profile.save()
                success_message = 'Usuario creado exitosamente!'
                return HttpResponse(f"<script>alert('{success_message}'); window.location.href='/home/';</script>")
            else:
                error_message = 'Contraseñas no coinciden'
                return HttpResponse(f"<script>alert('{error_message}'); window.location.href='/register/';</script>")
        except:
            error_message = 'Error en el registro'
            return HttpResponse(f"<script>alert('{error_message}'); window.location.href='/register/';</script>")
    else:
        error_message = 'Método de solicitud no válido'
        return HttpResponse(f"<script>alert('{error_message}'); window.location.href='/register/';</script>")

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        user = authenticate(request, username=request.POST['user'], password=request.POST['pass'])
        if user is None:
            error_message = 'Usuario o contraseña incorrecto'
            return HttpResponse(f"<script>alert('{error_message}'); window.location.href='/login/';</script>")
        else:
            success_message = 'Has iniciado sesión correctamente!'
            return HttpResponse(f"<script>alert('{success_message}'); window.location.href='/';</script>")

def recuperar(request):
    return render(request, 'recuperar.html')

def formulario(request):
    return render(request, 'formulario.html')

