from django.db import models

# Create your models here.

class Cliente(models.Model):
    correo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()

class Tecnico(models.Model):
    rut = models.CharField(max_length=12)
    correo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()

class Solicitud(models.Model):
    nombre = models.CharField(max_length=100) 
    email = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

class Producto(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    precio = models.IntegerField()
