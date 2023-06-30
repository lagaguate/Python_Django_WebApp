from django.db import models

# Create your models here.
class Contacto(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50) 
    email = models.CharField(max_length=50) 
    imagen = models.ImageField(upload_to="img",help_text="Test Help")
    contenido = models.CharField(max_length=2000,null=True) 
    created = models.DateTimeField(auto_now_add=True )
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
        db_table = 'demo_contacto'
        # version 4.2
        #db_table_comment = 'Definicion de servicios'

    def __str__(self):
        return self.firstname