from django import forms

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


