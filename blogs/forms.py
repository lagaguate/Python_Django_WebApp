from django import forms
from blogs.models import Categoria, Post
from django.contrib.auth.models import User


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, categoria):
        return "%s" % categoria.nombre


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido', 'imagen', 'autor', 'categorias']
    titulo = forms.CharField()
    contenido = forms.CharField()
    
    autor = forms.ModelChoiceField(
        queryset=User.objects.all(),
        to_field_name='username',
        required=True,  
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    imagen = forms.ImageField()

    # categorias = forms.ModelMultipleChoiceField(
    #    queryset=Categoria.objects.all(),
    #    widget=forms.CheckboxSelectMultiple)

    categorias = CustomMMCF(
        queryset=Categoria.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
