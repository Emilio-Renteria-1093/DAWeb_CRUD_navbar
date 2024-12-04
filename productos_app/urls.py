from django.urls import path
from . import views

urlpatterns=[
    path('productos',views.inicio_vista,name='productos'),
    path("registrarProducto/",views.registrarProducto, name="registrarProducto"),
    path("seleccionarProducto/<Id_Producto>",views.seleccionarProducto, name="seleccionaProducto"),
    path("editarProducto/",views.editarProducto, name="editarProducto"),
    path("borrarProducto/<Id_Producto>",views.borrarProducto,name="borrarProducto")
]