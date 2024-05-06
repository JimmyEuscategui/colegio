from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "secretaria/home.html")

def personal(request):
    return render(request, "secretaria/personal.html")

def acudiente(request):
    return render(request, "secretaria/acudiente.html")