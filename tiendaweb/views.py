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
    return render (request,'registro.html', {
 
    })