"""
ProyectoWebApp URL Configuration
 . Crear urls.py dentro del proyecto y configurar todas las urls de la aplicacion

"""

from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static
from ProyectoWebApp.views import ServicioListado, ServicioDetalle, ServicioCrear, ServicioActualizar, ServicioEliminar

#
# Dentro del proyecto se Crean los path de nuestro proyecto
#
# path('serviciosxx', views.servicios, name="Servicios"),
urlpatterns = [
    path('', views.home, name="Home"),
    
    path('tienda', views.tienda, name="Tienda"),
    path('blog', views.blog, name="Blog"),
    path('contacto', views.contacto, name="Contacto"),
    
    # La ruta 'leer' en donde listamos todos los registros de la Base de Datos
    path('servicios/', ServicioListado.as_view(template_name="ProyectoWebApp/servicios/index.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un registro
    path('servicios/detalles/<int:pk>',
         ServicioDetalle.as_view(template_name="ProyectoWebApp/servicios/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo registro
    path('servicios/crear',
         ServicioCrear.as_view(template_name="ProyectoWebApp/servicios/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un registro de la Base de Datos
    path('servicios/editar/<int:pk>', ServicioActualizar.as_view(
        template_name="ProyectoWebApp/servicios/actualizar.html"), name='editar'),

    # La ruta 'eliminar' que usaremos para eliminar un registro de la Base de Datos
    path('servicios/eliminar/<int:pk>',
         ServicioEliminar.as_view(), name='eliminar'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,
                           document_root = settings.MEDIA_ROOT)
