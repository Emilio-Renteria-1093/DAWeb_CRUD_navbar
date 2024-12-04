from django.shortcuts import render,redirect
from .models import Venta
# Create your views here.
def inicio_vista(request):
    ListaVenta=Venta.objects.all()
    return render(request,'gestionarVenta.html',{'listaVentas':ListaVenta})

def registrarVenta(request):
    Id_Venta=request.POST["txtId_Venta"]
    Id_Nomina=request.POST["txtId_Nomina"]
    Fecha_Venta=request.POST["txtFecha_Venta"]
    Id_Empleado=request.POST["txtId_Empleado"]
    Total=request.POST["txtTotal"]
    Producto_Vendido=request.POST["txtProducto_Vendido"]
    Cant_Productos=request.POST["txtCant_Productos"]
    Id_Producto=request.POST["txtId_Producto"]
    Id_Sucursal=request.POST["txtId_Sucursal"]
    Id_Proveedor=request.POST["txtCant_Productos"]


    guardarVenta=Venta.objects.create(Id_Venta=Id_Venta,Id_Nomina=Id_Nomina,Fecha_Venta=Fecha_Venta,Id_Empleado=Id_Empleado,Total=Total,Producto_Vendido=Producto_Vendido,Cant_Productos=Cant_Productos,Id_Producto=Id_Producto,Id_Sucursal=Id_Sucursal,Id_Proveedor=Id_Proveedor)
    return redirect("Ventas")

#editar Venta
def editarVenta(request):
    Id_Venta=request.POST["txtId_Venta"]
    Id_Nomina=request.POST["txtId_Nomina"]
    Fecha_Venta=request.POST["txtFecha_Venta"]
    Id_Empleado=request.POST["txtId_Empleado"]
    Total=request.POST["txtTotal"]
    Producto_Vendido=request.POST["txtProducto_Vendido"]
    Cant_Productos=request.POST["txtCant_Productos"]
    Id_Producto=request.POST["txtId_Producto"]
    Id_Sucursal=request.POST["txtId_Sucursal"]
    Id_Proveedor=request.POST["txtCant_Productos"]

    Ventas=Venta.objects.get(Id_Venta=Id_Venta)
    Ventas.Id_Venta=Id_Venta
    Ventas.Id_Nomina=Id_Nomina
    Ventas.Fecha_Venta=Fecha_Venta
    Ventas.Id_Empleado=Id_Empleado
    Ventas.Total=Total
    Ventas.Producto_Vendido=Producto_Vendido
    Ventas.Cant_Productos=Cant_Productos
    Ventas.Id_Producto=Id_Producto
    Ventas.Id_Sucursal=Id_Sucursal
    Ventas.Id_Proveedor=Id_Proveedor
    Ventas.save()
    
    return redirect("Ventas")


#seleccionar Venta
def seleccionarVenta(request,Id_Venta):
    Ventas=Venta.objects.get(Id_Venta=Id_Venta)
    return render(request,"editarVenta.html",{'listaVentas':Ventas})

#borrar Venta
def borrarVenta(request,Id_Venta):
    Ventas=Venta.objects.get(Id_Venta=Id_Venta)
    Ventas.delete()
    return redirect("Ventas")