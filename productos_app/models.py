from django.db import models

# Create your models here.
class Producto (models.Model):
    Id_Producto=models.CharField(primary_key=True,max_length=6)
    Cantidad_P=models.CharField(max_length=200)
    Tipo_Producto=models.CharField(max_length=300)
    Costo=models.CharField(max_length=10000)
    Fecha_Ingreso=models.DateField()
    Id_Proveedor=models.CharField(max_length=6)

    def __str__(self) -> str:
        return self.Id_Producto