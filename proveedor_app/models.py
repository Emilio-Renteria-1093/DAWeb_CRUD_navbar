from django.db import models

# Create your models here.
class Proveedor (models.Model):
    Id_Proveedor=models.CharField(primary_key=True,max_length=6)
    Nombre=models.CharField(max_length=50)
    Apellido=models.CharField(max_length=50)
    Direccion=models.CharField(max_length=300)
    Ruta=models.CharField(max_length=300)
    Sucursales=models.CharField(max_length=3)
    Num_Tel=models.CharField(max_length=10)
    Metodo_Trans=models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.Id_Proveedor