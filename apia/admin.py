from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(tipo_empleado )
admin.site.register(estado_empleados )
admin.site.register(empleados )
admin.site.register(estado_cliente)
admin.site.register(tipo_documento)
admin.site.register(cliente)
admin.site.register(tipo_habitacion)
admin.site.register(estado_habitacion)
admin.site.register(mobiliario)
admin.site.register(habitacion)
admin.site.register(estado_reserva)
admin.site.register(reserva)
admin.site.register(huspedes_reserva)
admin.site.register(servicios)
admin.site.register(adicionales)
admin.site.register(detalles_factura)
admin.site.register(factura)

