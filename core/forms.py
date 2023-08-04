from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from .models import Usuario

#clase para el formulario desde la bd
class UsuarioForm(ModelForm):
    correo = forms.EmailField()
    password = forms.CharField(max_length=12, label='password', widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields =['correo','nombre','telefono','password']

class IniciarSesionForm(ModelForm):
    correo = forms.EmailField()
    password = forms.CharField(max_length=12, label='password', widget=forms.PasswordInput())
    class Meta:
        model = Usuario
        fields =['correo','password']
    