from django.db import models
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput 

# Create your models here.

class MyClearableFileInput(ClearableFileInput):
    initial_text = 'currently'
    input_text = 'change'
    clear_checkbox_label = 'clear'

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

# Se crea la clase Meta (Investigar proposito)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        db_table = 'demo_categoria'
        # version 4.2
        #db_table_comment = 'Definicion de servicios'

    def __str__(self):
        return self.nombre    
    

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=50) 
    imagen = models.ImageField(upload_to="blog", null=True)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    
# Se crea la clase Meta (Investigar proposito)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'demo_post'
        # version 4.2
        #db_table_comment = 'Definicion de servicios'

    def __str__(self):
        return self.titulo    
