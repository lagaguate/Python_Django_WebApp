from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares
from django.urls import reverse, reverse_lazy

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitamos los formularios en Django
from django import forms
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from tienda.models import CategoriaProducto, Producto
from tienda.forms import CreateProductForm
from tienda.email import CorreoElectronico
from carro.views import Carro
#
# URLS de PROYECTOWEBAPP
#


def contacto(request):
    return render(request, "ProyectoWebApp/tienda.html")

#####################################################
# Metodos Crud categoria producto
#####################################################


class CategoryProductList(ListView):
    paginate_by = 5
    model = CategoriaProducto

#
# Usando form personalizado.  El CreatePostForm, buscarlo en form.py
#

class CategoryProductAdd(SuccessMessageMixin, CreateView):
    # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py'
    model = CategoriaProducto
    form = CategoriaProducto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Servicio'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Servicio' de nuestra Base de Datos
    # Mostramos este Mensaje luego de Crear un Postre
    success_message = 'Categoria producto creado correctamente !'

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('categoriaproductoleer')  # Redireccionamos a la vista principal 'leer'


class CategoryProductDetail(DetailView):
    # Llamamos a la clase 'Contacto' que se encuentra en nuestro archivo 'models.py'

    model = CategoriaProducto


class CategoryProductUpdate(SuccessMessageMixin, UpdateView):
    # Llamamos a la clase 'Contacto' que se encuentra en nuestro archivo 'models.py'
    model = CategoriaProducto
    form = CategoriaProducto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Contacto'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Contacto' de nuestra Base de Datos
    # Mostramos este Mensaje luego de Editar un Postre
    success_message = 'Categoria producto actualizado correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        # Redireccionamos a la vista principal 'leer'
        return reverse('categoriaproductoleer')


class CategoryProductDelete(SuccessMessageMixin, DeleteView):
    model = CategoriaProducto
    form = CategoriaProducto
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Postre
        success_message = 'Categoria producto eliminado correctamente !'
        messages.success(self.request, (success_message))
        # Redireccionamos a la vista principal 'leer'
        return reverse('categoriaproductoleer')

#####################################################
# Metodos Crud producto
#####################################################

#########################################
# Create your views here Producto
########################################

class ProductList(ListView):
    paginate_by=5
    model = Producto
    
#
# Usando form personalizado.  El CreatePostForm, buscarlo en form.py
#
class ProductAdd(SuccessMessageMixin, CreateView):
    model = Producto
    form_class = CreateProductForm
    template_name = "tienda/producto/crear.html"
    success_message = 'Producto creado correctamente !'
    success_url = reverse_lazy("productoleer")
                              

class ProductDetail(DetailView):
    # Llamamos a la clase 'Post' que se encuentra en nuestro archivo 'models.py'
    model = Producto

class ProductUpdate(SuccessMessageMixin, UpdateView):
    # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py'
    model = Producto
    form = Producto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Servicio'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Servicio' de nuestra Base de Datos
    # Mostramos este Mensaje luego de Editar un Postre
    success_message = 'Producto actualizado correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('productoleer')  # Redireccionamos a la vista principal 'leer'

class ProductDelete(SuccessMessageMixin, DeleteView):
    model = Producto
    form = Producto
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Categoria
        success_message = 'Producto eliminado correctamente !'
        messages.success(self.request, (success_message))
        return reverse('productoleer')  # Redireccionamos a la vista principal 'leer'


#########################################
# End Producto
########################################

class TiendaList(ListView):
    paginate_by=8
    model = Producto
    
#########################################
# End Tienda
########################################