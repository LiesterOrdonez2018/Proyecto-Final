from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context,loader

from coderBlog.models import *
from coderBlog.forms import Formulario


# Create your views here.


def clientes(request):
    
    clientes = Clientes()
    clientes.save()
    
    texto = f'Cliente:{clientes.nombre}, {clientes.apellido}, {clientes.email} '
    return render('coderBlog/clientes.html')

def programadores(request):
    programadores = Programadores()
    programadores.save()
     
    texto = 'Programador: {programadores.nombre}, {programadores.apellido}, {programadores.curso} '
    return render('coderBlog/programadores.html')
 
def profesores(request):
      profesores = Profesores()
      profesores.save()
      
      texto = f'Profesor: {profesores.nombre}, {profesores.celular}'
      return render(request,'coderBlog/profesores.html')

def index(request):
    return render(request, 'coderBlog/index.html')
'''
def formulario(request):
    
    if request.method == "POST":
        
        nombre = request.POST.get('clientes')
        nombre = request.POST.get('programadores')
        nombre = request.POST.get('profesores')
        
        clientes = Clientes(nombre=nombre)
        clientes.save()
        programadores = Programadores(nombre=nombre)
        programadores.save()
        profesores = Profesores(nombre=nombre)
        profesores.save()
        
        return render(request, 'index.html')
    
    return render(request, 'formulario.html')
'''

def formulario(request):
    
    if request.method == "POST":
        
        formulario = Formulario(request.POST)  
        
        #print('formulario')
        #print(formulario)
        
        print(f'is valid: {formulario.is_valid}')
        if formulario.is_valid():
            
            datos = formulario.cleaned_data
            
            nombre = datos.get('clientes','programadores','profesores')
            
            nombre = Clientes(nombre= nombre)
            nombre.save()
            
            nombre = Programadores(nombre=nombre)
            nombre.save()
            
            nombre = Profesores(nombre=nombre)
            nombre.save()
            
            return render(request, 'index.html')
    else: 
        formulario = Formulario()        
    return render(request, 'formulario.html', {'formulario': formulario}) 

def busqueda_nombre(request):
    
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        print(f'Vamos a buscar el nombre: {nombre}')
    
    return render(request, 'busqueda_nombre.html')