from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
from apia.models import *
from django.contrib import messages
from django.contrib.auth.hashers import make_password 





def users(request):
    if request.user.is_authenticated:
            
            empleado = empleados.objects.get(cc_usu=request.user)
            
            # Verificar el tipo de usuario
            if empleado.codigo_usu_id == 'Administrador':
                usersu = empleados.objects.all()
                estado = estado_empleados.objects.all()
                tipo = tipo_empleado.objects.all()

                return render(request, 'users/users.html', {"usuarios": usersu, "estado1": estado, "tipo": tipo})
            else:
                # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
                messages.error(request, "No tienes permiso para acceder a esta página.")
                return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    

    else:
        return redirect("/formularios/login/")
    

    

@login_required
def registartuser(request):
    if request.method == 'POST':
        cedula = request.POST.get("cedula")
        cedula=request.POST["cedula"]
        nombre=request.POST["nombre"]
        apellido=request.POST["apellido"]
        direcion=request.POST["direcion"]
        contacto_ememergencia=request.POST["contacto_ememergencia"]
        acudiente=request.POST["acudiente"]
        telefono=request.POST["telefono"]
        correo=request.POST["correo"]
        eps=request.POST["eps"]
        caja_de_compensacion=request.POST["caja_de_compensacion"]
        tipo=request.POST["tipo"]
        estado=request.POST["estado"]
        contraseña=request.POST["contraseña"]
        # Verificar si la cédula ya está en uso

        if empleados.objects.filter(cc_usu=cedula).exists():
            messages.error(request, "La cédula ya está registrada.")
            return render(request, 'error.html', {"message": "persona ya registrada con ese numero de documento ."})
         # O a donde sea apropiado
        # Si la cédula no está en uso, proceder con el registro

        else:
            hashed_password = make_password(contraseña)

            nombre = request.POST.get("nombre")
            apellido = request.POST.get("apellido")
            # Resto de los campos...
            users =empleados.objects.create(
            cc_usu=cedula,
            nombre=nombre,
            apellido=apellido,
            direcion=direcion,
            contacto_ememergenci=contacto_ememergencia,
            nombre_contacto=acudiente,
            telefono=telefono,
            correo=	correo,
            eps=eps,
            caja_de_compensacion=caja_de_compensacion,
            codigo_usu_id=tipo,
            estado_id=estado,
            password=hashed_password,
                                    )
            return redirect("/administrador/users/")
    else:
        return redirect("/administrador/users/")
    


@login_required

def eliminaruser(request,cedula):
    if request.user.is_authenticated:
            empleado = empleados.objects.get(cc_usu=request.user)

            # Verificar el tipo de usuario
            if empleado.codigo_usu_id == 'Administrador':
                
                estado="inactivo"
                users =empleados.objects.get(cc_usu=cedula)
                users.estado_id=estado
                users.save()
                # users.delete()
                return redirect("/administrador/users/")
            else:
                # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
                messages.error(request, "No tienes permiso para acceder a esta página.")
                return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    

    else:
        return redirect("/formularios/login/")
    
    

@login_required


def actualizaruser (request,cedula):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            estado =estado_empleados.objects.all
            tipo =tipo_empleado.objects.all
            users =empleados.objects.get(cc_usu=cedula)
            return render(request,"users/edicionusuario.html",{"cedula":users,"estado1":estado,"tipo1":tipo})
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")


@login_required
def editarUsuario(request,cedula):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            nombre=request.POST["nombre"]
            apellido=request.POST["apellido"]
            direcion=request.POST["direcion"]
            contacto_ememergencia=request.POST["contacto_ememergencia"]
            acudiente=request.POST["acudiente"]
            telefono=request.POST["telefono"]
            correo=request.POST["correo"]
            eps=request.POST["eps"]
            caja_de_compensacion=request.POST["caja_de_compensacion"]
            tipo=request.POST["tipo2"]
            estado=request.POST["estado2"]
            contraseña=request.POST["contraseña"]
            hashed_password = make_password(contraseña)

            users =empleados.objects.get(cc_usu=cedula)

            users.cc_usu=cedula
            users.nombre=nombre
            users.apellido=apellido
            users.direcion=direcion
            users.contacto_ememergenci=contacto_ememergencia
            users.nombre_contacto=acudiente
            users.telefono=telefono
            users.correo=correo
            users.eps=eps
            users.caja_de_compensacion=caja_de_compensacion

            users.codigo_usu_id=tipo

            users.estado_id=estado
    
            users.password=hashed_password
            users.save()

            return redirect("/administrador/users/")
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    
# --tipo_user

