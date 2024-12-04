from django.db import models

# Create your models here.
class Venta (models.Model):
    Id_Venta=models.CharField(primary_key=True,max_length=6)
    Id_Nomina=models.CharField(max_length=6)
    Fecha_Venta=models.DateField()
    Id_Empleado=models.CharField(max_length=6)
    Total=models.CharField(max_length=10000)
    Producto_Vendido=models.CharField(max_length=80)
    Cant_Productos=models.CharField(max_length=100)
    Id_Producto=models.CharField(max_length=6)
    Id_Sucursal=models.CharField(max_length=6)
    Id_Proveedor=models.CharField(max_length=6)



    def __str__(self) -> str:
        return self.Id_Venta