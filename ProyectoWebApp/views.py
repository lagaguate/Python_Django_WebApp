from django.shortcuts import render, HttpResponse

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


