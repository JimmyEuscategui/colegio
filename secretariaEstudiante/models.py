from django.db import models

# Create your models here.

class document(models.Model):
    idTipo = models.AutoField(primary_key=True) #Especificar que este campo es la primaryKey de la tabla o el id
    documento = models.CharField(max_length=50)
    
    def __str__(self):
        return self.documento

class sede(models.Model):
    idSede = models.AutoField(primary_key=True)
    sede = models.CharField(max_length=30)
    
    def __str__(self):
        return self.sede

class curso(models.Model):
    idCurso = models.AutoField(primary_key=True)
    curso = models.CharField(max_length=30)
    
    def __str__(self):
        return self.curso

class estudiante(models.Model):
    idEstudiante = models.AutoField(primary_key=True)
    primerNombre = models.CharField(max_length=20)
    segundoNombre = models.CharField(max_length=20, blank=True, null=True)
    primerApellido = models.CharField(max_length=20)
    segundoApellido = models.CharField(max_length=20)
    idCurso = models.ForeignKey(curso, on_delete=models.SET_NULL, null=True)
    idTipo = models.ForeignKey(document, on_delete=models.SET_NULL, null=True)
    documento = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    telefono = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='secretariaEstudiante') #lo que va en la comillas es a donde va guardada la imagen
    idSede = models.ForeignKey(sede, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    class meta:
        verbose_name="estudiante"
        verbose_name_plural="estudiantes"
        
    def __str__(self):
        return self.primerNombre
    
