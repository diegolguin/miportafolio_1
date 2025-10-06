from django import forms
from .models import Cliente, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']  # usa "email" como en models.py

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio']  # deja solo los campos que existen en models.py

# 🔽 Formulario de registro de usuarios
class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico'})
    )

    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Clave (mínimo 6 caracteres)'}),
        min_length=6
    )

    password2 = forms.CharField(
        label="Confirmar contraseña",
        widget=forms.PasswordInput(attrs={'placeholder': 'Repite la clave'}),
        min_length=6
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
        }
