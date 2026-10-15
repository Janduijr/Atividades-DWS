from django.shortcuts import render, get_object_or_404
from .models import Evento, Local

# Create your views here.

def index(request):
    eventos = Evento.objects.all()
    context = {
        'eventos':eventos
    }
    return render(request, 'agenda/index.html', context)

def detalhe(request, id):
    evento = get_object_or_404(Evento, id=id)
    context = {
        'evento':evento
    }
    return render(request, 'agenda/detalhe.html', context)

def local(request, id):
    local = get_object_or_404(Local, id=id)
    context = {
        'local': local
    }
    return render(request, 'agenda/local.html', context)