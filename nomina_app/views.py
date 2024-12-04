from django.shortcuts import render,redirect
from .models import Nomina
# Create your views here.
def inicio_vista(request):
    ListadoNomina=Nomina.objects.all()
    return render(request,'gestionarNomina.html',{'listaNomina':ListadoNomina})

def registrarNomina(request):
    Id_Nomina=request.POST["txtId_Nomina"]
    Id_Empleado=request.POST["txtId_Empleado"]
    Fecha_Pago=request.POST["txtFecha_Pago"]
    Periodo_Pago=request.POST["txtPeriodo_Pago"]
    Descripcion=request.POST["txtDescripcion"]
    Total=request.POST["txtTotal"]


    guardarEmpleado=Nomina.objects.create(Id_Nomina=Id_Nomina,Id_Empleado=Id_Empleado,Fecha_Pago=Fecha_Pago,Periodo_Pago=Periodo_Pago,Descripcion=Descripcion,Total=Total)
    return redirect("nominas")

#editar Nomina
def editarNomina(request):
    Id_Nomina=request.POST["txtId_Nomina"]
    Id_Empleado=request.POST["txtId_Empleado"]
    Fecha_Pago=request.POST["txtFecha_Pago"]
    Periodo_Pago=request.POST["txtPeriodo_Pago"]
    Descripcion=request.POST["txtDescripcion"]
    Total=request.POST["txtTotal"]
    nomina=Nomina.objects.get(Id_Nomina=Id_Nomina)
    nomina.Id_Empleado=Id_Empleado
    nomina.Fecha_Pago=Fecha_Pago
    nomina.Periodo_Pago=Periodo_Pago
    nomina.Descripcion=Descripcion
    nomina.Total=Total
    nomina.save()
    return redirect("nominas")


#seleccionar Nomina
def seleccionarNomina(request,Id_Nomina):
    nomina=Nomina.objects.get(Id_Nomina=Id_Nomina)
    return render(request,"editarNomina.html",{'listaNomina':nomina})

#borrar Nomina
def borrarNomina(request,Id_Nomina):
    nomina=Nomina.objects.get(Id_Nomina=Id_Nomina)
    nomina.delete()
    return redirect("nominas")