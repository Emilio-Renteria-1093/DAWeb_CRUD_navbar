from django.shortcuts import render,redirect
from .models import Proveedor
# Create your views here.
def inicio_vista(request):
    ListadoProveedores=Proveedor.objects.all()
    return render(request,'gestionarProveedor.html',{'listaProveedores':ListadoProveedores})

def registrarProveedor(request):
    Id_Proveedor=request.POST["txtId_Proveedor"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    Direccion=request.POST["txtDireccion"]
    Ruta=request.POST["txtRuta"]
    Sucursales=request.POST["txtSucursales"]
    Num_Tel=request.POST["txtNum_Tel"]
    Metodo_Trans=request.POST["txtMetodo_Trans"]


    guardarProveedores=Proveedor.objects.create(Id_Proveedor=Id_Proveedor,Nombre=Nombre,Apellido=Apellido,Direccion=Direccion,Ruta=Ruta,Sucursales=Sucursales,Num_Tel=Num_Tel,Metodo_Trans=Metodo_Trans)
    return redirect("proveedores")

#editar Proveedor
def editarProveedor(request):
    Id_Proveedor=request.POST["txtId_Proveedor"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    Direccion=request.POST["txtDireccion"]
    Ruta=request.POST["txtRuta"]
    Sucursales=request.POST["txtSucursales"]
    Num_Tel=request.POST["txtNum_Tel"]
    Metodo_Trans=request.POST["txtMetodo_Trans"]
    Proveedores=Proveedor.objects.get(Id_Proveedor=Id_Proveedor)
    Proveedores.Id_Proveedor=Id_Proveedor
    Proveedores.Nombre=Nombre
    Proveedores.Apellido=Apellido
    Proveedores.Direccion=Direccion
    Proveedores.Ruta=Ruta
    Proveedores.Sucursales=Sucursales
    Proveedores.Num_Tel=Num_Tel
    Proveedores.Metodo_Trans=Metodo_Trans
    Proveedores.save()
    return redirect("proveedores")


#seleccionar Proveedor
def seleccionarProveedor(request,Id_Proveedor):
    Proveedores=Proveedor.objects.get(Id_Proveedor=Id_Proveedor)
    return render(request,"editarProveedor.html",{'listaProveedores':Proveedores})

#borrar Proveedor
def borrarProveedor(request,Id_Proveedor):
    Productos=Proveedor.objects.get(Id_Proveedor=Id_Proveedor)
    Productos.delete()
    return redirect("proveedores")