from django.db import models

# Create your models here.
class Empleados (models.Model):
    Id_Empleado=models.CharField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=100)
    Apellido=models.CharField(max_length=100)
    Sexo=models.CharField(max_length=20)
    Direccion=models.CharField(max_length=180)
    Num_Tel=models.CharField(max_length=10)
    Email=models.CharField(max_length=180)
    Nomina=models.CharField(max_length=10000)

    def __str__(self) -> str:
        return self.Id_Empleado