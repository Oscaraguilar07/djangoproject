<<<<<<< HEAD
from django.contrib import admin
from django.urls import path

from tiendaweb.views import *

urlpatterns = [
    path('', index, name ='index'),
    path('admin/', admin.site.urls),
]
#h
=======
"""
URL configuration for tiendaweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
>>>>>>> 45bb346a6fa73b2f085a6a21a27f65d0b50f84e7
