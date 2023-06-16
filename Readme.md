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

## Crear la APP Servicios & makemigrations
python3 manage.py startapp servicios
python3 manage.py makemigrations servicios
python3 manage.py migrate servicios

## Crear la APP Blog & makemigrations
python3 manage.py startapp blogs
python3 manage.py makemigrations blogs
python3 manage.py migrate blogs

1. Ir al archivo admin del proyecto blog y llamar el modelo
## Crear la APP Contactos
python3 manage.py startapp contacto

## Migracion de Models Blogs
python3 manage.py makemigrations

## Crear la APP Tienda
python3 manage.py startapp tienda

## Luego de hacer makemigrations, se debe migrar
python3 manage.py migrate

## Siguiente paso registrar la APP Servicios
1. Crear Super usuario de Django para ingresar datos en ADMIN
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
