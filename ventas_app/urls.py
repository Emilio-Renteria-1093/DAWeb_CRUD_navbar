from django.urls import path
from . import views

urlpatterns=[
    path('Ventas',views.inicio_vista,name='Ventas'),
    path("registrarVenta/",views.registrarVenta, name="registrarVenta"),
    path("seleccionarVenta/<Id_Venta>",views.seleccionarVenta, name="seleccionarVenta"),
    path("editarVenta/",views.editarVenta, name="editarVenta"),
    path("borrarVenta/<Id_Venta>",views.borrarVenta,name="borrarVenta")
]