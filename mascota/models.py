from django.db import models


class Estado(models.Model):
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

class Perro(models.Model):
    nombre = models.CharField(max_length=100)
    foto = models.ImageField(default='default.png', blank=True)
    raza = models.CharField(default='Quiltro', max_length=100)
    descripcion = models.TextField()
    #estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=1)
    #dueno = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre


class Rescatados(models.Model):
    fotografia = models.ImageField(upload_to='misPerritos\Fotos')
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    ESTADOS = ((1, "Rescatado"),(2,'Dsiponible'),(3,'Adoptado'),(4,'Seleccionar'))
    estado = models.IntegerField(choices=ESTADOS,default=4)


# Create your models here.
