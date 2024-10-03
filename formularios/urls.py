from django.contrib import admin
from django.urls import path,include
from formularios import views


urlpatterns = [
    path('registro/',views.registro),
    path('login/', views.mostrarinicio,name="login1"),
    path('login/verifi/', views.inicio),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('administrador/',include('administrador.urls')),



]