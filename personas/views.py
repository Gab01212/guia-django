from django.shortcuts import render
from django.http import HttpResponse

def lista_personas(request):
    return HttpResponse("<h1 Directorio de Personas</h1>")

def perfil_persona(request):
    return HttpResponse("<h1 Perfil detallado de la persona</h1>")
