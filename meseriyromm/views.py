


from django.shortcuts import redirect, render
from apia.models import *

# Create your views here.


def SERadicionales(request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)

        if empleado.codigo_usu_id == "camarero" :
            servicio =servicios.objects.all
            return render(request ,'meserosRom.html',{"tipo_ser":servicio})
        
        elif empleado.codigo_usu_id == "room_service": 
            servicio =servicios.objects.all
            return render(request ,'meserosRom.html',{"tipo_ser":servicio})

        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
    else:
        return redirect("/formularios/login/")
    

    

def registaradicionales(request):
    if request.user.is_authenticated:
        
        empleado = empleados.objects.get(cc_usu=request.user)
        
        # Verificar el tipo de usuario
        if empleado.codigo_usu_id == "camarero" :
            numero_ser=request.POST["id_reserva"]
            tipo_ser=request.POST["tipo"]
            valo=request.POST["valor_C"]
            descip=request.POST["descipcion"]
            print(tipo_ser)

            adicion=adicionales.objects.create(
        
                id_reserva_id=numero_ser,
                id_servi_id=tipo_ser,
                valor=valo,
                descripcion=descip
                                            )

            return redirect("/adicionales/meseros/")
        
        elif empleado.codigo_usu_id == "room_service":
            numero_ser=request.POST["id_reserva"]
            tipo_ser=request.POST["tipo"]
            valo=request.POST["valor_C"]
            descip=request.POST["descipcion"]
            print(tipo_ser)

            adicion=adicionales.objects.create(
        
                id_reserva_id=numero_ser,
                id_servi_id=tipo_ser,
                valor=valo,
                descripcion=descip
                                            )

            return redirect("/adicionales/meseros/")
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    

    else:
        return redirect("/formularios/login/")
