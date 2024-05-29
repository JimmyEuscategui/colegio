from django.db import models
from secretariaEstudiante.models import sede, document

# Create your models here.

class Cargo(models.Model):
    idCargo = models.AutoField(primary_key=True) #Especificar que este campo es la primaryKey de la tabla o el id
    cargo = models.CharField(max_length=50)
    
    def __str__(self):
        return self.cargo
    
class Personal(models.Model):
    idPersonal = models.AutoField(primary_key=True)
    primerNombre = models.CharField(max_length=20)
    segundoNombre = models.CharField(max_length=20, blank=True, null=True)
    primerApellido = models.CharField(max_length=20)
    segundoApellido = models.CharField(max_length=20)
    idTipo = models.ForeignKey(document, on_delete=models.SET_NULL, null=True)
    documento = models.CharField(max_length=20)
    idCargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)
    especialidad = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='secretariaPersonal') #lo que va en la comillas es a donde va guardada la imagen
    idSede = models.ForeignKey(sede, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name="personal"
        verbose_name_plural="personales"
        
    def __str__(self):
        return self.primerNombre