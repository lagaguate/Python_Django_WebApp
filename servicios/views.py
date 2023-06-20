from django.shortcuts import render
# Instanciamos las vistas genéricas de Django
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares
from django.urls import reverse

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

# Habilitamos los formularios en Django
from django import forms

from servicios.models import Servicio


# Create your views here.

#########################################
# Create your views here Servicio
########################################

class ServicioListado(ListView):
    # Llamamos a la clase 'Servicio' que se encuentra en nuestro archivo 'models.py'
    model = Servicio


class ServicioCrear(SuccessMessageMixin, CreateView):
    # Llamamos a la clase 'Servicio' que se encuentra en nuestro archivo 'models.py'
    model = Servicio
    form = Servicio  # Definimos nuestro formulario con el nombre de la clase o modelo 'Servicio'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Servicio' de nuestra Base de Datos
    # Mostramos este Mensaje luego de Crear un Postre
    success_message = 'Servicio Creado Correctamente !'

    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):
        return reverse('leerservicio')  # Redireccionamos a la vista principal 'leer'


class ServicioDetalle(DetailView):
    # Llamamos a la clase 'Servicio' que se encuentra en nuestro archivo 'models.py'
    model = Servicio


class ServicioActualizar(SuccessMessageMixin, UpdateView):
    # Llamamos a la clase 'Servicio' que se encuentra en nuestro archivo 'models.py'
    model = Servicio
    form = Servicio  # Definimos nuestro formulario con el nombre de la clase o modelo 'Servicio'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Servicio' de nuestra Base de Datos
    # Mostramos este Mensaje luego de Editar un Postre
    success_message = 'Servicio Actualizado Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        return reverse('leerservicio')  # Redireccionamos a la vista principal 'leer'


class ServicioEliminar(SuccessMessageMixin, DeleteView):
    model = Servicio
    form = Servicio
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Postre
        success_message = 'Servicio Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        return reverse('leerservicio')  # Redireccionamos a la vista principal 'leer'
