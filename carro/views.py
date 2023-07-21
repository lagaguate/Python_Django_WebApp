from django.shortcuts import render
from .carro import Carro
from tienda.models import Producto
from django.shortcuts import redirect

# Create your views here.

def agregar_producto(request, producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto)

    return redirect("tiendaleer")


def eliminar_producto(request, producto_id):

    carro = Carro(request)
    prod = Producto.objects.get(id=producto_id)
    
    carro.eliminar(producto=prod)

    return redirect("tiendaleer")

def restar_producto(request, producto_id):

    carro = Carro(request)
    prod = Producto.objects.get(id=producto_id)
    
    carro.restart_producto(producto=prod)

    return redirect("tiendaleer")

def limpiar_carro(request, producto_id):

    carro = Carro(request)
    carro.limpiar_carro()

    return redirect("tiendaleer")



