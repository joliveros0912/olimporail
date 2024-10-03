import hashlib
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import registrocliente, loginclientes
from django.contrib.auth import authenticate, login, logout
from apia.models import cliente, empleados
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required





# Create your views here.

def registro(request):
    if request.method == "POST":
        cliente_form = registrocliente(request.POST)
        if cliente_form.is_valid():
            numero_doc = cliente_form.cleaned_data.get('numero_doc')
            if cliente.objects.filter(numero_doc=numero_doc).exists():
                return HttpResponse('<script>alert("Ya hay un usuario con el mismo documento"); window.location="/formularios/login/";</script>')
            if empleados.objects.filter(cc_usu=numero_doc).exists():
                return HttpResponse('<script>alert("Usted es un empleado"); window.location="/formularios/login/";</script>')
            else:
                contrasenaaC = cliente_form.cleaned_data.get('contrasenaaC')
                h = hashlib.sha256()
                h.update(contrasenaaC.encode())
                password_hash = h.hexdigest()
                nuevo_cliente = cliente_form.save(commit=False) 
                nuevo_cliente.contrasenaaC = password_hash
                nuevo_cliente.save()
                cliente_form.save()
                return redirect("/")
    else:
        cliente_form = registrocliente()

    return render(request, "registro.html", {'form': cliente_form})


def authenticate_cliente(numero_doc=None, password=None):
    try:
        cliente_obj = cliente.objects.get(numero_doc=numero_doc)
        h = hashlib.sha256()
        h.update(password.encode())
        password_hash = h.hexdigest()

        if password_hash == cliente_obj.contrasenaaC:
            return cliente_obj
    except cliente.DoesNotExist:
        pass
    return None

def authenticate_empleado(numero_doc_e=None, password_e=None, tipo = None):
    try:
        empleado_obj = empleados.objects.get(cc_usu=numero_doc_e)

        if check_password(password_e, empleado_obj.password):
            return empleado_obj
    except empleados.DoesNotExist:
        pass
    return None

def inicio(request):
    if request.method == "POST":
        print("a")
        documento1 = request.POST.get("numero_doc")  
        password1 = request.POST.get("contrasenaaC")  
        tipo_usu = request.POST.get("tipo_usuario")
        
        print("Documento ingresado:", documento1)  
        print("Contraseña ingresada:", password1)  
        print("tipo usuario:", tipo_usu)


        if tipo_usu == "cliente":
            print("cliente tall1")
            user = authenticate_cliente(numero_doc=documento1, password=password1)
            if user is not None:
                user_au = True
                login(request, user)
                print("Autenticación exitosa")
                print(request.user)
                nombre_usuario = user.nombre
                print(nombre_usuario)
                return render(request, "index.html", {"user_au": user_au, "name": nombre_usuario})
            else:
                return HttpResponse('<script>alert("Credenciales Incorrectas"); window.location="/formularios/login/";</script>')


        elif tipo_usu == "Administrador":
            empleado = authenticate_empleado(numero_doc_e=documento1, password_e=password1)
            if empleado is not None:
                login(request, empleado)
                print("autenticacion correcta empleado")
                return redirect("/administrador/")
            else:
                return HttpResponse('<script>alert("Credenciales Incorrectas"); window.location="/formularios/login/";</script>')
            
        elif tipo_usu == "resepcionista":

            empleado = authenticate_empleado(numero_doc_e=documento1, password_e=password1)
            if empleado is not None:
                login(request, empleado)
                print("autenticacion correcta empleado")
                return redirect( "/recepcionista/recepcionista/")
            else:
                return HttpResponse('<script>alert("Credenciales Incorrectas"); window.location="/formularios/login/";</script>')
        
        elif tipo_usu == "ama_de_llaves":
            empleado = authenticate_empleado(numero_doc_e=documento1, password_e=password1)
            if empleado is not None:
                login(request, empleado)
                print("autenticacion correcta empleado")
                return redirect("/amadellaves/accionamadellaves/")
            else:
                return HttpResponse('<script>alert("Credenciales Incorrectas"); window.location="/formularios/login/";</script>')

        elif tipo_usu == "camarero" or "room_service":
            empleado = authenticate_empleado(numero_doc_e=documento1, password_e=password1)
            if empleado is not None:
                login(request, empleado)
                print("autenticacion correcta empleado")
                return redirect( "/adicionales/meseros/")
            else:
                return HttpResponse('<script>alert("Credenciales Incorrectas"); window.location="/formularios/login/";</script>')

        else:
            print("Credenciales inválidas")

    return redirect('login/')


    
def mostrarinicio(request):
    loginc = loginclientes(request.POST)
    return render(request, 'login.html', {'form': loginc})

def cerrar_sesion(request):
    logout(request)
    return redirect('/')

