from django.urls import path
from . import views

urlpatterns=[
    path('sucursales',views.inicio_vista,name='sucursales'),
    path("registrarSucursal/",views.registrarSucursal, name="registrarSucursal"),
    path("seleccionarSucursal/<Id_Sucursal>",views.seleccionarSucursal, name="seleccionarSucursal"),
    path("editarSucursal/",views.editarSucursal, name="editarSucursal"),
    path("borrarSucursal/<Id_Sucursal>",views.borrarSucursal,name="borrarSucursal")
]