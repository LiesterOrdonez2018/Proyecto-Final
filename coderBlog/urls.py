from django.urls import path, include
from coderBlog.views import clientes,programadores,profesores, index,formulario,busqueda_nombre



urlpatterns = [
    
    
    path('cliente/',clientes, name='clientes'),
    path('programador/',programadores, name='programadores'),
    path('profesor/',profesores, name='profesores'),
    path('formulario/', formulario, name= 'formulario'),
    path('busquedaNombre/',busqueda_nombre, name='busqueda_nombre'),
    
    path('', index, name='index'),

]
