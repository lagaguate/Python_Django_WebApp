from django.shortcuts import render, HttpResponse
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


# Create your views here Servicio

class ServicioListado(ListView): 
    model = Servicio # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 


class ServicioCrear(SuccessMessageMixin, CreateView): 
    model = Servicio # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py'
    form = Servicio # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres'
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Postre Creado Correctamente !' # Mostramos este Mensaje luego de Crear un Postre
 
    # Redireccionamos a la página principal luego de crear un registro o postre
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

class ServicioDetalle(DetailView): 
    model = Servicio # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 


class ServicioActualizar(SuccessMessageMixin, UpdateView): 
    model = Servicio # Llamamos a la clase 'Postres' que se encuentra en nuestro archivo 'models.py' 
    form = Servicio # Definimos nuestro formulario con el nombre de la clase o modelo 'Postres' 
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos 
    success_message = 'Postre Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
 
    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):               
        return reverse('leer') # Redireccionamos a la vista principal 'leer'


class ServicioEliminar(SuccessMessageMixin, DeleteView): 
    model = Servicio 
    form = Servicio
    fields = "__all__"     

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self): 
        success_message = 'Postre Eliminado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre 
        messages.success (self.request, (success_message))       
        return reverse('leer') # Redireccionamos a la vista principal 'leer'

def home(request):
    return render(request, "ProyectoWebApp/home.html")


def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "ProyectoWebApp/servicios.html", {"servicios": servicios})



def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")


def blog(request):
    return render(request, "ProyectoWebApp/blog.html")


def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")
