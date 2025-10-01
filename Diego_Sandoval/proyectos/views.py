from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import ClienteForm, ProductoForm

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

