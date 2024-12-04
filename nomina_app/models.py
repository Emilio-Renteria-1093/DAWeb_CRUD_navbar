from django.db import models

# Create your models here.
class Nomina (models.Model):
    Id_Nomina=models.CharField(primary_key=True,max_length=6)
    Id_Empleado=models.CharField(max_length=6)
    Fecha_Pago=models.DateField()
    Periodo_Pago=models.CharField(max_length=80)
    Descripcion=models.CharField(max_length=300)
    Total=models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.Id_Nomina