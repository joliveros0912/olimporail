from rest_framework import serializers
from .models import*


#---
class zer_tipo_empleado (serializers.ModelSerializer):
    class Meta:
        model= tipo_empleado
        fields="__all__"

#---
class zer_estado_empleados (serializers.ModelSerializer):
    class Meta:
        model= estado_empleados
        fields="__all__"

#---
class zer_empleados (serializers.ModelSerializer):
    class Meta:
        model= empleados
        fields="__all__"

#---
class zer_estado_cliente(serializers.ModelSerializer):
    class Meta:
        model= estado_cliente
        fields="__all__"

#---
class zer_tipo_documento(serializers.ModelSerializer):
    class Meta:
        model= tipo_documento
        fields="__all__"

#---
        
class zer_cliente(serializers.ModelSerializer):
    class meta:
        model= cliente
        fields="__all__"
#---
class zer_tipo_habitacion(serializers.ModelSerializer):
    class Meta:
        model= tipo_habitacion
        fields="__all__"

#---
class zer_estado_habitacion(serializers.ModelSerializer):
    class Meta:
        model= estado_habitacion
        fields="__all__"

#---        
class zer_mobiliario(serializers.ModelSerializer):
    class Meta:
        model= mobiliario
        fields="__all__"

#---        
class zer_habitacion(serializers.ModelSerializer):
    class Meta:
        model= habitacion
        fields="__all__"

#---        
class zer_estado_reserva(serializers.ModelSerializer):
    class Meta:
        model= estado_reserva
        fields="__all__"

#---
class zer_reserva(serializers.ModelSerializer):
    class Meta:
        model= reserva
        fields="__all__"

#---
class zer_huspedes_reserva(serializers.ModelSerializer):
    class Meta:
        model= huspedes_reserva
        fields="__all__"

#---
class zer_servicios(serializers.ModelSerializer):
    class Meta:
        model= servicios
        fields="__all__"

#---
        
class zer_adicionales(serializers.ModelSerializer):
    class Meta:
        model= adicionales
        fields="__all__"

#---
class zer_detalles_factura(serializers.ModelSerializer):
    class Meta:
        model= detalles_factura
        fields="__all__"


#---
class zer_factura(serializers.ModelSerializer):
    class Meta:
        model= factura
        fields="__all__"