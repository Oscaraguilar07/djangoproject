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



def mostrar_productos(request):
    # Configura la conexión a la base de datos
    conexion = MySQLdb.connect(
        host='localhost',
        user='root',
        password='',
        db='tienda_virtual'
    )

    # Crea un cursor para ejecutar consultas SQL
    cursor = conexion.cursor()

    # Ejecuta una consulta para obtener todos los productos
    cursor.execute('SELECT * FROM productos')

    # Obtiene todos los resultados de la consulta
    productos = cursor.fetchall()

    # Cierra la conexión
    cursor.close()
    conexion.close()

    # Renderiza la plantilla con los productos
    return render(request, 'index.html', {'productos': productos})
