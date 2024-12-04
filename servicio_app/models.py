from django.db import models

# Create your models here.
class Servicio (models.Model):
    Id_Servicio=models.CharField(primary_key=True,max_length=6)
    Tipo_Servicio=models.CharField(max_length=20)
    Costo=models.CharField(max_length=20)
    Material=models.CharField(max_length=20)
    Fecha_inicio=models.DateTimeField()
    Fecha_finalizado=models.DateTimeField()
    Resolucion_Problema=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.Id_Servicio