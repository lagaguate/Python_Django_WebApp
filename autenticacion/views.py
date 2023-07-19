from django.shortcuts import render

# Create your views here.

def autentication(request):
    pass

from django.shortcuts import render, HttpResponse
from django.core.paginator import Paginator

# Nos sirve para redireccionar despues de una acción revertiendo patrones de expresiones regulares
from django.urls import reverse, reverse_lazy

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm

#
# URLS de PROYECTOWEBAPP
#

class VRegistro(View):

    def  get(self, request):
        form = UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self,request):
        pass