@login_required
def irtipo_user (request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            dato=tipo_empleado.objects.all
    
            return render(request ,'tipouser/Tipouser.html',{"dato":dato})      
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")

    
    
@login_required
def registartipo_user(request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            
            tipo_E=request.POST["tipo"]
            
        
            servio =tipo_empleado.objects.create(
                tipo_empleado=tipo_E)
            
            return redirect("/administrador/users/tipouser/")
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    

@login_required
def eliminartipo_user(request,tipo):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            
            tipo_E =tipo_empleado.objects.get(tipo_empleado=tipo)
            tipo_E.save()
            tipo_E.delete()
            return redirect("/administrador/users/tipouser/")
            
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    # 
    



# ----------------------- habiatcione 

@login_required
def habitacione(request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            habit =habitacion.objects.all

            estado =estado_habitacion.objects.all
            tipo =tipo_habitacion.objects.all
            moviliario=mobiliario.objects.all
            return render(request ,'habitaciones/habitaciones.html',
                    {"habitacion":habit,"estado1":estado,"tipo":tipo,"moviliario":moviliario})
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")

    



    

@login_required
def registarhabitacion(request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            
            numero_de_habitacion=request.POST["numero_H"]
            cantidad_personas=request.POST["cantidad_p"]
            valor=request.POST["valor"]
            estado=request.POST["estado"]
            tipo_de_moviliario=request.POST["mibiliario"]
            tipo=request.POST["tipo"]
        
            habita =habitacion.objects.create(
                numero_H=numero_de_habitacion,
                cantidad_p=cantidad_personas,
                valor_habitacion=valor,
                estado_id=estado,
                id_mobi_id=tipo_de_moviliario,
                tipo_id=tipo,
                                            )
            return redirect("/administrador/habitaciones/")


        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    



@login_required
def eliminarhabitacion(request,numero_H):

    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            estado="inactivo"
            habi =habitacion.objects.get(numero_H=numero_H)
            habi.estado_id=estado
            habi.save()
            # users.delete()
            return redirect("/administrador/habitaciones/")
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    

@login_required
def actualizahab(request,numero_H):
    
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
             
            estado =estado_habitacion.objects.all
            tipo =tipo_habitacion.objects.all
            moviliario=mobiliario.objects.all


            habita =habitacion.objects.get(numero_H=numero_H)
            return render(request,"habitaciones/edicionhabitacion.html",{"habitacion":habita,"estado1":estado,"tipo1":tipo,"moviliario":moviliario})
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
   


@login_required
def editarhabitacion(request,numero_H):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            
            cantidad_personas=request.POST["cantidad_p"]
            valor=request.POST["valor"]
            estado=request.POST["estado2"]
            tipo_de_moviliario=request.POST["mibiliario"]
            tipo=request.POST["tipo2"]
        
            habita =habitacion.objects.get(numero_H=numero_H)
            habita.numero_H=numero_H
            habita.cantidad_p=cantidad_personas
            habita.valor_habitacion=valor
            habita.estado_id=estado
            habita.cantidad_p=cantidad_personas
            habita.tipo_de_moviliario=tipo_de_moviliario
            habita.tipo_id=tipo

            habita.save()
            

            return redirect("/administrador/habitaciones/")
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    

# tipo habitacion

@login_required
def irtipo_habitacion (request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            
            dato=tipo_habitacion.objects.all
            
            return render(request ,'tipoHabitacion/TipoHabitacion.html',{"dato":dato})
    
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")



@login_required
def registartipo_habitacion(request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            
            tipo_E=request.POST["tipo"]
            
        
            servio =tipo_habitacion.objects.create(
                tipo_habitacion=tipo_E)
            
            return redirect("/administrador/habitaciones/tipohabitacion/")
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    

@login_required

def eliminartipo_habitacion(request,tipo):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            
            tipo_E =tipo_habitacion.objects.get(tipo_habitacion=tipo)
            tipo_E.save()
            tipo_E.delete()
            return redirect("/administrador/habitaciones/tipohabitacion/")

            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")



# ----------------------- SERVICIO
 
@login_required
def irservicios (request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            dato=servicios.objects.all
    
            return render(request ,'Servicios/Servicios.html',{"dato":dato})
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")  

   
    
@login_required
 
def registarServicio(request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
             
            servi=request.POST["servicio"]
            
        
            servio =servicios.objects.create(
                tipo_servicio=servi)
            
            return redirect("/administrador/servicios/")
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")   
   

@login_required
  
def eliminarServi(request,tipo):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            habi =servicios.objects.get(tipo_servicio=tipo)
            habi.save()
            habi.delete()
            return redirect("/administrador/servicios/")
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")  
  

# ----------------------- MOBILIARIO
@login_required

def irmobiliario (request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            mobi=mobiliario.objects.all
    
            return render(request ,'mobiliario/Mobiliario.html',{"dato":mobi})
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")

    

@login_required

def actualizaMobiliario(request,codigo):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            codigoDato =mobiliario.objects.get(id_mobi=codigo)
            return render(request,"mobiliario/edicionMobiliario.html",{"mobi":codigoDato})
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    

@login_required
    
def eliminarMobiliario(request,codigo):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            habi =mobiliario.objects.get(id_mobi=codigo)
            habi.save()
            habi.delete()
            return redirect("/administrador/mobiliario/")
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    

@login_required

def editarMobiliario(request,codigo):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
            
            camass_encillas=request.POST["camassencillas"]
            camasd_oble=request.POST["camasdoble"]
            camask_ing=request.POST["camasking"]
            tvp_lano=request.POST["tvplano"]
            sal_a=request.POST["sala"]
            silla_s=request.POST["sillas"]
        
            movili =mobiliario.objects.get(id_mobi=codigo)
            movili.camas_sencillas=camass_encillas
            movili.camas_doble=camasd_oble
            movili.camas_king=camask_ing
            movili.tv_plano=tvp_lano
            movili.sala=sal_a
            movili.sillas=silla_s

            movili.save()
            

            return redirect("/administrador/mobiliario/")
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")


@login_required

def registarMobiliario(request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       

        if empleado.codigo_usu_id == 'Administrador':
                id_mo=request.POST["co_mibi"]            
                camass_encillas=request.POST["camassencillas"]
                camasd_oble=request.POST["camasdoble"]
                camask_ing=request.POST["camasking"]
                tvp_lano=request.POST["tvplano"]
                sal_a=request.POST["sala"]
                silla_s=request.POST["sillas"]
            
                habita =mobiliario.objects.create(
                    id_mobi=id_mo,
                    camas_sencillas=camass_encillas,
                    camas_doble=camasd_oble,
                    camas_king=camask_ing,
                    tv_plano=tvp_lano,
                    sala=sal_a,
                    sillas=silla_s,
                                                )
                return redirect("/administrador/mobiliario/")
            
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            messages.error(request, "No tienes permiso para acceder a esta página.")
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    



# para todos 

