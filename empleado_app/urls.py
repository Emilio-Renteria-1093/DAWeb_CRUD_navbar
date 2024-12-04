from django.urls import path
from . import views

urlpatterns=[
    path('empleados',views.inicio_vista,name='empleados'),
    path("registrarEmpleado/",views.registrarEmpleado, name="registrarEmpleado"),
    path("seleccionarEmpleado/<Id_Empleado>",views.seleccionarEmpleado, name="seleccionarEmpleado"),
    path("editarEmpleado/",views.editarEmpleado, name="editarEmpleado"),
    path("borrarEmpleado/<Id_Empleado>",views.borrarEmpleado,name="borrarEmpleado")
]