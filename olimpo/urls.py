from django.contrib import admin
from django.urls import path,include
from olimpo import views


urlpatterns = [
    path('reservaC/',views.reservaC),
    path('reservaC/reserva/<documento>/<fecha_ini>/<fecha_fin>/',views.crearReservaRes_clien),
    path('reservaC/reserva/generarinformedereserva/<id_res>/',views.pdfres),

    ]