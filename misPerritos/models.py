from django.db import models

class Estado(models.Model):
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='Fotos')
    raza = models.CharField(max_length=100)
    descripcion = models.TextField()
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre


# Create your models here.
