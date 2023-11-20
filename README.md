# DIEZ SILVANA GABRIELA -FINAL-PYTHON
# ProyectoFinalSilvanaGabrielaDiezPython
Proyecto Final Silvana Gabriela Diez curso Python en Centro de Formacion 406
se desarrrollo un microservicios con una aplicación web estilo banco de imágenes y recursos audiovisuales para profesionales y el blog correspondiente a la misma, programada en Python en Django. Esta web tendrá admin, perfiles, registro de usuarios, páginas y formularios.

Este proyecto no utiliza Python puro sino Python con Django para desarrollo web. Y la magia de HTML5 Y CSS3 combinado de las plantillas de Bootstrap nos facilitan
el diseño FrontEnd de este proyecto.


# Comenzando🚀
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu local para propósitos de desarrollo y pruebas.

git clone https://github.com/sildiez/ProyectoBancoEntregaFinal2023.git

# Descarga de instalación ZIP
Ir a “code” > download ZIP
Descomprimir el archivo
y luego elegir en que carpeta de tu equipo lo instalas y lurgo se abre con  VS CODE


# Pre-requisitos📋
Deberas tener instalado para correr este proyecto:

Visual Studio Code, Python 3.10 o superior, Django, DB SQLITE Browser


# instalacion🔧
Se instala en primer instancia VS Code se descarga de https://code.visualstudio.com/download 
se elige el sistema operativo que usas Windows, Mac o Linux se descarga y se siguen los pasos que nos indica hasta instalar VS CODE.

Luego se instala Python 3.10 se descarga de https://www.python.org/  en la primer pantalla selecionar la caja de path sera de utilidad para este proyecto y
luego seguir con la instalacion del mismo.

 Descargue de aqui  DB SQLITE https://www.sqlite.org/index.html y siga los pasos.



# construido con🛠️
 VS CODE
 PYTHON 3.10
 DB SQLITE BROWSER
 Django
 HTML 5
 CSS
 BOOTSTRAPP

# Comandos usados en la consola de VS CODE para hacer funcionar el proyecto
python -m venv entorno (creamos el entorno virtual)

.\entorno\Scripts\activate (activación del entorno virtual)

django-admin startproject Proyecto (crea el proyecto)

cd .\ProyectoEntrega\   (nos posiciona en la carpeta del proyecto)

python manage.py startapp MiApp (crea la app)

python manage.py makemigrations (hace los cambios en la base de datos y los modelos)

python manage.py migrate (Guarda los cambios de los modelos)

python manage.py runserver (activa el sitio web en localhost)

# Gestionando mi app

python manage.py startapp 

Creamos nuestro modelo dentro de models.py

En nuestro views.py, definimos la vista para mostrar nuestro modelo, importamos nuestro modelos!!

Creamos nuestra plantilla .html con las líneas de código necesarias para mostrar la información de nuestros modelos.

Creamos nuestro archivo urls.py (dentro de la app), creamos la url para la vista deseada, importamos nuestra vista!!

En nuestro archivo settings.py incluimos la app creada en INSTALLED_APPS, agregamos la dirección de la carpeta de nuestros templates en la sección DIRS, de templates. 
Listo!

## Créditos
Gracias a todos los que apoyaron la iniciativa del proyecto y a los que brindaron información y ayuda en los momentos de complicaciones y contratiempos. 
Mi agradecimiento al Centro de formación 406 de Morón, por la posibilidad de incorporar nuevos conocimientos y por los momentos compartidos, al [Profesor] Ignacio Giordano, y a los compañeros que siempre estuvieron ahí y me dieron el aliento para no decaer cuando era necesario, además a los amigos que incitaron para continuar en el camino de la programación con python/django. 
Por ultimo y casi diría lo importante a mí, por este grandisimo esfuerzo, en este año tan difícil que me ha tocado superar, y a mi Familia que me acompañó en este transcurso, mil gracias.

# Autor✒️
SILVANA GABRIELA DIEZ

