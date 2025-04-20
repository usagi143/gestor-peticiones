from django import forms
from . import models

class Peticion(forms.Form):
    nombre = forms.CharField(label="user_name", max_length=100)
    edad = forms.IntegerField(label="edad")

