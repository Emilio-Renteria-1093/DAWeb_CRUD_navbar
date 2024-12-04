from django.shortcuts import render,redirect
from .models import Producto
# Create your views here.
def inicio_vista(request):
    ListadoProductos=Producto.objects.all()
    return render(request,'gestionarProducto.html',{'listaProductos':ListadoProductos})

def registrarProducto(request):
    Id_Producto=request.POST["txtId_Producto"]
    Cantidad_P=request.POST["txtCantidad_P"]
    Tipo_Producto=request.POST["txtTipo_Producto"]
    Costo=request.POST["txtCosto"]
    Fecha_Ingreso=request.POST["txtFecha_Ingreso"]
    Id_Proveedor=request.POST["txtId_Proveedor"]


    guardarProductos=Producto.objects.create(Id_Producto=Id_Producto,Cantidad_P=Cantidad_P,Tipo_Producto=Tipo_Producto,Costo=Costo,Fecha_Ingreso=Fecha_Ingreso,Id_Proveedor=Id_Proveedor)
    return redirect("productos")

#editar Producto
def editarProducto(request):
    Id_Producto=request.POST["txtId_Producto"]
    Cantidad_P=request.POST["txtCantidad_P"]
    Tipo_Producto=request.POST["txtTipo_Producto"]
    Costo=request.POST["txtCosto"]
    Fecha_Ingreso=request.POST["txtFecha_Ingreso"]
    Id_Proveedor=request.POST["txtId_Proveedor"]
    Productos=Producto.objects.get(Id_Producto=Id_Producto)
    Productos.Id_Producto=Id_Producto
    Productos.Cantidad_P=Cantidad_P
    Productos.Tipo_Producto=Tipo_Producto
    Productos.Costo=Costo
    Productos.Fecha_Ingreso=Fecha_Ingreso
    Productos.Id_Proveedor=Id_Proveedor
    Productos.save()
    return redirect("productos")


#seleccionar Producto
def seleccionarProducto(request,Id_Producto):
    Productos=Producto.objects.get(Id_Producto=Id_Producto)
    return render(request,"editarProducto.html",{'listaProductos':Productos})

#borrar Producto
def borrarProducto(request,Id_Producto):
    Productos=Producto.objects.get(Id_Producto=Id_Producto)
    Productos.delete()
    return redirect("productos")