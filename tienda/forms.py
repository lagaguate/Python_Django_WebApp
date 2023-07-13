from django import forms
from tienda.models import Producto, CategoriaProducto 

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, categoria):
        return "%s" % categoria.nombre


class CreateProductForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','categorias','descripcion','imagen', 'precio','disponibilidad']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
        }

    nombre = forms.CharField(required=True)
    categorias = forms.ModelChoiceField(
        queryset=CategoriaProducto.objects.all(),
        to_field_name='nombre',
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":25}))
    precio = forms.FloatField()
    disponibilidad = forms.BooleanField(required=False, widget=forms.CheckboxInput(
                                                        attrs={
                                                                'checked': True
                                                            }
                                                        )
                                        )
    imagen = forms.ImageField()
    

    
    