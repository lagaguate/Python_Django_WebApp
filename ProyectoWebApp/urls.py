"""
ProyectoWebApp URL Configuration
 . Crear urls.py dentro del proyecto y configurar todas las urls de la aplicacion

"""

from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static

#
# Dentro del proyecto se Crean los path de nuestro proyecto
#
# path('serviciosxx', views.servicios, name="Servicios"),
urlpatterns = [
    path('', views.home, name="Home"),
    
    path('tienda', views.tienda, name="Tienda"),
    path('contacto', views.contacto, name="Contacto"),
        
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,
                           document_root = settings.MEDIA_ROOT)
