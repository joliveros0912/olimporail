from django.db import models

# Create your models here.

#empleados 
class tipo_empleado (models.Model) :
    tipo_empleado=models.CharField(max_length=20 ,primary_key=True)
    def __str__(self):
        return self.tipo_empleado

#---
class estado_empleados(models.Model):
    esatado_empleado =models.CharField(max_length=20 ,primary_key=True)
#---
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager

class empleados(AbstractBaseUser):
    cc_usu =models.CharField(max_length=20 ,primary_key=True)
    nombre =models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    direcion=models.CharField(max_length=80)
    contacto_ememergenci=models.CharField(max_length=20)
    nombre_contacto=models.CharField(max_length=30)
    telefono=models.CharField(max_length=15)
    correo=models.CharField(max_length=70)
    eps=models.CharField(max_length=20)
    contrasenaU=models.CharField(max_length=400)
    last_login = models.DateTimeField(("last login"), blank=True, null=True)
    caja_de_compensacion=models.CharField(max_length=50)
    codigo_usu=models.ForeignKey(tipo_empleado,null=True,blank=True,on_delete=models.CASCADE)
    estado=models.ForeignKey(estado_empleados ,null=True,blank=True,on_delete=models.CASCADE)
    usuario_administrador=models.BooleanField(default=False)

    USERNAME_FIELD="cc_usu"
    REQUIRED_FIELDS=["correo","nombre"]
    
    def __str__(self):
        return f'{self.cc_usu}'
    
    def has_perm(self,perm,obj =None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    @property
    def is_staff(self):
        return self.usuario_administrador
#---

# relacionado con reserva-------------------
     
class estado_cliente (models.Model):
    estado=models.CharField(max_length=20 ,primary_key=True)
    
#---
class tipo_documento (models.Model):
    tipo_documento=models.CharField(max_length=25 ,primary_key=True)
    def __str__(self):
        return self.tipo_documento

#--- cliente --------------------------------


class cliente (models.Model):
    numero_doc = models.CharField(max_length=20, primary_key=True, verbose_name="Número de Documento")
    correo = models.CharField(max_length=100, verbose_name="Correo")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    numero_contacto = models.CharField(max_length=25, verbose_name="Número de Contacto")
    contrasenaaC = models.CharField(max_length=400, verbose_name="Contraseña")
    estado = models.ForeignKey(estado_cliente, default='Activo', null=True, blank=True, on_delete=models.CASCADE, verbose_name="Estado")
    tipo_doc = models.ForeignKey(tipo_documento, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Tipo de Documento")
    last_login = models.DateTimeField(("last login"), blank=True, null=True)

#---
class tipo_habitacion (models.Model):
    tipo_habitacion=models.CharField(max_length=25 ,primary_key=True)
#---
class estado_habitacion (models.Model):
    estado_reserva=models.CharField(max_length=25 ,primary_key=True)

#---
class mobiliario (models.Model):
    id_mobi=models.CharField(max_length=20 ,primary_key=True)
    camas_sencillas=models.CharField(max_length=20)
    camas_doble=models.CharField(max_length=20)
    camas_king=models.CharField(max_length=20)
    tv_plano=models.CharField(max_length=20)
    sala=models.CharField(max_length=20)
    sillas=models.CharField(max_length=20)
    
#---
class habitacion (models.Model):
    numero_H=models.CharField(max_length=20 ,primary_key=True)
    cantidad_p=models.CharField(max_length=20)
    valor_habitacion=models.FloatField()

    id_mobi=models.ForeignKey(mobiliario ,null=True,blank=True,on_delete=models.CASCADE)
    estado=models.ForeignKey(estado_habitacion ,null=True,blank=True,on_delete=models.CASCADE)
    tipo =models.ForeignKey(tipo_habitacion ,null=True,blank=True,on_delete=models.CASCADE)

#---
class estado_reserva (models.Model):
    estado_reserva=models.CharField(max_length=25 ,primary_key=True)
#---

class reserva (models.Model):
    id_reserva=models.AutoField(primary_key=True)    
    fecah_ini=models.DateTimeField(auto_now = False)
    fecah_fin=models.DateTimeField(auto_now = False)
    valor_reserva=models.FloatField()

    habitacion=models.ForeignKey(habitacion ,null=True,blank=True,on_delete=models.CASCADE)
    numero_doc=models.ForeignKey(cliente ,null=True,blank=True,on_delete=models.CASCADE)
    estado_res=models.ForeignKey(estado_reserva ,null=True,blank=True,on_delete=models.CASCADE)

#---
class huspedes_reserva(models.Model):
    
    id_reserva=models.ForeignKey(reserva ,null=True,blank=True,on_delete=models.CASCADE)
    numero_doc=models.ForeignKey(cliente ,null=True,blank=True,on_delete=models.CASCADE)


#servivios y adiciona les factura-----------------------------------
    
class servicios (models.Model):
    tipo_servicio=models.CharField(max_length=25 ,primary_key=True)

#---
class adicionales(models.Model):
    id_adi=models.AutoField(primary_key=True)  
    descripcion=models.CharField(max_length=300)
    valor=models.FloatField()

    id_servi=models.ForeignKey(servicios ,null=True,blank=True,on_delete=models.CASCADE)
    empleado_A_cargo=models.ForeignKey(empleados ,null=True,blank=True,on_delete=models.CASCADE) 
    id_reserva=models.ForeignKey(reserva ,null=True,blank=True,on_delete=models.CASCADE)
#---

class detalles_factura(models.Model):
    id_factura=models.AutoField(primary_key=True) 
    valor_reserva=models.FloatField()
    valor_adicional=models.FloatField()

    id_reserva=models.ForeignKey(reserva ,null=True,blank=True,on_delete=models.CASCADE)
    id_adi=models.ForeignKey(adicionales ,null=True,blank=True,on_delete=models.CASCADE)

#---
    
class factura(models.Model):
    id_factura=models.AutoField(primary_key=True)
    pago_total=models.FloatField()
    fecha=models.DateTimeField()
    
    empleado_A_cargo=models.ForeignKey(empleados ,null=True,blank=True,on_delete=models.CASCADE)