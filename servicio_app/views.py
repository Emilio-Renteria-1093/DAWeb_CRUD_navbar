from django.shortcuts import render,redirect
from .models import Servicio
# Create your views here.
def inicio_vista(request):
    ListadoServicio=Servicio.objects.all()
    return render(request,'gestionarServicio.html',{'listaServicio':ListadoServicio})

def registrarServicio(request):
    Id_Servicio=request.POST["txtId_Servicio"]
    Tipo_Servicio=request.POST["txtTipo_Servicio"]
    Costo=request.POST["txtCosto"]
    Material=request.POST["txtMaterial"]
    Fecha_inicio=request.POST["txtFecha_inicio"]
    Fecha_finalizado=request.POST["txtFecha_finalizado"]
    Resolucion_Problema=request.POST["txtResolucion_Problema"]


    guardarServicio=Servicio.objects.create(Id_Servicio=Id_Servicio,Tipo_Servicio=Tipo_Servicio,Costo=Costo,Material=Material,Fecha_inicio=Fecha_inicio,Fecha_finalizado=Fecha_finalizado,Resolucion_Problema=Resolucion_Problema)
    return redirect("servicios")

#editar Servicio
def editarServicio(request):
    Id_Servicio=request.POST["txtId_Servicio"]
    Tipo_Servicio=request.POST["txtTipo_Servicio"]
    Costo=request.POST["txtCosto"]
    Material=request.POST["txtMaterial"]
    Fecha_inicio=request.POST["txtFecha_inicio"]
    Fecha_finalizado=request.POST["txtFecha_finalizado"]
    Resolucion_Problema=request.POST["txtResolucion_Problema"]
    servicio=Servicio.objects.get(Id_Servicio=Id_Servicio)
    servicio.Tipo_Servicio=Tipo_Servicio
    servicio.Costo=Costo
    servicio.Material=Material
    servicio.Fecha_inicio=Fecha_inicio
    servicio.Fecha_finalizado=Fecha_finalizado
    servicio.Resolucion_Problema=Resolucion_Problema
    servicio.save()
    return redirect("servicios")


#seleccionar Servicio
def seleccionarServicio(request,Id_Servicio):
    servicio=Servicio.objects.get(Id_Servicio=Id_Servicio)
    return render(request,"editarServicio.html",{'listaServicio':servicio})

#borrar Servicio
def borrarServicio(request,Id_Servicio):
    servicio=Servicio.objects.get(Id_Servicio=Id_Servicio)
    servicio.delete()
    return redirect("servicios")