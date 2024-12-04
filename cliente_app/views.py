from django.shortcuts import render,redirect
from .models import Clientes
# Create your views here.
def inicio_vista(request):
    ListadoClientes=Clientes.objects.all()
    return render(request,'gestionarCliente.html',{'listaClientes':ListadoClientes})

def registrarCliente(request):
    Id_Cliente=request.POST["txtid_Cliente"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    Sexo=request.POST["txtSexo"]
    Direccion=request.POST["txtDireccion"]
    Num_Tel=request.POST["txtNum_Tel"]
    Email=request.POST["txtEmail"]


    guardarCientes=Clientes.objects.create(Id_Cliente=Id_Cliente,Nombre=Nombre,Apellido=Apellido,Sexo=Sexo,Direccion=Direccion,Num_Tel=Num_Tel,Email=Email)
    return redirect("clientes")

#editar clientes
def editarCliente(request):
    Id_Cliente=request.POST["txtid_Cliente"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    Sexo=request.POST["txtSexo"]
    Direccion=request.POST["txtDireccion"]
    Num_Tel=request.POST["txtNum_Tel"]
    Email=request.POST["txtEmail"]
    Cliente=Clientes.objects.get(Id_Cliente=Id_Cliente)
    Cliente.Nombre=Nombre
    Cliente.Apellido=Apellido
    Cliente.Sexo=Sexo
    Cliente.Direccion=Direccion
    Cliente.Num_Tel=Num_Tel
    Cliente.Email=Email
    Cliente.save()
    return redirect("clientes")


#seleccionar cliente
def seleccionarCliente(request,Id_Cliente):
    cliente=Clientes.objects.get(Id_Cliente=Id_Cliente)
    return render(request,"editarClientes.html",{'listaClientes':cliente})

#borrar cliente
def borrarCliente(request,Id_Cliente):
    cliente=Clientes.objects.get(Id_Cliente=Id_Cliente)
    cliente.delete()
    return redirect("clientes")