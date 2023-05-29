from django.db import models

# Create your models here.

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50)
    imagen = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

# Se crea la clase Meta (Investigar proposito)    
    class Meta: 
        verbose_name='servicio'
        verbose_name_plural='servicios'
        db_table = 'dj_servicio'
        # version 4.2
        #db_table_comment = 'Definicion de servicios'

    def __str__(self):
        return self.titulo
    
