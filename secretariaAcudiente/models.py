from django.db import models
from secretariaEstudiante.models import document

# Create your models here.

class Acudiente(models.Model):
    idAcudiente = models.AutoField(primary_key=True)
    primerNombre = models.CharField(max_length=20)
    segundoNombre = models.CharField(max_length=20, blank=True, null=True)
    primerApellido = models.CharField(max_length=20)
    segundoApellido = models.CharField(max_length=20)
    idTipo = models.ForeignKey(document, on_delete=models.SET_NULL, null=True)
    documento = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='secretariaAcudiente', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class meta:
        verbose_name="acudiente"
        verbose_name_plural="acudientes"
        
    def __str__(self):
        return self.primerNombre