from django.urls import path
from . import views

urlpatterns=[
    path('proveedores',views.inicio_vista,name='proveedores'),
    path("registrarProveedor/",views.registrarProveedor, name="registrarProveedor"),
    path("seleccionarProveedor/<Id_Proveedor>",views.seleccionarProveedor, name="seleccionaProveedor"),
    path("editarProveedor/",views.editarProveedor, name="editarProveedor"),
    path("borrarProveedor/<Id_Proveedor>",views.borrarProveedor,name="borrarProveedor")
]