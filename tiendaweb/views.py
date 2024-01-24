from django.shortcuts import render 
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

def index (request):
    return render (request,'index.html',{
    
    })

def login_views (request):
    if request.method == 'POST':
        usuario = request.POST.get('usario')
        contraseña = request.POST.get('contraseña')
        
        user = authenticate(username=usuario, contraseña=contraseña)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect ('index')
        else
        messages.error(request, 'usuario o contraseña no vaido')
        
    return render (request,'login.html', {
 
    })  
    
def registro_views (request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        correo = request.POST.get('correo')
        password_plano = request.POST.get('clave')
         # Hashea la contraseña antes de guardarla en la base de datos
        hashed_password = make_password(password_plano)
        #mensaje de éxito
        return HttpResponse('Usuario registrado con éxito!')
    return render (request,'registro.html', {
 
    })