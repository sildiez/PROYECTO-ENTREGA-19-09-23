from django.shortcuts import render

# Create your views here.

from App.models import Imagen
from App.models import Vector
from App.models import Video
from App.models import Musica
from App.models import Avatar
from App.models import Contacto
from App.models import Pedido


from .forms import Crear_Imagen_Form, Crear_Video_Form, Crear_Vector_Form, Crear_Musica_Form, SignUpForm, Crear_Contacto_Form, Crear_Pedido_Form
#UserEdithForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def exhibir_imagen(request):

    i1 = Imagen(numero= 1001, tamaño= '1920x1080', resolucion= 300, categoria= 'fauna', orientacion= 'horizontal', tipo = 'CMYK')
    i2 = Imagen(numero= 1002, tamaño= '1920x1080', resolucion= 300, categoria= 'flora', orientacion= 'vertical', tipo = 'CMYK')
    i3 = Imagen(numero= 1003, tamaño= '1920x1080', resolucion= 150, categoria= 'paisaje', orientacion= 'horizontal', tipo = 'RGB')
    i4 = Imagen(numero= 1004, tamaño= '1920x1080', resolucion= 150, categoria= 'astro', orientacion= 'horizontal', tipo = 'CMYK')

    return render(request, 'App/imagen.html', {'imagenes': [i1, i2, i3, i4]})

def mostrar_imagen(request):
    imagenes = Imagen.objects.all()
    context = {'imagenes': imagenes}

    return render(request, 'App/mostrarimagen.html', context = context)

def eliminar_imagen(request, imagen_id):
    imagen = Imagen.objects.get(id=imagen_id)
    imagen.delete()

    imagen = Imagen.objects.all()
    context = {'imagenes': imagen}

    return render(request, 'App/mostrarimagen.html', context = context)

def actualizar_imagen(request, imagen_id):
    imagenes = Imagen.objects.get(id=imagen_id)

    if request.method == 'POST':
        
        miformulario = Crear_Imagen_Form(request.POST)
        if miformulario.is_valid():
            formulario_limpio = miformulario.cleaned_data

            imagenes.numero = formulario_limpio ['numero']
            imagenes.tamaño = formulario_limpio ['tamaño']
            imagenes.resolucion = formulario_limpio ['resolucion']
            imagenes.categoria = formulario_limpio ['categoria']
            imagenes.orientacion = formulario_limpio ['orientacion']
            imagenes.tipo = formulario_limpio ['tipo']

            imagenes.save()

            return render(request, 'App/home.html')
    else:
        miformulario = Crear_Imagen_Form(initial={'numero': imagenes.numero, 'tamaño': imagenes.tamaño, 'resolucion': imagenes.resolucion, 'categoria': imagenes.categoria, 'orientacion': imagenes.orientacion, 'tipo': imagenes.tipo})

    return render (request, 'App/actualizar_imagen.html', {'miformulario' : Crear_Imagen_Form, 'imagenes' : imagenes})


def exhibir_vector(request):

    v1 = Vector(numero= 101, categoria= 'fiesta', orientacion= 'horizontal', tipo = 'RGB')
    v2 = Vector(numero= 102, categoria= 'flora', orientacion= 'horizontal', tipo = 'RGB')
    v3 = Vector(numero= 103, categoria= 'geometria', orientacion= 'vertical', tipo = 'CMYK')
    v4 = Vector(numero= 104, categoria= 'comida', orientacion= 'vertical', tipo = 'CMYK')

    return render(request, 'App/vectores.html', {'vectores': [v1, v2, v3, v4]})

def mostrar_vector(request):
    vectores = Vector.objects.all()
    context = {'vectores': vectores}
    return render(request, 'App/mostrarvector.html', context = context)

def eliminar_vector(request, vector_id):
    vector = Vector.objects.get(id=vector_id)
    vector.delete()

    vector = Vector.objects.all()
    context = {'vectores': vector}
    return render(request, 'App/mostrarvector.html', context=context)

