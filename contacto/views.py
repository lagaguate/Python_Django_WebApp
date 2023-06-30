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

from contacto.models import Contacto
from contacto.forms import CreateContactoForm
from contacto.email import CorreoElectronico
#
# URLS de PROYECTOWEBAPP
#


def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")

#########################################
# Create your views here Contacto
########################################


class ContactoListado(ListView):
    paginate_by = 5
    model = Contacto

#
# Usando form personalizado.  El CreatePostForm, buscarlo en form.py
#


class AddPContacto(SuccessMessageMixin, CreateView):
    model = Contacto
    form_class = CreateContactoForm
    template_name = "contacto/crear.html"
    success_message = 'Contacto creado correctamente !'

    def get_success_url(self):
        # Si el post fue OK, entonces recupere los campos
        if self.request.method == 'POST':
            email = self.request.POST.get('email')
        body = "Correo registrado: "+email
        mycorreo = CorreoElectronico
        mycorreo.enviarcorreo("lagaguate@yahoo.com", "Test de envio", body)
        
        return reverse_lazy("Home")
    #


class ContactoDetalle(DetailView):
    # Llamamos a la clase 'Contacto' que se encuentra en nuestro archivo 'models.py'

    model = Contacto


class ContactoActualizar(SuccessMessageMixin, UpdateView):
    # Llamamos a la clase 'Contacto' que se encuentra en nuestro archivo 'models.py'
    model = Contacto
    form = Contacto  # Definimos nuestro formulario con el nombre de la clase o modelo 'Contacto'
    fields = "__all__"  # Le decimos a Django que muestre todos los campos de la tabla 'Contacto' de nuestra Base de Datos
    # Mostramos este Mensaje luego de Editar un Postre
    success_message = 'Contacto Actualizado Correctamente !'

    # Redireccionamos a la página principal luego de actualizar un registro o postre
    def get_success_url(self):
        # Redireccionamos a la vista principal 'leer'
        return reverse('leerContacto')


class ContactoEliminar(SuccessMessageMixin, DeleteView):
    model = Contacto
    form = Contacto
    fields = "__all__"

    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):
        # Mostramos este Mensaje luego de Editar un Postre
        success_message = 'Contacto Eliminado Correctamente !'
        messages.success(self.request, (success_message))
        # Redireccionamos a la vista principal 'leer'
        return reverse('leerContacto')
