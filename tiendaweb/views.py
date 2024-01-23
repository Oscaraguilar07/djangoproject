from django.shortcuts import render
from django.http import HttpResponse


def index (request):
    return render (request,'index.html',{
        'message': 'wili😘😘'
    })

def login_views (request):
    return render (request,'login.html', {
 
    })
    
def registro_views (request):
    return render (request,'registro.html', {
 
    })