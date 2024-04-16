from django.shortcuts import render, redirect, get_object_or_404
from secretariaEstudiante.models import estudiante, document, curso, sede
from secretariaEstudiante.forms import EstudianteForm
# Create your views here.

def estudiente(request):
    estudiantes=estudiante.objects.all()
    documentos=document.objects.all()
    cursos=curso.objects.all()
    sedes=sede.objects.all()
    return render(request, "secretariaEstudiante/estudiante.html", {"estudiantes":estudiantes, "documentos":documentos, "cursos":cursos, "sedes":sedes})

def createEstudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES)
        if form.is_valid():
            # Procesar el formulario
            form.save()
            return redirect('estudiante')
    else:
        form = EstudianteForm()
    
    return render(request, 'secretariaEstudiante/createEstudiante.html', {'form': form})

def editarEstudiante(request, id):
    editar = get_object_or_404(estudiante, idEstudiante=id)
    if request.method == "POST":
        form = EstudianteForm(request.POST, request.FILES, instance=editar)
        if form.is_valid():
            form.save()
            return redirect('Estudiante')
    else:
        form = EstudianteForm(instance=editar)
    return render(request, 'secretariaEstudiante/editarEstudiante.html', {'form': form})

def eliminarEstudiante(request, id):
    eliminar = get_object_or_404(estudiante, idEstudiante=id)
    if eliminar:
        eliminar.delete()
        return redirect('Estudiante')