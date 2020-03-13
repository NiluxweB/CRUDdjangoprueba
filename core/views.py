from django.shortcuts import render
from .models import Persona, Genero
from datetime import datetime, time

# Create your views here.

def index(request):

    return render(request, 'core/index.html')

def listarpersona(request):
    persona = Persona.objects.all()
    data = {
        'persona':persona
    }
    return render(request, 'core/index.html', data)

def agregarpersona(request):
    if request.POST:
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        direccion = request.POST.get("direccion")
        telefono = request.POST.get("telefono")
        fecha_nacimiento = request.POST.get("fecha_nacimiento")
        genero = request.POST.get("genero")
        form = agregarpersona(nombre=nombre, apellido=apellido, direccion=direccion, telefono=telefono, fecha_nacimiento=fecha_nacimiento, genero=genero)
        form.save()

    return render(request, 'core/index.html')