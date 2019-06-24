from django.shortcuts import render, redirect
from .models import Cliente, Tecnico, Solicitud, Producto
from Usuarios.models import User

# Create your views here.

def index(request):
    return render(request,'index.html')

def registro(request):
    return render(request,'registro.html')

def perfil(request):
    clientes = Cliente.objects.all()

    contexto = {'clientes':clientes}
    return render(request, 'perfil.html', contexto)

def administrador(request):
    clientes = Cliente.objects.all()
    tecnicos = Tecnico.objects.all()
    solicitudes = Solicitud.objects.all()
    productos = Producto.objects.all()
    usuarios = User.objects.all()

    contexto = {'clientes':clientes, 'tecnicos':tecnicos, 'solicitudes':solicitudes, 'productos':productos, 'usuarios':usuarios}

    return render(request,'administrador.html', contexto)


def crear_cliente(request):
    correo = request.POST.get('correo')
    nombre = request.POST.get('nombre')
    contra = request.POST.get('contra')
    direccion = request.POST.get('direccion')
    telefono = request.POST.get('telefono')
    cli = Cliente(correo = correo, nombre = nombre, direccion = direccion, telefono = telefono)
    cli.save()
    us = User.objects.create_user(email = correo, password = contra, tipo='cli', rut = '0')
    us.save()
    return redirect('Usuarios:log')

def crear_solicitud(request):
    nombre = request.POST.get('nombre')
    email = request.POST.get('correo')
    direccion = request.POST.get('direccion')
    mensaje = request.POST.get('mensaje')
    sl = Solicitud(nombre=nombre, email=email, direccion=direccion, mensaje=mensaje)
    sl.save()

    return redirect('perfil')