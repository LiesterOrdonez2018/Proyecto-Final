from django import forms


#class Formulario(forms.Form):

class Clientes(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido =  forms.CharField(max_length=20)
    
class Programadores(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido =  forms.CharField(max_length=20)
    
class Profesores(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido =  forms.CharField(max_length=20)
