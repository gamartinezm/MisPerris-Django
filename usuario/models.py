from django.db import models

# Create your models here.


class Persona(models.Model):
	nombre = models.CharField(max_length=50)
	apellidos = models.CharField(max_length=50)
	edad = models.IntegerField()
	telefono = models.CharField(max_length=50)
	email = models.EmailField()
	domicilio = models.TextField()