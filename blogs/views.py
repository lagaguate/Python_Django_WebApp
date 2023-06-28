from django.shortcuts import render
from django.core.paginator import Paginator
# Instanciamos las vistas genéricas de Django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares
from django.urls import reverse, reverse_lazy

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitamos los formularios en Django
from django import forms
from blogs.forms import CreatePostForm


from blogs.models import Categoria, Post

from generic_scaffold import CrudManager



class BlogListado(ListView):
    # Llamamos a la clase 'Servicio' que se encuentra en nuestro archivo 'models.py'
    model = Post

#########################################
# Create your views here Categoria
########################################

class CategoriaListado(ListView):
    # Llamamos a la clase 'Servicio' que se encuentra en nuestro archivo 'models.py'
    model = Categoria

class CategoriaCrear(SuccessMessageMixin, CreateView):
    # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py'
    model = Categoria
    form = Categoria  # Definimos nuestro formulario con el nombre de la clase o modelo 'Servicio'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Servicio' de nuestra Base de Datos
    # Mostramos este Mensaje luego de Crear un Postre
    success_message = 'Categoria Creado Correctamente !'

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('categorialeer')  # Redireccionamos a la vista principal 'leer'

class CategoriaDetalle(DetailView):
    # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py'
    model = Categoria

class CategoriaActualizar(SuccessMessageMixin, UpdateView):
    # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py'
    model = Categoria
    form = Categoria  # Definimos nuestro formulario con el nombre de la clase o modelo 'Servicio'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Servicio' de nuestra Base de Datos
    # Mostramos este Mensaje luego de Editar un Postre
    success_message = 'Categoria Actualizado Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('categorialeer')  # Redireccionamos a la vista principal 'leer'

class CategoriaEliminar(SuccessMessageMixin, DeleteView):
    model = Categoria
    form = Categoria
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Categoria
        success_message = 'Categoria Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('categorialeer')  # Redireccionamos a la vista principal 'leer'

#########################################
# End Categoria
########################################

#########################################
# Create your views here Post
########################################

class PostListado(ListView):
    paginate_by=5
    model = Post
    #model = Post.objects.all()
    #paginator = Paginator(model,5)
    #page_number = request.GET.get('page')

class AddPost(SuccessMessageMixin, CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = "blogs/post/crear.html"
    success_message = 'Post Creado Correctamente !'
    success_url = reverse_lazy("postleer")
                              

class PostDetalle(DetailView):
    # Llamamos a la clase 'Post' que se encuentra en nuestro archivo 'models.py'
    model = Post

class PostActualizar(SuccessMessageMixin, UpdateView):
    # Llamamos a la clase 'Categoria' que se encuentra en nuestro archivo 'models.py'
    model = Post
    form = Post  # Definimos nuestro formulario con el nombre de la clase o modelo 'Servicio'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Servicio' de nuestra Base de Datos
    # Mostramos este Mensaje luego de Editar un Postre
    success_message = 'Post Actualizado Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('postleer')  # Redireccionamos a la vista principal 'leer'

class PostEliminar(SuccessMessageMixin, DeleteView):
    model = Post
    form = Post
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Categoria
        success_message = 'Post Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('postleer')  # Redireccionamos a la vista principal 'leer'


class PostCrudManager(CrudManager):
    model = Post
    prefix = 'post'
#########################################
# End Categoria
########################################