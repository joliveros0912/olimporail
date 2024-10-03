from tkinter import Canvas
from django.shortcuts import render ,redirect
from apia.models import *
import mysql.connector
# pip install mysql-connector-python
# Create your views here.

def recervas(request):
    if request.user.is_authenticated:
        
        empleado = empleados.objects.get(cc_usu=request.user)
        
        # Verificar el tipo de usuario
        if empleado.codigo_usu_id == 'resepcionista':
            reservass =reserva.objects.all
    
            habisao =habitacion.objects.all

            return render(request ,'reserva.html',{"res":reservass,"habit":habisao})

        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    

    else:
        return redirect("/formularios/login/")
   
def crearReservaRes(request):
    if request.user.is_authenticated:
        
        empleado = empleados.objects.get(cc_usu=request.user)
        
        # Verificar el tipo de usuario
        if empleado.codigo_usu_id == 'resepcionista':
            fecah_ini_pos=request.POST["fecha_in"]
            fecah_fin_pos=request.POST["fecha_fi"]
            habitacion_pos=request.POST["tipo"]
            numero_doc_pos=request.POST["numero_doc_cli"]
            estado_res_pos="Activo"
            habitacionas=habitacion.objects.get(numero_H=habitacion_pos)
        
            habita =reserva.objects.create(
                fecah_ini=fecah_ini_pos,
                fecah_fin=fecah_fin_pos,
                valor_reserva=habitacionas.valor_habitacion,
                habitacion_id=habitacion_pos,
                numero_doc_id=numero_doc_pos,
                estado_res_id=estado_res_pos,
                                            )
            estado="Activo"
            habitacionas.estado_id=estado

            habitacionas.save()
            return redirect("/recepcionista/recepcionista/")
    else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
        return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    
   
    
def eliminarRES(request,numero_res):
    if request.user.is_authenticated:
        
        empleado = empleados.objects.get(cc_usu=request.user)
        
        # Verificar el tipo de usuario
        if empleado.codigo_usu_id == 'resepcionista':
            estado="inactivo"
            habi =reserva.objects.get(id_reserva=numero_res)
            habi.estado_res_id=estado
            habi.save()

            nuero__h=habi.habitacion_id

            # estado="mantenimiento"
            estado="Disponible"

            habitacionas=habitacion.objects.get(numero_H=nuero__h)
            habitacionas.estado_id=estado
            habitacionas.save()
            
            return redirect("/recepcionista/recepcionista/")
            

           
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    

    else:
        return redirect("/formularios/login/")
    

    # users.delete()


# import para la generacion del pdf 
from django.http import HttpResponse
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

   

def obtener_valor_adicionales(id_reserva):
    
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="olimpo_1"
    )
    cursor = conexion.cursor()

    cursor.execute("SELECT SUM(valor) FROM apia_adicionales WHERE id_reserva_id = %s", (id_reserva,))
    total_adicionales = cursor.fetchone()[0]  # Obtenemos el resultado de la consulta

    cursor.close()
    conexion.close()

    return total_adicionales

def obtener_valor_reserva(id_reserva):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="olimpo_1"
    )
    cursor = conexion.cursor()

    cursor.execute("SELECT valor_reserva FROM apia_reserva WHERE id_reserva = %s", (id_reserva,))
    valor_reserva = cursor.fetchone()[0]  # Obtenemos el resultado de la consulta

    cursor.close()
    conexion.close()

    return valor_reserva

def generar_factura(request, id_reserva, habitacion_id):
    if request.user.is_authenticated:
        
        empleado = empleados.objects.get(cc_usu=request.user)
        
        # Verificar el tipo de usuario
        if empleado.codigo_usu_id == 'resepcionista':
            try:
                    
                total_adicionales = obtener_valor_adicionales(id_reserva)
                valor_reserva = obtener_valor_reserva(id_reserva)
                estado = "inactivo"

                # Cambiar el estado de la reserva a "inactivo"
                reserva_obj = reserva.objects.get(id_reserva=id_reserva)
                reserva_obj.estado_res_id = estado
                reserva_obj.save()

                # Cambiar el estado de la habitación a "Disponible"
                habitacion_obj = habitacion.objects.get(numero_H=habitacion_id)
                habitacion_obj.estado_id = "Disponible"
                habitacion_obj.save()

                if total_adicionales is None:
                    total_adicionales = 0  # Asignar un valor predeterminado si total_adicionales es None

                if valor_reserva is None:
                    return HttpResponse("No se encontraron datos para la reserva.")

                total_factura = total_adicionales + valor_reserva

                # Crear un objeto BytesIO para almacenar el PDF
                buffer = BytesIO()

                # Crear el documento PDF
                c = canvas.Canvas(buffer, pagesize=letter)
                c.drawString(100, 750, "Factura")
                c.drawString(100, 730, f"ID de Reserva: {id_reserva}")
                c.drawString(100, 710, f"Total de Adicionales: ${total_adicionales}")
                c.drawString(100, 690, f"Valor de Reserva: ${valor_reserva}")
                c.drawString(100, 670, f"Total de Factura: ${total_factura}")
                c.save()

                # Establecer la posición del puntero en el inicio del archivo
                buffer.seek(0)

                # Crear una respuesta HTTP con el contenido del PDF adjunto
                response = HttpResponse(buffer, content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename=factura_{id_reserva}.pdf'

                # Redirigir a una URL después de enviar la respuesta
                return response
            except Exception as e:
                # Manejar errores
                return HttpResponse(f"Error al generar la factura: {e}")
        else:
            # Si el usuario no tiene el tipo de usuario adecuado, mostrar un mensaje de alerta
            return render(request, 'error.html', {"message": "usted no tiene permisos para esatr aca ."})    

    else:
        return redirect("/formularios/login/")
   
   
