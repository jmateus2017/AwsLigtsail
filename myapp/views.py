# myapp/views.py

from django.shortcuts import render
from django.http import HttpResponse # Importa HttpResponse

def home_view(request):
    return HttpResponse("<h1>¡Hola Aplicación DjangoLightsail!</h1>")