from django.shortcuts import render, redirect
from .models import Livro, Autor
from django.shortcuts import get_list_or_404, get_object_or_404
from .forms import AutorForms, LivroForms

# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all().order_by('id')
    context = {
        'livros':livros
    }
    return render(request, 'biblioteca/listar_livros.html', context)

def criar_autor(request):
    if request.method == 'POST':
        form = AutorForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = AutorForms()
    
    context = {
        'form': form
    }
    return render(request, 'biblioteca/criar_autor.html', context)

def livro(request, pk=None):
    
    if pk:
        livro = get_object_or_404(Livro, pk=pk)
    else:
        livro = None
    
    if request.method == 'POST':
        form = LivroForms(request.POST, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('listar_livros')
    else:
        form = LivroForms(instance=livro)
    
    context = {
        'form': form,
        'livro':livro
    }
    return render(request, 'biblioteca/livro.html', context)

def autor_detalhe(request, autor_id):
    livros = get_list_or_404(Livro, autor__id=autor_id)
    autor = Autor.objects.get(id=autor_id)
    context = {
        'livros': livros,
        'autor': autor
    }
    return render(request, 'biblioteca/autor_detalhe.html', context)