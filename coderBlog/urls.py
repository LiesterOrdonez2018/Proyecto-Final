from django.urls import path, include
from coderBlog.views import *



urlpatterns = [
    
    
    path('clientes/',clientes, name='clientes'),
    path('programadores/',programadores, name='programadores'),
    path('profesores/',profesores, name='profesores'),
    path('formulario/', formulario, name= 'formulario'),
    path('busquedaNombre/',busqueda_nombre, name='busqueda_nombre'),
    path('leerProfesores/',leer_profesores, name= 'leer_profesores'),
    path('leerClientes/',leer_clientes, name= 'leer_clientes'),
    path('leerProgramadores/',leer_programadores, name= 'leer_programadores'),
    
    path('', index, name='index'),

]
