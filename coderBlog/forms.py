from django import forms


class Formulario(forms.Form):
    clientes= forms.CharField(max_length=20)
    programadores= forms.CharField(max_length=20)
    profesores=forms.CharField(max_length=20)
