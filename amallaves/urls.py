from django.contrib import admin
from django.urls import path,include
from amallaves import views


urlpatterns = [
    path('accionamadellaves/',views.menueestadohabitacione),
    path('accionamadellaves/cambiaresatdo/<numero_H>/',views.actualizaestadop),
    path('accionamadellaves/editarestado/<numero_H>/',views.editarestado)


    
    ]