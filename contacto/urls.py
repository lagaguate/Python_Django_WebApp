from django.urls import path
from contacto import views
from django.conf import settings
from django.conf.urls.static import static
from contacto.views import AddPContacto, ContactoListado, ContactoActualizar,ContactoDetalle, ContactoEliminar

#
# URLS de ContactoS
#

urlpatterns = [
    
    # La ruta 'leer' en donde listamos todos los registros de la Base de Datos
    path('listado', ContactoListado.as_view(template_name="contacto/index.html"), name='leerContacto'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un registro
    path('detalles/<int:pk>',
         ContactoDetalle.as_view(template_name="contacto/detalles.html"), name='detalleContacto'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo registro
    path('crear',
         AddPContacto.as_view(template_name="contacto/crear.html"), name='crearContacto'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un registro de la Base de Datos
    path('editar/<int:pk>', ContactoActualizar.as_view(
        template_name="contacto/actualizar.html"), name='editarContacto'),

    # La ruta 'eliminar' que usaremos para eliminar un registro de la Base de Datos
    path('contacto/eliminar/<int:pk>',
         ContactoEliminar.as_view(), name='eliminarContacto'),
]


