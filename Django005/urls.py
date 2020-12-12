"""Django005 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from .views import home
from .views import read_cliente
from .views import create_cliente
from .views import update_cliente
from .views import delete_cliente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home),
    path('', read_cliente, name='read_cliente'),
    path('read_cliente/', read_cliente, name='read_cliente'),
    path('create_cliente/', create_cliente, name='create_cliente'),
    path('update_cliente/<int:id>', update_cliente, name='update_cliente'),
    path('delete_cliente/<int:id>', delete_cliente, name='delete_cliente')
]
