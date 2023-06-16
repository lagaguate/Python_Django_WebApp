

from django.urls import path
from servicios import views
from django.conf import settings
from django.conf.urls.static import static
from servicios.views import ServicioListado, ServicioDetalle, ServicioCrear, ServicioActualizar, ServicioEliminar

#
# URLS de SERVICIOS
#

urlpatterns = [
    
    # La ruta 'leer' en donde listamos todos los registros de la Base de Datos
    path('', ServicioListado.as_view(template_name="servicios/index.html"), name='leer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un registro
    path('detalles/<int:pk>',
         ServicioDetalle.as_view(template_name="servicios/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo registro
    path('crear',
         ServicioCrear.as_view(template_name="servicios/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un registro de la Base de Datos
    path('editar/<int:pk>', ServicioActualizar.as_view(
        template_name="servicios/actualizar.html"), name='editar'),

    # La ruta 'eliminar' que usaremos para eliminar un registro de la Base de Datos
    path('eliminar/<int:pk>',
         ServicioEliminar.as_view(), name='eliminar'),
]


