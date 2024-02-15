from django import forms


#class Formulario(forms.Form):

class ClientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido =  forms.CharField(max_length=20)
    
class ProgramadoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido =  forms.CharField(max_length=20)
    
class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido =  forms.CharField(max_length=20)