def actualizar_vector(request, vector_id):
    vectores = Vector.objects.get(id=vector_id)

    if request.method == 'POST':
        
        miformulario = Crear_Vector_Form(request.POST)
        if miformulario.is_valid():
            formulario_limpio = miformulario.cleaned_data

            vectores.numero = formulario_limpio ['numero']
            vectores.categoria = formulario_limpio ['categoria']
            vectores.orientacion = formulario_limpio ['orientacion']
            vectores.tipo = formulario_limpio ['tipo']

            vectores.save()

            return render(request, 'App/home.html')
    else:
        miformulario = Crear_Vector_Form(initial={'numero': vectores.numero, 'categoria': vectores.categoria, 'orientacion': vectores.orientacion, 'tipo': vectores.tipo})

    return render (request, 'App/actualizar_vector.html', {'miformulario' : Crear_Vector_Form, 'vectores' : vectores})


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
    if request.user.is_authenticated:
        context = {'Avatar': Avatar.objects.get(user = request.user.id).imagen.url}

    else:
        context = {}

    return render(request, 'App/home.html', context)

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


#Clases basadas en vistas
from django.views.generic import ListView
class VideoList(LoginRequiredMixin, ListView):

    model = Video
    template_name = 'App/video_list.html'

from django.views.generic.detail import DetailView
class VideoDetailView(DetailView):

    model = Video
    template_name = 'App/video_detalle.html'

from django.views.generic.edit import CreateView, UpdateView, DeleteView
class VideoCreateView(LoginRequiredMixin, CreateView):

    model = Video
    success_url = '/video_list'
    fields = ['numero', 'tamaño', 'resolucion', 'categoria', 'orientacion']
class VideoUpdateView(UpdateView):

    model = Video
    success_url = '/video_list'
    fields = ['numero', 'tamaño', 'resolucion', 'categoria', 'orientacion']
class VideoDeleteView(DeleteView):

    model = Video
    success_url = '/video_list'

###
class MusicaList(LoginRequiredMixin, ListView):

    model = Musica
    template_name = 'App/musica_list.html'
class MusicaDetailView(DetailView):

    model = Musica
    template_name = 'App/musica_detalle.html'
class MusicaCreateView(LoginRequiredMixin, CreateView):

    model = Musica
    success_url = '/musica_list'
    fields = ['numero', 'duracion', 'calidad', 'categoria']
class MusicaUpdateView(UpdateView):

    model = Musica
    success_url = '/musica_list'
    fields = ['numero', 'duracion', 'calidad', 'categoria']
class MusicaDeleteView(DeleteView):

    model = Musica
    success_url = '/musica_list'

# Usuario
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('Inicio')
    template_name = 'App/registro.html'

class AdminLoginView(LoginView):
    template_name = 'App/login.html'

class AdminLogoutView(LogoutView):
    template_name = 'App/logout.html'

class AdminUpdateView(UpdateView):
    model = Musica
    success_url = '/musica_list'
    fields = ['numero', 'duracion', 'calidad', 'categoria']

# contacto

def crear_contacto(request):
    if request.method == 'POST':

        miformulario = Crear_Contacto_Form (request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data
        
            contacto = Contacto ( nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], mensaje=informacion['mensaje'])

            contacto.save()

            return render(request, 'App/home.html')
        
    else:

        miformulario = Crear_Contacto_Form()

    return render(request, 'App/contactoFormulario.html', {'miformulario': Crear_Contacto_Form})

# pedido

def crear_pedido(request):
    if request.method == 'POST':

        miformulario = Crear_Pedido_Form (request.POST)

        if miformulario.is_valid():

            informacion = miformulario.cleaned_data
        
            pedido = Pedido ( nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], telefono=informacion['telefono'], tipo_de_archivo=informacion['tipo_de_archivo'], articulo=informacion['articulo'], metodo_de_pago=informacion['metodo_de_pago'])

            pedido.save()

            return render(request, 'App/home.html')
        
    else:

        miformulario = Crear_Pedido_Form()

    return render(request, 'App/pedidoFormulario.html', {'miformulario': Crear_Pedido_Form})

# Acerca
def acerca(request):
    return render(request, 'App/acerca.html')


# Registro
"""def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render ('App/home.html', {"mensaje":"usuario creado"})
    else:
            form = UserCreationForm()

    return render(request, 'App/registro.html', {"form": form})"""
