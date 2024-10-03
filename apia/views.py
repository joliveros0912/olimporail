#from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import*
from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request ,'index.html')


#---

class viw_tipo_empleado(viewsets.ModelViewSet):
    queryset= tipo_empleado.objects.all()
    serializer_class=zer_tipo_empleado

#-----
class viw_estado_empleados(viewsets.ModelViewSet):
    queryset= estado_empleados.objects.all()
    serializer_class=zer_estado_empleados

#-----
class viw_empleados(viewsets.ModelViewSet):
    queryset= empleados.objects.all()
    serializer_class=zer_empleados

#-----
class viw_estado_cliente(viewsets.ModelViewSet):
    queryset= estado_cliente.objects.all()
    serializer_class=zer_estado_cliente

#-----
class viw_tipo_documento(viewsets.ModelViewSet):
    queryset= tipo_documento.objects.all()
    serializer_class=zer_tipo_documento

#-----
    
class viw_cliente(viewsets.ModelViewSet):
    queryset= cliente.objects.all()
    serializer_class=zer_cliente

#-----
class viw_tipo_habitacion(viewsets.ModelViewSet):
    queryset= tipo_habitacion.objects.all()
    serializer_class=zer_tipo_habitacion

#-----
class viw_estado_habitacion(viewsets.ModelViewSet):
    queryset= estado_habitacion.objects.all()
    serializer_class=zer_estado_habitacion

#-----
class viw_mobiliario(viewsets.ModelViewSet):
    queryset= mobiliario.objects.all()
    serializer_class=zer_mobiliario

#-----
class viw_habitacion(viewsets.ModelViewSet):
    queryset= habitacion.objects.all()
    serializer_class=zer_habitacion

#-----
class viw_estado_reserva(viewsets.ModelViewSet):
    queryset= estado_reserva.objects.all()
    serializer_class=zer_estado_reserva

#-----
class viw_reserva(viewsets.ModelViewSet):
    queryset= reserva.objects.all()
    serializer_class=zer_reserva

#-----
class viw_huspedes_reserva(viewsets.ModelViewSet):
    queryset= huspedes_reserva.objects.all()
    serializer_class=zer_huspedes_reserva

#-----
class viw_servicios(viewsets.ModelViewSet):
    queryset= servicios.objects.all()
    serializer_class=zer_servicios

#-----
class viw_adicionales(viewsets.ModelViewSet):
    queryset= adicionales.objects.all()
    serializer_class=zer_adicionales

#-----
class viw_detalles_factura(viewsets.ModelViewSet):
    queryset= detalles_factura.objects.all()
    serializer_class=zer_detalles_factura

#-----
class viw_factura(viewsets.ModelViewSet):
    queryset= factura.objects.all()
    serializer_class=zer_factura

