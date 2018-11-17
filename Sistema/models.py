from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Region(models.Model):
	codigoRegion = models.CharField(primary_key = True, max_length = 5)
	nombreRegion = models.CharField(max_length = 50)

	def __str__(self):
		return self.nombreRegion

class Ciudad(models.Model):
	codigoCiudad = models.CharField(primary_key = True, max_length = 15)
	nombreCiudad = models.CharField(max_length = 30)
	region = models.ForeignKey(Region, on_delete = models.DO_NOTHING)

	def __str__(self):
		return self.nombreCiudad

class Adoptante(models.Model):
	codigoAdoptante = models.AutoField(primary_key = True)
	usuario = models.OneToOneField(User, unique = True, on_delete = models.CASCADE)
	run = models.CharField(unique = True, max_length = 10)
	nombres = models.CharField(max_length = 20)
	apPaterno = models.CharField(max_length = 20)
	apMaterno = models.CharField(max_length = 20)
	fechaNacimiento = models.DateField()
	telefono = models.IntegerField(null = True)
	ciudad = models.ForeignKey(Ciudad, on_delete = models.DO_NOTHING)
	tipoVivienda = models.CharField(max_length = 30)

class Mascota(models.Model):
	codigoMascota = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 20)
	raza = models.CharField(max_length = 20)
	descripcion = models.TextField()
	estado = models.CharField(max_length = 10)
	foto = models.ImageField(upload_to = "mascotas", blank = True, null = True)
	adoptante = models.ForeignKey(Adoptante, on_delete = models.DO_NOTHING, null = True)

class Mensaje(models.Model):
	codigoMensaje = models.AutoField(primary_key = True)
	nombre = models.CharField(max_length = 30)
	correo = models.EmailField(max_length = 30)
	mensaje = models.TextField()
