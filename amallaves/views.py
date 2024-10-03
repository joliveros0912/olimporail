from django.shortcuts import redirect, render
from apia.models import *
# Create your views here.


def menueestadohabitacione(request):
    if request.user.is_authenticated:
        
        empleado = empleados.objects.get(cc_usu=request.user)
        
        # Verificar el tipo de usuario
        if empleado.codigo_usu_id == 'ama_de_llaves':
            
            habit =habitacion.objects.all
            return render(request ,'amadellaves.html',
                        {"habitacion":habit})


        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    

    else:
        return redirect("/formularios/login/")


def actualizaestadop(request,numero_H):
    if request.user.is_authenticated:
        
        empleado = empleados.objects.get(cc_usu=request.user)
        
        # Verificar el tipo de usuario
        if empleado.codigo_usu_id == 'ama_de_llaves':
            
            estado =estado_habitacion.objects.all
            habita =habitacion.objects.get(numero_H=numero_H)

            return render(request,"edicionamadllaves.html",{"habitacion":habita,"estado1":estado})


        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    

    else:
        return redirect("/formularios/login/")
    


def editarestado(request,numero_H):
    if request.user.is_authenticated:
        
        empleado = empleados.objects.get(cc_usu=request.user)
        
        # Verificar el tipo de usuario
        if empleado.codigo_usu_id == 'ama_de_llaves':
            
                estado=request.POST["estado2"]
                habita =habitacion.objects.get(numero_H=numero_H)
                habita.estado_id=estado

                habita.save()
                

                return redirect("/amadellaves/accionamadellaves/")


        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    

    else:
        return redirect("/formularios/login/")
    
