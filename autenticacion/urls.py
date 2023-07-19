from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import VRegistro


#
# URLS de AutenticacionS
#

urlpatterns = [
    
    # La ruta 'leer' en donde listamos todos los registros de la Base de Datos
    path('registro', VRegistro.as_view(), name='autenticacion'),

]


