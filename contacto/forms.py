from django import forms
from contacto.models import Contacto
from django.contrib.auth.models import User


class CreateContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['firstname', 'lastname','email','imagen', 'contenido']
        widgets = {
            'contenido': forms.Textarea(attrs={'rows': 3}),
        }

    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    email = forms.EmailField(required=True,help_text="A valid email address, please.",error_messages={"required": "Please enter your name"})
    imagen = forms.ImageField()
    contenido = forms.CharField(widget=forms.Textarea(attrs={"rows":3, "cols":20}))

    