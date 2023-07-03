from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VehiculoForm(forms.ModelForm):
    class Meta:
        model=VehiculoModel#el nombre de la tabla dentro de la db (obtenido de models.py)
        fields="__all__"#se guardan todos los campos