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

#
# URLS de PROYECTOWEBAPP
#

def home(request):
    return render(request, "ProyectoWebApp/home.html")

def tienda(request):
    return render(request, "ProyectoWebApp/tienda.html")


def blog(request):
    return render(request, "ProyectoWebApp/blog.html")


def contacto(request):
    return render(request, "ProyectoWebApp/contacto.html")
