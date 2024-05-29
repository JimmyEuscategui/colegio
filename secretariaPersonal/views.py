from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from secretariaPersonal.models import Personal, Cargo
from django.contrib import messages
from .forms import PersonalForm

# Create your views here.

def personal(request):
    personales=Personal.objects.all()
    cargo=Cargo.objects.all()
    return render(request, "secretariaPersonal/personal.html", {"personales":personales, "cargo":cargo})

def registrarPersonal(request):
    if request.method == 'POST':
        personal_form = PersonalForm(request.POST or None, request.FILES or None)
        if personal_form.is_valid():
            personal_form.save()
            return redirect('Personal')
        else:
            # Añade un mensaje de error para depuración
            print("Errores en el formulario:", personal_form.errors)
            print("Datos enviados:", request.POST)
    else:
        personal_form = PersonalForm()
    return render(request, "secretariaPersonal/registrarPersonal.html", {'personal_form': personal_form})



def editarPersonal(request, id):
    personal = get_object_or_404(Personal, idPersonal=id)
    if request.method == 'POST':
        personal_form = PersonalForm(request.POST or None, request.FILES or None, instance=personal)
        if personal_form.is_valid():
            personal_form.save()
            return redirect('Personal')
    else:
        personal_form = PersonalForm(instance=personal)
    return render(request, "secretariaPersonal/registrarPersonal.html", {'personal_form': personal_form})


def eliminarPersonal(request, id):
    personal = get_object_or_404(Personal, idPersonal=id)
     
    if personal:
        personal.delete()
    return redirect('Personal')