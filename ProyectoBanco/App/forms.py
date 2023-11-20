from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Crear_Imagen_Form(forms.Form):
    numero= forms.IntegerField()
    tamaño= forms.CharField(min_length=3, max_length=20)
    resolucion= forms.IntegerField()
    categoria= forms.CharField(min_length=3, max_length=15)
    orientacion = forms.CharField(min_length=3, max_length=10)
    tipo = forms.CharField(min_length=3, max_length=5)


class Crear_Video_Form(forms.Form):
    numero = forms.IntegerField()
    tamaño = forms.CharField(min_length=3, max_length=20)
    resolucion = forms.IntegerField()
    categoria = forms.CharField(min_length=3, max_length=15)
    orientacion = forms.CharField(min_length=3, max_length=10)


class Crear_Vector_Form(forms.Form):
    numero= forms.IntegerField()
    categoria= forms.CharField(min_length=3, max_length=15)
    orientacion = forms.CharField(min_length=3, max_length=10)
    tipo = forms.CharField(min_length=3, max_length=5)


class Crear_Musica_Form(forms.Form):
    numero= forms.IntegerField()
    duracion= forms.CharField(min_length=3, max_length=5)
    calidad= forms.CharField(min_length=3, max_length=10)
    categoria= forms.CharField(min_length=3, max_length=15)

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class UserEditForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
        help_texts = {k: '' for k in fields}
        
class Crear_Contacto_Form(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=25)
    apellido = forms.CharField(min_length=3, max_length=15)
    email = forms.EmailField(min_length=8, max_length=50)
    mensaje = forms.CharField(min_length=3, max_length=500)

class Crear_Pedido_Form(forms.Form):
    nombre = forms.CharField(min_length=3, max_length=25)
    apellido = forms.CharField(min_length=3, max_length=15)
    email = forms.EmailField(min_length=8, max_length=50)
    telefono = forms.IntegerField()
    tipo_de_archivo = forms.CharField(min_length=6,max_length=8)
    articulo = forms.IntegerField()
    metodo_de_pago = forms.CharField(min_length=6, max_length=7)



