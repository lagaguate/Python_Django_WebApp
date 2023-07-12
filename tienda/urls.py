from django.urls import path
from contacto import views
from django.conf import settings
from django.conf.urls.static import static
from tienda.views import CategoryProductDetail, CategoryProductAdd, CategoryProductDelete, CategoryProductList, CategoryProductUpdate
from tienda.views import ProductList, ProductAdd, ProductDetail, ProductUpdate, ProductDelete
from tienda.views import TiendaList
#
# URLS de ContactoS
#

urlpatterns = [

    # Tienda
    path('', TiendaList.as_view(template_name="tienda.html"), name='tiendaleer'),

    # Categoria producto listar
    path('categoria', CategoryProductList.as_view(
        template_name="categoria/listado.html"), name='categoriaproductoleer'),

    # Categoria producto detalles
    path('categoria/detalles/<int:pk>',
         CategoryProductDetail.as_view(template_name="categoria/detalles.html"), name='categoriaproductodetalle'),

    # Categoria producto crear
    path('categoria/crear',
         CategoryProductAdd.as_view(template_name="categoria/crear.html"), name='categoriaproductocrear'),

    # Categoria producto actualizar
    path('categoria/editar/<int:pk>', CategoryProductUpdate.as_view(
        template_name="categoria/actualizar.html"), name='categoriaproductoeditar'),

    # Categoria producto eliminar
    path('categoria/eliminar/<int:pk>',
         CategoryProductDelete.as_view(), name='categoriaproductoeliminar'),

    # Product List
    path('producto', ProductList.as_view(
        template_name="tienda/product/index.html"), name='productoleer'),

    # La ruta 'detalles' en donde mostraremos una página con los detalles de un registro
    path('producto/detalles/<int:pk>',
         ProductDetail.as_view(template_name="tienda/producto/detalles.html"), name='productodetalle'),

    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevo registro
    path('producto/crear',
         ProductAdd.as_view(template_name="tienda/producto/crear.html"), name='productocrear'),

    # La ruta 'actualizar' en donde mostraremos un formulario para actualizar un registro de la Base de Datos
    path('producto/editar/<int:pk>', ProductUpdate.as_view(
        template_name="tienda/producto/actualizar.html"), name='productoeditar'),

    # La ruta 'eliminar' que usaremos para eliminar un registro de la Base de Datos
    path('producto/eliminar/<int:pk>',
         ProductDelete.as_view(), name='productoeliminar'),
]
