from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import VRegistro,cerrar_session, logear


#
# URLS de AutenticacionS
#

urlpatterns = [
    
    # La ruta 'leer' en donde listamos todos los registros de la Base de Datos
    path('registro', VRegistro.as_view(), name='autenticacion'),
    path('login', logear, name='login'),
    path('', cerrar_session, name='cerrarsesion'),

]


