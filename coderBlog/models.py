from django.db import models

# Create your models here.


class Clientes(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    email=models.EmailField()
    
    #class Meta:
        #verbose_name_plural = '  ' # Aqui va el plural d lo q queremos cambiar
        #ordering=['nombre'] #Esto es para oredenar alfabeticamente.Ej:Nombre
    
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
    
class Programadores(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    curso=models.CharField(max_length=20)
    email=models.EmailField()
    
    class Meta:
        verbose_name_plural = "Profesores"
        ordering = ["nombre"]
    
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
    
class Profesores(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    #celular=models.IntegerField()
    
    def __str__(self):
        return f'{self.nombre}, {self.apellido}'
    