from django.shortcuts import render,redirect
from .models import Sucursal
# Create your views here.
def inicio_vista(request):
    ListaSucursal=Sucursal.objects.all()
    return render(request,'gestionarSucursal.html',{'listaSucursales':ListaSucursal})

def registrarSucursal(request):
    Id_Sucursal=request.POST["txtId_Sucursal"]
    Locolizacion=request.POST["txtLocolizacion"]
    Num_Empleados=request.POST["txtNum_Empleados"]
    Ganancias=request.POST["txtGanancias"]
    Telefono=request.POST["txtTelefono"]
    Email=request.POST["txtEmail"]
    Encargado=request.POST["txtEncargado"]


    guardarSucursal=Sucursal.objects.create(Id_Sucursal=Id_Sucursal,Locolizacion=Locolizacion,Num_Empleados=Num_Empleados,Ganancias=Ganancias,Telefono=Telefono,Encargado=Encargado,Email=Email)
    return redirect("sucursales")

#editar sucursal
def editarSucursal(request):
    Id_Sucursal=request.POST["txtId_Sucursal"]
    Locolizacion=request.POST["txtLocolizacion"]
    Num_Empleados=request.POST["txtNum_Empleados"]
    Ganancias=request.POST["txtGanancias"]
    Telefono=request.POST["txtTelefono"]
    Email=request.POST["txtEmail"]
    Encargado=request.POST["txtEncargado"]

    sucurlsal=Sucursal.objects.get(Id_Sucursal=Id_Sucursal)
    sucurlsal.Locolizacion=Locolizacion
    sucurlsal.Num_Empleados=Num_Empleados
    sucurlsal.Ganancias=Ganancias
    sucurlsal.Telefono=Telefono
    sucurlsal.Encargado=Encargado
    sucurlsal.Email=Email
    sucurlsal.save()
    
    return redirect("sucursales")


#seleccionar sucursal
def seleccionarSucursal(request,Id_Sucursal):
    sucursal=Sucursal.objects.get(Id_Sucursal=Id_Sucursal)
    return render(request,"editarSucursal.html",{'listaSucursales':sucursal})

#borrar sucursal
def borrarSucursal(request,Id_Sucursal):
    sucursal=Sucursal.objects.get(Id_Sucursal=Id_Sucursal)
    sucursal.delete()
    return redirect("sucursales")