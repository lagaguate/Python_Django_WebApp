## Crear Proyecto 

django-admin startproject AplicacionWeb


## Crear aplicacion
- En linux asi:
python3 manage.py start app ProyectoWebApp

## Test Proyecto WEB
python3 manage.py runserver

## Registrar la aplicacion en el proyecto
1. A nivel de aplicacion, buscar el archivo settings.py
2. En la seccion de INSTALLED_APPS registrar la aplicacion.

## Crear la APP Servicios
python3 manage.py startapp servicios

## Migracion de Models
python3 manage.py makemigrations

## Luego de hacer makemigrations, se debe migrar
python3 manage.py migrate

## Siguiente paso registrar la APP Servicios
1. Crear Super usuario de Django
```sh
python manage.py createsuperuser
```
- usuario: lagaguate
- email: lagaguate
. pass: hunter1972


## dentro de la APP Servicio, buscar el archivo admin.py
## importar servicios
1. from .models import Servicio
## registrar servicio dentro de admin
2. admin.site.register(Servicio)
