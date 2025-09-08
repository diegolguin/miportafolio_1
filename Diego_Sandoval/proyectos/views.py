from django.shortcuts import render

def inicio(request):
    return render(request, 'proyectos/inicio.html')

def lista(request):
    proyectos = [
        "Sistema de Ventas",
        "Landing Page",
        "Gestor de Reservas"
    ]
    return render(request, 'proyectos/lista.html', {"proyectos": proyectos})
