from rest_framework import serializers
from core.models import Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields =['correo','nombre','telefono','password']