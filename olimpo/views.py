import random
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from apia.models import *
from django.http import HttpResponse
import psycopg2  # Cambiado de mysql.connector a psycopg2
from datetime import datetime
from random import choice
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'index.html')

def admin(request):
    if request.user.is_authenticated:
        empleado = empleados.objects.get(cc_usu=request.user)
       
        if empleado.codigo_usu_id == 'Administrador':
            return render(request, 'admin.html')
        else:
            return render(request, 'error.html', {"message": "Usted no tiene permisos para estar aquí."})    
    else:
        return redirect("/formularios/login/")

def reservaC(request):
    documen = request.POST.get("numero_doc")
    fecha_inicial = request.POST.get("fecha_in")
    fecha_final = request.POST.get("fecha_fi")
    tipo_H = tipo_habitacion.objects.all()

    try:
        # Cambia la conexión de MySQL a PostgreSQL
        conexion = psycopg2.connect(
            host="localhost",
            user="your_user",  # Cambia esto a tu usuario de PostgreSQL
            password="your_password",  # Cambia esto a tu contraseña de PostgreSQL
            dbname="olimpo_1"  # Cambia esto al nombre de tu base de datos en PostgreSQL
        )
        cursor = conexion.cursor()

        cursor.execute("SELECT nombre, correo FROM apia_cliente WHERE numero_doc = %s", (documen,))
        clientes = cursor.fetchall()

        cursor.close()
        conexion.close()

        if clientes:
            nombre1, correo1 = clientes[0]
        else:
            nombre1, correo1 = "", ""
            print("No se encontraron clientes con el número de documento proporcionado.")
            return render(request, 'error.html', {"message": "No se encontró ninguna persona con el número de documento proporcionado."})

        return render(request, 'reservacliente.html', {
            "tipo": tipo_H,
            "documento": documen,
            "NombreC": nombre1,
            "correoC": correo1,
            "fecha_ini": fecha_inicial,
            "fecha_fin": fecha_final,
        })

    except psycopg2.Error as err:
        print("Error al conectar a la base de datos:", err)
        return render(request, 'error.html', {"message": "Error al conectar a la base de datos."})

def crearReservaRes_clien(request, documento, fecha_ini, fecha_fin):
    tipo_h = request.POST.get("tipo")
    estado_res_pos = "Activo"
    estado_habitacion = "Disponible"
    estado_habitacion_res = "Reservada"
    habitaciones = habitacion.objects.filter(tipo_id=tipo_h, estado_id=estado_habitacion)

    if habitaciones.exists():
        habitacion_seleccionada = choice(habitaciones)

        nueva_reserva = reserva.objects.create(
            fecah_ini=fecha_ini,
            fecah_fin=fecha_fin,
            valor_reserva=habitacion_seleccionada.valor_habitacion,
            habitacion_id=habitacion_seleccionada.numero_H,
            numero_doc_id=documento,
            estado_res_id=estado_res_pos
        )
        valor = habitacion_seleccionada.valor_habitacion

        fecha_inicial = datetime.strptime(fecha_ini, "%Y-%m-%d")
        fecha_final = datetime.strptime(fecha_fin, "%Y-%m-%d")
        diferencia = fecha_final - fecha_inicial
        resultado = diferencia.days * valor

        habitacion_seleccionada.estado_id = estado_habitacion_res
        habitacion_seleccionada.save()

        # Establecer la conexión con PostgreSQL
        conexion = psycopg2.connect(
            host="localhost",
            user="your_user",
            password="your_password",
            dbname="olimpo_1"
        )
        cursor = conexion.cursor()

        consulta = """
            SELECT max(id_reserva), valor_reserva FROM apia_reserva WHERE numero_doc_id = %s AND estado_res_id = %s
        """
        cursor.execute(consulta, (documento, 'Activo'))

        resultados = cursor.fetchall()

        for resultado in resultados:
            id_res = resultado[0]
            valor_res = resultado[1]

        cursor.close()
        conexion.close()

        conexion = psycopg2.connect(
            host="localhost",
            user="your_user",
            password="your_password",
            dbname="olimpo_1"
        )
        cursor = conexion.cursor()

        cursor.execute("SELECT nombre, correo FROM apia_cliente WHERE numero_doc = %s", (documento,))
        clientes = cursor.fetchall()

        cursor.close()
        conexion.close()

        if clientes:
            nombre1, correo1 = clientes[0]

        return render(request, 'reservacliente_info_res.html', {
            "tipo": tipo_h,
            "documento": documento,
            "NombreC": nombre1,
            "correoC": correo1,
            "fecha_ini": fecha_inicial,
            "fecha_fin": fecha_final,
            "id_res": id_res,
            "valor": valor_res
        })
    else:
        return render(request, 'error.html', {"message": "No hay habitaciones disponibles para el tipo especificado."})

def pdfres(request, id_res):
    # Establecer la conexión con PostgreSQL
    conexion = psycopg2.connect(
        host="localhost",
        user="your_user",
        password="your_password",
        dbname="olimpo_1"
    )
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM apia_reserva WHERE id_reserva = %s", (id_res,))
    clientes = cursor.fetchall()

    cursor.close()
    conexion.close()

    if clientes:
        id_res = clientes[0][0]
        fecah_ini = clientes[0][1]
        fecah_fin = clientes[0][2]
        valor_reserva = clientes[0][3]
        habitacion_id = clientes[0][5]
        numero_doc_id = clientes[0][6]

        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        c.drawString(100, 750, "Su reserva")
        c.drawString(100, 730, f"ID de Reserva: {id_res}")
        c.drawString(100, 710, f"Fecha de inicio: {fecah_ini}")
        c.drawString(100, 690, f"Fecha de final: {fecah_fin}")
        c.drawString(100, 670, f"Valor de su reserva: {valor_reserva}")
        c.drawString(100, 650, f"Su número de habitación: {habitacion_id}")
        c.drawString(100, 630, f"Su número de documento: {numero_doc_id}")
        c.save()

        buffer.seek(0)

        response = HttpResponse(buffer, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename=reserva_olimpo{id_res}.pdf'

        return response
    else:
        return HttpResponse("No se encontró la reserva especificada.")
