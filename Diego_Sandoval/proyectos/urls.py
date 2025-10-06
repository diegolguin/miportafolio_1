from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('lista/', views.lista, name='lista'),

    # Clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('editar_cliente/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('eliminar_cliente/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),

    # Productos
    path('productos/', views.lista_productos, name='lista_productos'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:id>/', views.editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', views.eliminar_producto, name='eliminar_producto'),

    # Registro
    path('registro/', views.registrar_usuario, name='registro'),

    # Login y Logout
    path('login/', auth_views.LoginView.as_view(template_name='proyectos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
