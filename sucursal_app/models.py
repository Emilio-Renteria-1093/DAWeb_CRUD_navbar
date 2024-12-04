from django.db import models

# Create your models here.
class Sucursal (models.Model):
    Id_Sucursal=models.CharField(primary_key=True,max_length=6)
    Locolizacion=models.CharField(max_length=200)
    Num_Empleados=models.CharField(max_length=2)
    Ganancias=models.CharField(max_length=10000)
    Telefono=models.CharField(max_length=10)
    Email=models.CharField(max_length=80)
    Encargado=models.CharField(max_length=20)


    def __str__(self) -> str:
        return self.Id_Sucursal