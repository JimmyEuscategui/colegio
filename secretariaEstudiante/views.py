from django.shortcuts import render
from secretariaEstudiante.models import estudiante, document, curso, sede
# Create your views here.

def estudiente(request):
    estudiantes=estudiante.objects.all()
    documentos=document.objects.all()
    cursos=curso.objects.all()
    sedes=sede.objects.all()
    return render(request, "secretariaEstudiante/estudiante.html", {"estudiantes":estudiantes, "documentos":documentos, "cursos":cursos, "sedes":sedes})
