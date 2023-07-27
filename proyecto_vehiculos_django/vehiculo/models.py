from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class VehiculoModel(models.Model):
    marcas= [
        ('fiat', 'Fiat'),
        ('chevrolet', 'Chevrolet'),
        ('ford', 'Ford'),
        ('toyota', 'Toyota'),
    ]
    categorias= [
        ('particular', 'Particular'),
        ('transporte', 'Transporte'),
        ('carga', 'Carga'),
    ]
    marca=models.CharField(choices=marcas,max_length=20,default='ford')
    modelo=models.CharField(max_length=100)
    serial_carroceria=models.CharField(max_length=50)
    serial_motor=models.CharField(max_length=50)
    categoria=models.CharField(choices=categorias,max_length=20,default='particular')
    precio=models.IntegerField()
    creado=models.DateTimeField(auto_now_add=True)
    modificado=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.modelo