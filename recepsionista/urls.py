from django.contrib import admin
from django.urls import path,include
from recepsionista import views




urlpatterns = [
    path('recepcionista/',views.recervas),
    path('recepcionista/registarReservaResep/',views.crearReservaRes),
    path('recepcionista/eliminarRES/<numero_res>',views.eliminarRES),
    path('recepcionista/factura/<id_reserva>/<habitacion_id>/',views.generar_factura),

    # path('recepcionista/registarservi/',views.registaradicionales),
    ]