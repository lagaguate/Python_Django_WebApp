from django.db import models
from django.forms.widgets import ClearableFileInput 


# Create your models here.

class MyClearableFileInput(ClearableFileInput):
    initial_text = 'currently'
    input_text = 'change'
    clear_checkbox_label = 'clear'

class CategoriaProducto(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'categoriaproducto'
        verbose_name_plural = 'categoriaproductos'
        db_table = 'demo_categoriaproducto'
        # version 4.2
        #db_table_comment = 'Se utiliza para poner comentarios'

    def __str__(self):
        return self.nombre    
    

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProducto,on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50) 
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        db_table = 'demo_producto'
        # version 4.2
        #db_table_comment = 'Definicion de servicios'

    def __str__(self):
        return str(self.id) +"-"+self.nombre+"-"+str(self.precio)    
