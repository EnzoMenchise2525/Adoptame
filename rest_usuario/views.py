from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes # Token
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Usuario
from rest_usuario.serializers import UsuarioSerializer
# permisos de token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))   # autentificación por Token  
def lista_usuarios(request):
    if request.method == 'GET':           # metodo GET
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':       # metodo POST
        data = JSONParser().parse(request)
        serializer = UsuarioSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))  # autentificación por Token
def detalle_usuario(request, id):
    try:
        usuarios = Usuario.objects.get(correo=id)
    except Usuario.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
 
 # metodo GET   
    if request.method == 'GET':
        serializer =  UsuarioSerializer(usuarios)
        return Response(serializer.data)

# metodo PUT    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer =  UsuarioSerializer(usuarios, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    

# metodo DELETE                
    elif request.method == 'DELETE':
        usuarios.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)