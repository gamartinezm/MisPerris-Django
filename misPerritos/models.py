from django.db import models

class RescatadosPost(models.Model):
    fotografia = models.ImageField(upload_to='misPerritos\Fotos')
    nombre = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=300)
    ESTADOS = ((1, "Rescatado"),(2,'Dsiponible'),(3,'Adoptado'),(4,'Seleccionar'))
    estado = models.IntegerField(choices=ESTADOS,default=4)


# Create your models here.
