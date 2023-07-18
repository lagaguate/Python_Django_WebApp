from django.urls import path
from contacto import views
from django.conf import settings
from django.conf.urls.static import static
from carro.views import agregar_producto , eliminar_producto, restar_producto, limpiar_carro
#
# URLS de ContactoS
#
app_name = "carro"
urlpatterns = [

    
    #################################################################
    #  CRUD de Carrito
    # ############################################################### 
    # Product List
    path('agregarproducto/<int:producto_id>', agregar_producto, name='agregarproducto'),

    path('eliminar/<int:producto_id>', eliminar_producto, name='eliminarproducto'),

    path('restarproducto/<int:producto_id>', restar_producto, name='restarproducto'),

    path('limpiarproducto', limpiar_carro, name='limpiarcarro'),


    
]
