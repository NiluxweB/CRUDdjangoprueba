from django.db import models

# Create your models here.

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateTimeField()
    """ genero = models.ForeignKey(Genero, on_delete=models.CASCADE) """
    genero = models.CharField(max_length=100)
    



        