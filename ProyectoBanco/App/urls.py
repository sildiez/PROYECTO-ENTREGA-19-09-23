from django.urls import path

from App import views

urlpatterns = [
    path('', views.mostrar_index, name='Inicio'),
    path('imagenes/', views.exhibir_imagen, name='Imagenes'),
    path('vectores/', views.exhibir_vector, name='Vectores'),
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
    # Crud 
    path('mostrarimagen/', views.mostrar_imagen, name='mostrarimagen'),
    path('actualizar_imagen/<imagen_id>', views.actualizar_imagen, name='actualizar_imagen'),
    path('eliminar_imagen/<imagen_id>', views.eliminar_imagen, name='eliminar_imagen'),
    path('mostrarvector/', views.mostrar_vector, name='mostrarvector'),
    path('actualizar_vector/<vector_id>', views.actualizar_vector, name='actualizar_vector'),
    path('eliminar_vector/<vector_id>', views.eliminar_vector, name='eliminar_vector'),
    #clases basadas en vistas
    path('video_list/', views.VideoList.as_view(), name='list_v'),
    path('video_detail/<pk>', views.VideoDetailView.as_view(), name='detail_v'),
    path('video_confirm_delete/<pk>', views.VideoDeleteView.as_view(), name='Delete_V'),
    path('video_edit/<pk>', views.VideoUpdateView.as_view(), name='Update_V'),
    path('video_form/', views.VideoCreateView.as_view(), name='Create_V'),
    #
    path('musica_list/', views.MusicaList.as_view(), name='list'),
    path('musica_detail/<pk>', views.MusicaDetailView.as_view(), name='detail'),
    path('musica_confirm_delete/<pk>', views.MusicaDeleteView.as_view(), name='Delete'),
    path('musica_edit/<pk>', views.MusicaUpdateView.as_view(), name='Update'),
    path('musica_form/', views.MusicaCreateView.as_view(), name='Create'),
    #
    #path('musica_form/', views.CreateView.as_view(), name='Create'),
    path('signup/', views.SignUpView.as_view(), name='Sign Up'),
    path('login/', views.AdminLoginView.as_view(), name='Login'),
    path('logout/', views.AdminLogoutView.as_view(), name='Logout'),
    #path('editar_usuario/', views.editar_usuario, name='Editar Usuario'),
    # contacto
    path('contacto/', views.crear_contacto, name='Contacto'),
    # pedido
    path('pedido/', views.crear_pedido, name='Pedido'),
    # acerca
    path('Acerca_nuestro/', views.acerca, name='Acerca'),
]
