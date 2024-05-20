from django.shortcuts import render, redirect, get_object_or_404
from secretariaEstudiante.models import estudiante, document, curso, sede
from secretariaEstudiante.forms import EstudianteForm
from django.contrib import messages 
# Create your views here.

def estudiente(request):
    estudiantes=estudiante.objects.all()
    documentos=document.objects.all()
    cursos=curso.objects.all()
    sedes=sede.objects.all()
    return render(request, "secretariaEstudiante/estudiante.html", {"estudiantes":estudiantes, "documentos":documentos, "cursos":cursos, "sedes":sedes})

def crearEstudiante(request):
    formulario = EstudianteForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'El registro ha sido guardado exitosamente.')
        return redirect('Estudiante')
    return render(request, 'secretariaEstudiante/createEstudiante.html', {'formulario':formulario})

def editarEstudiante(request, id):
    estudiantes= estudiante.objects.get(idEstudiante=id)
    formulario = EstudianteForm(request.POST or None, request.FILES or None, instance=estudiantes)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        messages.success(request, 'El registro ha sido guardado exitosamente.')
        return redirect('Estudiante')
    return render(request, 'secretariaEstudiante/editarEstudiante.html', {'formulario':formulario})

def eliminarEstudiante(request, id):
    eliminar = get_object_or_404(estudiante, idEstudiante=id)
    if eliminar:
        eliminar.delete()
        return redirect('Estudiante')