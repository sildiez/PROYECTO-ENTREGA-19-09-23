from django.shortcuts import render

# Create your views here.

from App.models import Imagen
from App.models import Vector
from App.models import Video
from App.models import Musica


from .forms import Crear_Imagen_Form, Crear_Video_Form, Crear_Vector_Form, Crear_Musica_Form

def mostrar_imagen(request):

    i1 = Imagen(numero= 1001, tamaño= '1920x1080', resolucion= 300, categoria= 'fauna', orientacion= 'horizontal', tipo = 'CMYK')
    i2 = Imagen(numero= 1002, tamaño= '1920x1080', resolucion= 300, categoria= 'flora', orientacion= 'vertical', tipo = 'CMYK')
    i3 = Imagen(numero= 1003, tamaño= '1920x1080', resolucion= 150, categoria= 'paisaje', orientacion= 'horizontal', tipo = 'RGB')
    i4 = Imagen(numero= 1004, tamaño= '1920x1080', resolucion= 150, categoria= 'astro', orientacion= 'horizontal', tipo = 'CMYK')

    return render(request, 'App/imagen.html', {'imagenes': [i1, i2, i3, i4]})

def mostrar_vector(request):

    v1 = Vector(numero= 101, categoria= 'fiesta', orientacion= 'horizontal', tipo = 'RGB')
    v2 = Vector(numero= 102, categoria= 'flora', orientacion= 'horizontal', tipo = 'RGB')
    v3 = Vector(numero= 103, categoria= 'geometria', orientacion= 'vertical', tipo = 'CMYK')
    v4 = Vector(numero= 104, categoria= 'comida', orientacion= 'vertical', tipo = 'CMYK')

    return render(request, 'App/vectores.html', {'vectores': [v1, v2, v3, v4]})

def mostrar_video(request):

    vi1 = Video(numero= 10001, tamaño= '3840x2160', resolucion= 96, categoria= 'fauna', orientacion= 'horizontal')
    vi2 = Video(numero= 10002, tamaño= '1920x1080', resolucion= 300, categoria= 'abstrato', orientacion= 'horizontal')
    vi3 = Video(numero= 10003, tamaño= '1280x720', resolucion= 150, categoria= 'abstrato', orientacion= 'horizontal')
    vi4 = Video(numero= 10004, tamaño= '1280x720', resolucion= 96, categoria= 'recital', orientacion= 'horizontal')

    return render(request, 'App/videos.html', {'videos': [vi1, vi2, vi3, vi4]})

def mostrar_musica(request):

    m1 = Musica(numero= 1, duracion= '3:46', calidad= 'alta', categoria= 'rock')
    m2 = Musica(numero= 2, duracion= '5:46', calidad= 'baja', categoria= 'rock')
    m3 = Musica(numero= 3, duracion= '2:06', calidad= 'alta', categoria= 'pop')
    m4 = Musica(numero= 4, duracion= '3:00', calidad= 'media', categoria= 'rock')

    return render(request, 'App/musica.html', {'musica': [m1, m2, m3, m4]})

def mostrar_index(request):


    return render(request, 'App/home.html')

def crear_imagenes(request):
    if request.method == 'POST':

        miformulario = Crear_Imagen_Form (request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data
        
            imagen = Imagen ( numero=informacion['numero'], tamaño=informacion['tamaño'], resolucion=informacion['resolucion'], categoria=informacion['categoria'], orientacion=informacion['orientacion'], tipo=informacion['tipo'])

            imagen.save()

            return render(request, 'App/home.html')
        
    else:

        miformulario = Crear_Imagen_Form()

    return render(request, 'App/imagenesFormulario.html', {'miformulario': Crear_Imagen_Form})


def crear_videos(request):
    if request.method == 'POST':

        miformulario = Crear_Video_Form (request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data
        
            video = Video ( numero=informacion['numero'], tamaño=informacion['tamaño'], resolucion=informacion['resolucion'], categoria=informacion['categoria'], orientacion=informacion['orientacion'])

            video.save()

            return render(request, 'App/home.html')
        
    else:

        miformulario = Crear_Video_Form()

    return render(request, 'App/videosFormulario.html', {'miformulario': Crear_Video_Form})


def crear_vectores(request):
    if request.method == 'POST':

        miformulario = Crear_Vector_Form (request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data
        
            vector = Vector ( numero=informacion['numero'], categoria=informacion['categoria'], orientacion=informacion['orientacion'], tipo=informacion['tipo'])

            vector.save()

            return render(request, 'App/home.html')
        
    else:

        miformulario = Crear_Vector_Form()

    return render(request, 'App/vectoresFormulario.html', {'miformulario': Crear_Vector_Form})


def crear_musica(request):
    if request.method == 'POST':

        miformulario = Crear_Musica_Form (request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data
        
            musica = Musica ( numero=informacion['numero'], duracion=informacion['duracion'], calidad=informacion['calidad'], categoria=informacion['categoria'])

            musica.save()

            return render(request, 'App/home.html')
        
    else:

        miformulario = Crear_Musica_Form()

    return render(request, 'App/musicaFormulario.html', {'miformulario': Crear_Musica_Form})


def buscar_numero_imagen(request):
    
    if request.GET.get('numero', False):
        numero = request.GET['numero']
        imagen = Imagen.objects.filter(numero__icontains=numero)

        return render(request, 'App/buscar_numero_imagen.html', {'imagen' : imagen})
    else:
        respuesta = 'No hay datos'
    return render(request, 'App/buscar_numero_imagen.html', {'respuesta' : respuesta})


def buscar_numero_video(request):

    if request.GET.get('numero', False):
        numero = request.GET['numero']
        video = Video.objects.filter(numero__icontains=numero)

        return render(request, 'App/buscar_numero_video.html', {'video' : video})
    else:
        respuesta = 'No hay un video para mostrar'
    return render(request, 'App/buscar_numero_video.html', {'respuesta' : respuesta})
    

def buscar_numero_vector(request):

    if request.GET.get('numero', False):
        numero = request.GET['numero']
        vector = Vector.objects.filter(numero__icontains=numero)

        return render(request, 'App/buscar_numero_vector.html', {'vector': vector})
    else:
        respuesta = 'No hay datos para mostrar'
    return render(request, 'App/buscar_numero_vector.html', {'respuesta': respuesta})


def buscar_numero_musica(request):

    if request.GET.get('numero', False):
        numero = request.GET['numero']
        musica = Musica.objects.filter(numero__icontains=numero)

        return render(request, 'App/buscar_numero_musica.html', {'musica' : musica})
    else:
        respuesta = 'No hay musica para mostrar'
    return render(request, 'App/buscar_numero_musica.html', {'respuesta' : respuesta})



