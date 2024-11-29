from django.urls import path
from . import views

urlpatterns=[
    path('',views.inicio_vista,name='clientes'),
    path("registrarCliente/",views.registrarCliente, name="registrarCliente"),
    path("seleccionarCliente/<Id_Cliente>",views.seleccionarCliente, name="seleccionarCliente"),
    path("editarCliente/",views.editarCliente, name="editarCliente"),
    path("borrarCliente/<Id_Cliente>",views.borrarCliente,name="borrarCliente")
]