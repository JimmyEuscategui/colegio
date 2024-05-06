from django.forms import ModelForm
from django import forms
from .models import estudiante

class EstudianteForm(ModelForm):
    class Meta:
        model = estudiante
        fields = '__all__'