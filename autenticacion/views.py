from django.shortcuts import render, redirect

# Habilitamos el uso de mensajes en Django
from django.contrib import messages

# Habilitamos los mensajes para class-based views
from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import View
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#
# URLS de PROYECTOWEBAPP
#

class VRegistro(View):

    def  get(self, request):
        form = UserCreationForm()
        return render(request,"registro/registro.html",{"form":form})

    def post(self,request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
           usuario = form.save()

           login(request,usuario)
           list(messages.get_messages(request))
           return redirect('Home')
        else: 
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request,"registro/registro.html",{"form":form})
        
def cerrar_session(request):
    logout(request)
    return redirect('Home')

def logear(request):
    if request.method=="POST":
       form = AuthenticationForm(request,data=request.POST)
       if form.is_valid():
            nombre_usuario=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")
            usuario = authenticate(username=nombre_usuario, password=clave)
            if usuario is not None:
                login(request,usuario)
                list(messages.get_messages(request))
                return redirect('Home')
            else:
                messages.error(request, "Usuario invalido")
       else:
            messages.error(request, "Informacion incorrecta")

    form = AuthenticationForm
    return render(request,"login/login.html",{"form":form})

