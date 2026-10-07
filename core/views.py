from django.shortcuts import render, redirect, get_object_or_404
from solucion import decidir
from .models import Registro
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from functools import wraps
from django.contrib.auth.decorators import login_required

def tiene_rol(user, *roles):
    return user.groups.filter(name__in=roles).exists() or user.is_superuser

def requiere_rol(*roles):
    def decorador(view_func):
        @wraps(view_func)
        @login_required(login_url="login")
        def wrapper(request, *args, **kwargs):
            if tiene_rol(request.user, *roles):
                return view_func(request, *args, **kwargs)
            messages.error(request, "No tienes permiso para esta accion.")
            return redirect("lista")
        return wrapper
    return decorador

@login_required(login_url="login")
def lista(request):
    registros = Registro.objects.filter(eliminado=False)
    return render(request, "lista.html", {"registros": registros})

@requiere_rol("admin", "normal")
def crear(request):
    error = None
    if request.method == "POST":
        nombre = request.POST.get("nombre", "").strip()
        try:
            edad = int(request.POST.get("edad", ""))
            cupos = int(request.POST.get("cupos", ""))

        except ValueError:
            error = "La edad y los cupos deben ser numeros enteros."
        else:
            estado, motivo = decidir(edad, cupos, nombre)
            Registro.objects.create(nombre=nombre, edad=edad, cupos=cupos, estado=estado, motivo=motivo)
            return redirect("lista")
    
    return render(request, "form.html", {"accion": "Crear", "error": error})

@requiere_rol("admin")
def editar(request, pk):
    reg = get_object_or_404(Registro, pk=pk, eliminado=False)
    error = None
    if request.method == "POST":
        reg.nombre = request.POST.get("nombre", "").strip()
        try:
            reg.edad = int(request.POST.get("edad", ""))
            reg.cupos = int(request.POST.get("cupos", ""))

            reg.estado, reg.motivo = decidir(reg.edad, reg.cupos, reg.nombre)
            reg.save()
            return redirect("lista")
        except ValueError:
            error = "La edad y los cupos deben ser numeros enteros."
    return render(request, "form.html", {"accion": "Editar", "registro": reg, "error": error})

@requiere_rol("admin")
def eliminar(request, pk):
    reg = get_object_or_404(Registro, pk=pk, eliminado=False)
    if request.method == "POST":
        reg.soft_delete()
        return redirect("lista")
    return render(request, "confirmar.html", {"registro": reg})

def vista_login(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username", "").strip(),
            password=request.POST.get("password", "")
        )
        if user:
            login(request, user)
            return redirect("lista")
        messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "login.html")

def vista_logout(request):
    logout(request)
    return redirect("login")
    

    
