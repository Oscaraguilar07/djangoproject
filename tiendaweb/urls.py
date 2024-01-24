from django.contrib import admin
from django.urls import path

from .views import login_views, registro_views




from tiendaweb.views import index

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_views, name='login'),
    path('registro/', registro_views, name='registro'),
    path('admin/', admin.site.urls),
]
