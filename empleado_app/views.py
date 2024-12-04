from django.shortcuts import render,redirect
from .models import Empleados
# Create your views here.
def inicio_vista(request):
    ListadoEmpleado=Empleados.objects.all()
    return render(request,'gestionarEmpleado.html',{'listaClientes':ListadoEmpleado})

def registrarEmpleado(request):
    Id_Empleado=request.POST["txtid_Empleado"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    Sexo=request.POST["txtSexo"]
    Direccion=request.POST["txtDireccion"]
    Num_Tel=request.POST["txtNum_Tel"]
    Email=request.POST["txtEmail"]
    Nomina=request.POST["txtNomina"]


    guardarEmpleado=Empleados.objects.create(Id_Empleado=Id_Empleado,Nombre=Nombre,Apellido=Apellido,Sexo=Sexo,Direccion=Direccion,Num_Tel=Num_Tel,Email=Email,Nomina=Nomina)
    return redirect("empleados")

#editar Empleado
def editarEmpleado(request):
    Id_Empleado=request.POST["txtid_Empleado"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    Sexo=request.POST["txtSexo"]
    Direccion=request.POST["txtDireccion"]
    Num_Tel=request.POST["txtNum_Tel"]
    Email=request.POST["txtEmail"]
    Nomina=request.POST["txtNomina"]
    empleado=Empleados.objects.get(Id_Empleado=Id_Empleado)
    empleado.Nombre=Nombre
    empleado.Apellido=Apellido
    empleado.Sexo=Sexo
    empleado.Direccion=Direccion
    empleado.Num_Tel=Num_Tel
    empleado.Email=Email
    empleado.Nomina=Nomina
    empleado.save()
    return redirect("empleados")


#seleccionar empleado
def seleccionarEmpleado(request,Id_Empleado):
    empleado=Empleados.objects.get(Id_Empleado=Id_Empleado)
    return render(request,"editarEmpleado.html",{'listaEmpleados':empleado})

#borrar Empleado
def borrarEmpleado(request,Id_Empleado):
    empelado=Empleados.objects.get(Id_Empleado=Id_Empleado)
    empelado.delete()
    return redirect("empleados")