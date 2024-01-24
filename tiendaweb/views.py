from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

def index (request):
    return render (request,'index.html',{
    
    })

def login_views (request):
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