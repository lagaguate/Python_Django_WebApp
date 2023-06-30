Python_Django_WebApp
========================

**Autor**: Luis Gutierrez

**Twitter**:@lagaguate

**email**: <lagaguate@yahoo.com>

Ultimo Cambio: 29/06/23

Tags: `Python`, `Django`

# Introducción

Es un ejercicio utilizando Python + Django, basado en un video tutorial de **pildorasinformativas**.  Este proyecto tiene variantes, aunque reconozco que el video me ayudo abrir mas la menta con relacion de **Python** y **Django**.

[Curso Django. Introducción e Instalación.Vídeo 1 - YouTube](https://www.youtube.com/watch?v=7XO1AzwkPPE&list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB) Curso Django

Es importante comentar que estoy usando **Linux Ubuntu**, por ese motivo uso **python3** en la linea de comando

- Versión Ubuntu
*Distributor ID: Ubuntu
Description: Ubuntu 22.04.2 LTS
Release: 22.04
Codename: jammy

*

- Versión Python
*Python 3.10.11*
- Versión Djando
*>>> import django

>>> django.VERSION
(4, 1, 0, 'final', 0)*

El proyecto usa bootstrap5,  widget_tweaks

## Comando con Django

1. Ejecutar el comando para crear un proyecto en Django.

```
django-admin startproject AplicacionWeb
```

2. Django crear un proyecto como primer paso, con el nombre  **ProyectoWebApp**.

```
python3 manage.py start app ProyectoWebApp
```

3. Ejecutar el servidor web de Django.

```
python3 manage.py runserver
```

# Registrar la aplicación en el proyecto

1. A nivel de proyecto, buscar el archivo **settings.py** y abrirlo
2. En la sección de **INSTALLED_APPS** registrar la aplicación.  Al momento de actualizar el readme.md ya teniamos otras aplicaciones creadas.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'generic_scaffold',
    'bootstrap5',
    'django_bootstrap_icons',
    'widget_tweaks',
    'ProyectoWebApp',
    'servicios',
    'blogs',
]
```

# Crear la APP Servicios

Para crear la app Servicios, se debe ejecutar estos comando de Python.   Importante que cada vez que se agregue o modifique el moldeo se debe repetir el makemigrations y  migrate

```
python3 manage.py startapp servicios
python3 manage.py makemigrations servicios
python3 manage.py migrate servicios
```

# Crear la APP Blog

**Nota:** Por cada nuevo modelo o modificación se debe ejecutar el paso 2 y 3

```
python3 manage.py startapp blogs
python3 manage.py makemigrations blogs
python3 manage.py migrate blogs
```

# Crear la APP Contactos

```
python3 manage.py startapp contacto
python3 manage.py makemigrations contacto
python3 manage.py migrate contacto
```

# Crear la APP Tienda

```
python3 manage.py startapp tienda
python3 manage.py makemigrations tienda
python3 manage.py migrate tienda
```

# Crear super usuario de Django

Para aprovechar las plantillas de CRUD de Django, es importante crear un super usuario.  

```
python manage.py createsuperuser
```

Defines el usuairo

- usuario: lagaguate
- email: lagaguate
. pass: xxxxxxxx

## En cada APP, se debe agregar la aplicación en admin.py

Cuando creas un proyecto, es importante aprovecha las ventajas de Admin, permite realizar CRUD sobre los datos.
Procedimiento:

1. Buscar el archivo admin.py dentro de la APP creada.
2. Dar los permisos y registrarla. Ver codigo

```
from django.contrib import admin
from .models import Servicio



# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio,ServicioAdmin)
```
