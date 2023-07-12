from django import forms
from tienda.models import Producto, CategoriaProducto 

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, categoria):
        return "%s" % categoria.nombre


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'categorias','descripcion','imagen', 'precio','disponibilidad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

   
    nombre = forms.CharField(required=True)
    categorias = CustomMMCF(
        queryset=CategoriaProducto.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}))
    precio = forms.FloatField()
    disponibilidad = forms.BooleanField()
    imagen = forms.ImageField()
    

    
    