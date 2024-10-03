from django.urls import path,include

from rest_framework import routers

from apia import views

router_tipo_empleado =routers.DefaultRouter()
router_tipo_empleado.register(r"tipo_empleado", views.viw_tipo_empleado)

router_estado_empleados =routers.DefaultRouter()
router_estado_empleados.register(r"estado_empleados", views.viw_estado_empleados)

router_empleados =routers.DefaultRouter()
router_empleados.register(r"empleados", views.viw_empleados)

router_estado_cliente=routers.DefaultRouter()
router_estado_cliente.register(r"estado_cliente", views.viw_estado_cliente)

router_tipo_documento=routers.DefaultRouter()
router_tipo_documento.register(r"tipo_documento", views.viw_tipo_documento)

router_cliente=routers.DefaultRouter()
router_cliente.register(r"cliente", views.viw_cliente)

router_tipo_habitacion=routers.DefaultRouter()
router_tipo_habitacion.register(r"tipo_habitacion", views.viw_tipo_habitacion)

router_estado_habitacion=routers.DefaultRouter()
router_estado_habitacion.register(r"estado_habitacion", views.viw_estado_habitacion)

router_mobiliario=routers.DefaultRouter()
router_mobiliario.register(r"mobiliario", views.viw_mobiliario)

router_habitacion=routers.DefaultRouter()
router_habitacion.register(r"habitacion", views.viw_habitacion)

router_estado_reserva=routers.DefaultRouter()
router_estado_reserva.register(r"estado_reserva", views.viw_estado_reserva)

router_reserva=routers.DefaultRouter()
router_reserva.register(r"reserva", views.viw_reserva)

router_huspedes_reserva=routers.DefaultRouter()
router_huspedes_reserva.register(r"huspedes_reserva", views.viw_huspedes_reserva)

router_servicios=routers.DefaultRouter()
router_servicios.register(r"servicios", views.viw_servicios)

router_adicionales=routers.DefaultRouter()
router_adicionales.register(r"adicionales", views.viw_adicionales)

router_detalles_factura=routers.DefaultRouter()
router_detalles_factura.register(r"detalles_factura", views.viw_detalles_factura)

router_factura=routers.DefaultRouter()
router_factura.register(r"factura", views.viw_factura)

urlpatterns = [
path("tipo_empleado/",include(router_tipo_empleado.urls)),
path("estado_empleados/",include(router_estado_empleados.urls)) ,
path("empleados/",include(router_empleados.urls)) ,
path("estado_cliente/",include(router_estado_cliente.urls)),
path("tipo_documento/",include(router_tipo_documento.urls)),
path("cliente/",include(router_cliente.urls)),
path("tipo_habitacion/",include(router_tipo_habitacion.urls)),
path("estado_habitacion/",include(router_estado_habitacion.urls)),
path("mobiliario/",include(router_mobiliario.urls)),
path("habitacion/",include(router_habitacion.urls)),
path("estado_reserva/",include(router_estado_reserva.urls)),
path("reserva/",include(router_reserva.urls)),
path("huspedes_reserva/",include(router_huspedes_reserva.urls)),
path("servicios/",include(router_servicios.urls)),
path("adicionales/",include(router_adicionales.urls)),
path("detalles_factura/",include(router_detalles_factura.urls)),
path("factura/",include(router_factura.urls)),
]