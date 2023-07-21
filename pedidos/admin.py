from django.contrib import admin

# Register your models here.

from .models import Pedido, LineaPedido

admin.site.register([Pedido,LineaPedido])