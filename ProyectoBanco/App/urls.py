from django.urls import path

from App import views

urlpatterns = [
    path('', views.mostrar_index, name='Inicio'),
    path('imagenes/', views.mostrar_imagen, name='Imagenes'),
    path('vectores/', views.mostrar_vector, name='Vectores'),
    path('videos/', views.mostrar_video, name='Videos'),
    path('musica/', views.mostrar_musica, name='Musica'),
    path('imagenesFormulario/', views.crear_imagenes, name='ImagenesFormulario'),
    path('videosFormulario/', views.crear_videos, name='VideosFormulario'),
    path('vectoresFormulario/', views.crear_vectores, name='VectoresFormulario'),
    path('musicaFormulario/', views.crear_musica, name='MusicaFormulario'),
    path('buscar_numero_imagen/', views.buscar_numero_imagen, name='buscar_numero_imagen'),
    path('buscar_numero_video/', views.buscar_numero_video, name='buscar_numero_video'),
    path('buscar_numero_vector/', views.buscar_numero_vector, name='buscar_numero_vector'),
    path('buscar_numero_musica/', views.buscar_numero_musica, name='buscar_numero_musica'),
]
