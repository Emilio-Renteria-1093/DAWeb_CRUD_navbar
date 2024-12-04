from django.urls import path
from . import views

urlpatterns=[
    path('nominas',views.inicio_vista,name='nominas'),
    path("registrarNomina/",views.registrarNomina, name="registrarNomina"),
    path("seleccionarNomina/<Id_Nomina>",views.seleccionarNomina, name="seleccionarNomina"),
    path("editarNomina/",views.editarNomina, name="editarNomina"),
    path("borrarNomina/<Id_Nomina>",views.borrarNomina,name="borrarNomina")
]