from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from pedidos.models import Pedido,LineaPedido
from carro.carro import Carro
from django.contrib import messages
from tienda.email import CorreoElectronico


# Create your views here.
@login_required(redirect_field_name="login")
def procesar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(

            producto_id=key,
            cantidad=value["cantidad"],
            user=request.user,
            pedido=pedido

        ))

    print("linea pedidos")
    print(lineas_pedido)

    LineaPedido.objects.bulk_create(lineas_pedido)
    detalle="{: <25} {: <5} {: <5}\n{}\n".format("Producto","Cantidad","precio",'-'.ljust(50, '-'))
    for k in lineas_pedido:
        detalle=detalle+"{: <25} {: <11} {: <10}\n".format(k.producto.nombre,k.cantidad,k.producto.precio)

    # para que funcione, debe registratdr los usuarios con su correo electronico
    emailusuario="lagaguate@yahoo.com"
    body = render_to_string("emails/pedidos.html",{
        "pedido_id": pedido.id,
        "detalle":detalle,
        "usuario":request.user,
        "emailusuario": emailusuario
    })
    body_text = strip_tags(body)
    subject="Pedido ordenado"
    CorreoElectronico.enviarcorreo(emailusuario, subject, body_text)
    

    messages.success(request,"Pedido creado exitosamente")

    return redirect('tiendaleer')

