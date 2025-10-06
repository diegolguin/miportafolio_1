from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import ClienteForm, ProductoForm

def inicio(request):
    return render(request, 'proyectos/inicio.html')

# 👇 Aquí agregamos la nueva función lista
from django.contrib.auth.decorators import login_required 
@login_required
def lista(request):
    proyectos = [
        {"nombre": "Sistema de Ventas", "url": "lista_productos"},
        {"nombre": "Gestión de Clientes", "url": "lista_clientes"},
        {"nombre": "Inventario", "url": "lista_productos"},
    ]
    return render(request, 'proyectos/lista.html', {'proyectos': proyectos})
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'proyectos/lista_clientes.html', {'clientes': clientes})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'proyectos/lista_productos.html', {'productos': productos})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'proyectos/agregar_cliente.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
    return render(request, 'proyectos/agregar_producto.html', {'form': form})
from django.shortcuts import render, redirect
from .forms import RegistroForm

def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()  # crea el usuario
            return redirect('login')  # redirige al login
    else:
        form = RegistroForm()
    return render(request, 'proyectos/registro.html', {'form': form})
# ✏️ Editar cliente
def editar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'proyectos/editar_cliente.html', {'form': form})

# ✏️ Editar producto
def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'proyectos/editar_producto.html', {'form': form})
# 🗑️ Eliminar cliente
def eliminar_cliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('lista_clientes')

# 🗑️ Eliminar producto
def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('lista_productos')
