from unittest import loader
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Bienvenidos a mi blog personal")

def inicio(request):
    template = loader.get_template('Inicio.html')

    plantilla_generada = template.render({})

    return HttpResponse(plantilla_generada)