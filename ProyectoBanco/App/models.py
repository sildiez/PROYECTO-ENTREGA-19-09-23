from django.db import models

# Create your models here.

class Imagen(models.Model):
    numero= models.IntegerField()
    tamaño= models.CharField(max_length=20)
    resolucion= models.IntegerField()
    categoria= models.CharField(max_length=15)
    orientacion = models.CharField(max_length=10)
    tipo = models.CharField(max_length=5)

    def __str__(self):
        return f'Articulo: {self.numero}, Dimension: {self.tamaño} pixeles, en:{self.resolucion} DPI, Categoria: {self.categoria}, Posicion: {self.orientacion}, en modo: {self.tipo}'

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
        return f'Articulo: {self.numero}, Dimension: {self.tamaño} pixeles, en:{self.resolucion} DPI, Categoria: {self.categoria}, Posicion: {self.orientacion}'
        
class Musica(models.Model):
    numero= models.IntegerField()
    duracion= models.CharField(max_length=5)
    calidad= models.CharField(max_length=10)
    categoria= models.CharField(max_length=15)

    def __str__(self):
        return f'Articulo: {self.numero}, Duracion: {self.duracion} minutos, en:{self.calidad}, Categoria: {self.categoria}'