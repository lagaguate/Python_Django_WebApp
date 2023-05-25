"""
ProyectoWebApp URL Configuration
 . Crear urls.py dentro del proyecto y configurar todas las urls de la aplicacion

"""

from django.urls import path

from ProyectoWebApp import views

# 
# Dentro del proyecto se Crean los path de nuestro proyecto
# 
urlpatterns = [
    path('', views.home,name="Home"),
    path('servicios', views.servicios,name="Servicios"),
    path('tienda', views.tienda,name="Tienda"),
    path('blog', views.blog,name="Blog"),
    path('contacto', views.contacto,name="Contacto"),
]