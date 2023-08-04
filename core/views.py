
from django.shortcuts import render, redirect

from core.forms import UsuarioForm
from .models import Usuario


# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def adminUsuarios(request):
    usuarios = Usuario.objects.all()
    datos={
        'usuarios': usuarios
    }
    return render(request, 'core/adminUsuarios.html', datos)

def formUsuario(request):
    datos = {
        'form': UsuarioForm()
    }
    if request.method=='POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Guardado correctamente"
    return render(request, 'core/formUsuario.html', datos)
    
def formModUsuario(request, id):
    usuario = Usuario.objects.get(correo=id)
    datos = {
        'form': UsuarioForm(instance=usuario)
    }
    if request.method=='POST':
        formulario = UsuarioForm(data=request.POST, instance=usuario)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje']="Modificado correctamente"
    return render(request, 'core/formModUsuario.html', datos)


def formElimUsuario(request, id):
    usuario = Usuario.objects.get(correo=id)
    usuario.delete()
    return redirect(to="adminUsuarios")


#crear vistas

def agendar_hora(request):
    return render(request, 'core/agendar hora.html')

def comida(request):
    return render(request, 'core/comida.html')

def cosas_gatos(request):
    return render(request, 'core/cosas_gatos.html')

def cosas_perros(request):
    return render(request, 'core/cosas_perros.html')

def api(request):
    return render(request, 'core/api.html')

def formulario_de_contacto(request):
    return render(request, 'core/formulario_de_contacto.html')  #

def gato(request):
    return render(request, 'core/gato.html')

def iniciar_sesion(request):
    return render(request, 'core/iniciar_sesion.html')

def perro(request):
    return render(request, 'core/perro.html')

def usuario(request):
    return render(request, 'core/usuario.html')

def veterinario(request):
    return render(request, 'core/veterinario.html')

