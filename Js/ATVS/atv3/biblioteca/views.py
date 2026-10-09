from django.shortcuts import render
from .models import Livro, Autor
from django.shortcuts import get_list_or_404


# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all().order_by('id')
    context = {
        'livros':livros
    }
    return render(request, 'biblioteca/listar_livros.html', context)

def autor_detalhe(request, autor_id):
    livros = get_list_or_404(Livro, autor__id=autor_id)
    autor = Autor.objects.get(id=autor_id)
    context = {
        'livros': livros,
        'autor': autor
    }
    return render(request, 'biblioteca/autor_detalhe.html', context)