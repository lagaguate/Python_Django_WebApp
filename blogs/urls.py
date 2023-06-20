

from django.urls import path
from servicios import views
from django.conf import settings
from django.conf.urls.static import static
from blogs.views import CategoriaListado, CategoriaDetalle, CategoriaCrear, CategoriaActualizar, CategoriaEliminar

#
# URLS de Categoria de Blogs
#

urlpatterns = [
    
    # La ruta 'leer' en donde listamos todos los registros de la Base de Datos
    path('', CategoriaListado.as_view(template_name="blogs/index.html"), name='leerblog'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un registro
    path('detalles/<int:pk>',
         CategoriaDetalle.as_view(template_name="blogs/detalles.html"), name='detalles'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo registro
    path('crear',
         CategoriaCrear.as_view(template_name="blogs/crear.html"), name='crear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un registro de la Base de Datos
    path('editar/<int:pk>', CategoriaActualizar.as_view(
        template_name="blogs/actualizar.html"), name='editar'),

    # La ruta 'eliminar' que usaremos para eliminar un registro de la Base de Datos
    path('eliminar/<int:pk>',
         CategoriaEliminar.as_view(), name='eliminar'),
]


