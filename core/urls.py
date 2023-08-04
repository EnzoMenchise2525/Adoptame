from unicodedata import name
from django.urls import path,include
from .views import index
from .views import formUsuario,adminUsuarios,formModUsuario,formElimUsuario
from .views import comida,cosas_gatos,cosas_perros,formulario_de_contacto,gato,iniciar_sesion,perro,usuario,veterinario
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', index, name="index"),
    path('formUsuario', formUsuario, name="formUsuario"),
    path('adminUsuarios', adminUsuarios, name="adminUsuarios"),
    path('formModUsuario/<id>', formModUsuario, name="formModUsuario"),
    path('formElimUsuario/<id>', formElimUsuario, name="formElimUsuario"),
    #path('api', api, name="api"),
    path('comida', comida, name="comida"),
    path('cosas_gatos',cosas_gatos , name="cosas_gatos"),
    path('cosas_perros',cosas_perros , name="cosas_perros"),
    path('formulario_de_contacto',formulario_de_contacto, name="formulario_de_contacto"),
    path('gato',gato , name="gato"),
    path('iniciar_sesion',iniciar_sesion , name="iniciar_sesion"),
    path('perro',perro , name="perro"),
    path('usuario',usuario , name="usuario"),
    path('veterinario',veterinario , name="veterinario"),
    path('accounts/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name="iniciar_sesion")),
    path('logout', LogoutView.as_view()),
  
]