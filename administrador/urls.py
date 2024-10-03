from django.contrib import admin
from django.urls import path,include
from administrador import views


urlpatterns = [
    # url de empleados 
    path('users/registrarusuario/',views.registartuser),
    path('users/',views.users),
    path('users/eliminar/<cedula>',views.eliminaruser),
    path('users/actualizar/<cedula>',views.actualizaruser),
    path('users/editarU/<cedula>',views.editarUsuario),
    # -tipo user
    path('users/tipouser/',views.irtipo_user),
    path('users/tipouser/registrtipouser/',views.registartipo_user),
    path('users/tipouser/EliminarTipoE/<tipo>',views.eliminartipo_user),



    # url de habitaciones
    path('habitaciones/',views.habitacione),
    path('habitaciones/registrarhabitacion/',views.registarhabitacion),
    path('habitaciones/actializarhabitacion/<numero_H>',views.actualizahab),
    path('habitaciones/editarhabitacion/<numero_H>',views.editarhabitacion),
    path('habitaciones/eliminarHabitacion/<numero_H>',views.eliminarhabitacion),
    # -tipo habitacion
    path('habitaciones/tipohabitacion/',views.irtipo_habitacion),
    path('habitaciones/tipohabitacion/registartipohabitacion/',views.registartipo_habitacion),
    path('habitaciones/tipohabitacion/Eliminartipohabitacion/<tipo>',views.eliminartipo_habitacion),



    # url de servicios
    path('servicios/',views.irservicios),
    path('servicios/regisatarServi/',views.registarServicio),
    path('servicios/eliminarServi/<tipo>',views.eliminarServi),
    # url de mobiliario
    path('mobiliario/',views.irmobiliario),
    path('mobiliario/regisatarMobiliario/',views.registarMobiliario),
    path('mobiliario/editarMobiliario/<codigo>',views.editarMobiliario),
    path('mobiliario/actializarMobiliario/<codigo>',views.actualizaMobiliario),
    path('mobiliario/eliminarMobiliario/<codigo>',views.eliminarMobiliario),








    
    
]
