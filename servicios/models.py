from django.db import models
from django.forms.widgets import ClearableFileInput 

# Create your models here.

class MyClearableFileInput(ClearableFileInput):
    initial_text = 'currently'
    input_text = 'change'
    clear_checkbox_label = 'clear'

class Servicio(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50) 
    imagen = models.ImageField(upload_to="img",help_text="Test Help")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


# Se crea la clase Meta (Investigar proposito)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        db_table = 'demo_servicio'
        # version 4.2
        #db_table_comment = 'Definicion de servicios'

    def __str__(self):
        return self.titulo
