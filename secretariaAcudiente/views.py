from django.shortcuts import render, get_object_or_404, redirect
from .models import Acudiente
from .forms import AcudienteForm

# Create your views here.
 
def acudiente(request):
    acudiente = Acudiente.objects.all()
    return render(request, "secretariaAcudiente/acudiente.html", {'acudiente': acudiente})

def acudiente_detalle(request, acudiente_id):
    acudiente = get_object_or_404(Acudiente, idAcudiente=acudiente_id)
    estudiantes = acudiente.estudiantes.all()  # Utiliza el related_name definido
    return render(request, 'secretariaAcudiente/acudiente.html', {'acudiente': acudiente, 'estudiantes': estudiantes})

def registrarAcudiente(request):
    if request.method == 'POST':
        acudiente_form = AcudienteForm(request.POST or None, request.FILES or None)
        if acudiente_form.is_valid():
            acudiente_form.save()
            return redirect('Acudiente')
        else:
            print("Errores en el formulario:", acudiente_form.errors)
            print("Datos envíados:", request.POST)
    else:
        acudiente_form = AcudienteForm()
    return render(request, "secretariaAcudiente/registrarAcudiente.html", {'acudiente_form':acudiente_form})

def editarAcudiente(request, id):
    acudiente = get_object_or_404(Acudiente, idAcudiente=id)
    if request.method == 'POST':
        acudiente_form =AcudienteForm(request.POST or None, request.FILES or None, instance=acudiente)
        if acudiente_form.is_valid():
            acudiente_form.save()
            return redirect('Acudiente')
    else:
        acudiente_form = AcudienteForm(instance=acudiente)
    return render(request, "secretariaAcudiente/registrarAcudiente.html", {'acudiente_form':acudiente_form})

def eliminarAcudiente(request, id):
    acudiente = get_object_or_404(Acudiente, idAcudiente=id)
    if acudiente:
        acudiente.delete()
    return redirect('Acudiente')
    