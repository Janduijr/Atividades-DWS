from django.shortcuts import render
from .models import Livro

# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all().order_by('id')
    context = {
        'livros':livros
    }
    return render(request, 'biblioteca/listar_livros.html', context)