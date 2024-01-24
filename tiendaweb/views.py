from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
import MySQLdb


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
