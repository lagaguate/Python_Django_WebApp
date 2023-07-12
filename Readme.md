Python_Django_WebApp
========================

**Autor**: Luis Gutierrez

**Twitter**:@lagaguate

**emails**: <lagaguate@yahoo.com, lagaguate@gmail.com>

Ultimo Cambio: 29/06/23

Tags: `Python`, `Django`

# Introducción

Es un ejercicio utilizando Python + Django, basado en un video tutorial de **pildorasinformativas**.  Este proyecto tiene variantes, aunque reconozco que el video me ayudo abrir mas la menta con el desarrollo  de **Python** y **Django**.

La intención dejar el código en Github para ayuda de otros que necesiten el código fuente.

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

## Comandos Django

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

## Registrar la aplicación en el proyecto

1. A nivel de proyecto, buscar el archivo **settings.py** y abrirlo
2. En la sección de **INSTALLED_APPS** registrar la aplicación.   

**Nota:** Se tienen registrados 5 Apps.  Adelante se deja constancia de la creación de cada APP

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
    'contacto',
    'tienda'
]
```

### Crear las APP 

Para crear la app Servicios, se debe ejecutar estos comando de Python.   Importante que cada vez que se agregue o modifique el moldeo se debe repetir el makemigrations y  migrate

 *Crear la APP proyectoWebApp*
```
python3 manage.py startapp proyectoWebApp
python3 manage.py makemigrations proyectoWebApp
python3 manage.py migrate proyectoWebApp
```


 *Crear la APP servicio*
```
python3 manage.py startapp servicios
python3 manage.py makemigrations servicios
python3 manage.py migrate servicios
```

 *Crear la APP blogs*

**Nota:** Por cada nuevo modelo o modificación se debe ejecutar el paso 2 y 3

```
python3 manage.py startapp blogs
python3 manage.py makemigrations blogs
python3 manage.py migrate blogs
```

 *Crear la APP Contactos*

```
python3 manage.py startapp contacto
python3 manage.py makemigrations contacto
python3 manage.py migrate contacto
```

 *Crear la APP Tienda*

```
python3 manage.py startapp tienda
python3 manage.py makemigrations tienda
python3 manage.py migrate tienda

```
### En cada APPs, configurar modelos en  admin.py

Cuando creas un proyecto, es importante aprovecha las ventajas de Admin, permite realizar CRUD sobre los datos.

Procedimiento:

1. Buscar el archivo admin.py dentro de la APP creada.
2. Dar los permisos y registrarla. Ver codigo

*Ejemplo de la app de servicios*
```
from django.contrib import admin
from .models import Servicio



# Register your models here.
class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Servicio,ServicioAdmin)
```

### Crear super usuario de Django

Para aprovechar las plantillas de CRUD de Django, es importante crear un super usuario.  

```
python manage.py createsuperuser
```

Definir usuario y password admin

- usuario: lagaguate
- email: lagaguate
. pass: xxxxxxxx


#  Django 4.1
1.  En los modelos puedes aprender como relacionar 2 tablas.  Guiate con la aplicacion de Blog y Tienda.
2.  En los proyecto puedes revisar el archivo forms.py para aprender a crear formularios 
3.  Puedes apreder a configurar imagenes, todo inicia del archivo settings donde dejas configurado que carpeta usas en el proyecto.
