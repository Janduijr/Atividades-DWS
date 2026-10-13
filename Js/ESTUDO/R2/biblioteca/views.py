from django.shortcuts import render
from .models import Livro

# Create your views here.

def exibir(request):
    livros = Livro.objects.filter().order_by('id')
    context = {
        'livros':livros
    }
    
    return render(request, 'biblioteca/exibir.html', context)