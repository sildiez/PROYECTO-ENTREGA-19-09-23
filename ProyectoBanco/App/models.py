from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Imagen(models.Model):
    numero= models.IntegerField()
    tamaño= models.CharField(max_length=20)
    resolucion= models.IntegerField()
    categoria= models.CharField(max_length=15)
    orientacion = models.CharField(max_length=10)
    tipo = models.CharField(max_length=5)

    def __str__(self):
        return f'Articulo: {self.numero}, Dimension: {self.tamaño} pixeles, en: {self.resolucion} DPI, Categoria: {self.categoria}, Posicion: {self.orientacion}, en modo: {self.tipo}'

class Vector(models.Model):
    numero= models.IntegerField()
    categoria= models.CharField(max_length=15)
    orientacion = models.CharField(max_length=10)
    tipo = models.CharField(max_length=5)

    def __str__(self):
        return f'Articulo: {self.numero}, Categoria: {self.categoria}, Posicion: {self.orientacion}, en modo: {self.tipo}'


class Video(models.Model):
    numero= models.IntegerField()
    tamaño= models.CharField(max_length=20)
    resolucion= models.IntegerField()
    categoria= models.CharField(max_length=15)
    orientacion = models.CharField(max_length=10)

    def __str__(self):
        return f'Articulo: {self.numero}, Dimension: {self.tamaño} pixeles, en: {self.resolucion} DPI, Categoria: {self.categoria}, Posicion: {self.orientacion}'
        
class Musica(models.Model):
    numero= models.IntegerField()
    duracion= models.CharField(max_length=5)
    calidad= models.CharField(max_length=10)
    categoria= models.CharField(max_length=15)

    def __str__(self):
        return f'Articulo: {self.numero}, Duracion: {self.duracion} minutos, en: {self.calidad}, Categoria: {self.categoria}'
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

class Contacto(models.Model):
    nombre = models.CharField(max_length=5)
    apellido = models.CharField(max_length=5)
    email = models.EmailField(max_length=16)
    mensaje = models.TextField(max_length=350)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Mensaje: {self.mensaje}'

class Pedido(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    telefono = models.IntegerField()
    tipo_de_archivo = models.CharField(max_length=8)
    articulo = models.IntegerField()
    metodo_de_pago = models.CharField(max_length=7)    

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, Email: {self.email}, Telefono: {self.telefono}, Tipo de Archivo: {self.tipo_de_archivo}, Articulo: {self.articulo}, Metodo de Pago: {self.metodo_de_pago}'
