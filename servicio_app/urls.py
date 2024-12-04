from django.urls import path
from . import views

urlpatterns=[
    path('servicios',views.inicio_vista,name='servicios'),
    path("registrarServicio/",views.registrarServicio, name="registrarServicio"),
    path("seleccionarServicio/<Id_Servicio>",views.seleccionarServicio, name="seleccionarServicio"),
    path("editarServicio/",views.editarServicio, name="editarServicio"),
    path("borrarServicio/<Id_Servicio>",views.borrarServicio,name="borrarServicio"),
]