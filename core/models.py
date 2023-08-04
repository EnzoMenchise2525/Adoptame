from django.db import models

# Create your models here.
class Usuario(models.Model):
    correo= models.CharField(primary_key=True, max_length=30, verbose_name='Correo usuario')
    nombre= models.CharField(max_length=60, verbose_name='Nombre usuario')
    telefono= models.IntegerField(verbose_name='Numero telefono')
    password= models.CharField(max_length=12, verbose_name='Password usuario')
    
    def __str__(self):
        return self.nombre
        