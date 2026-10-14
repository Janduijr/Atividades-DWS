from django.shortcuts import render
from .models import Livro, Autor
from django.shortcuts import get_object_or_404
from .forms import LivroForms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def exibir(request):
    livros = Livro.objects.filter().order_by('id')
    context = {
        'livros':livros
    }
    
    return render(request, 'biblioteca/exibir.html', context)

def autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    livros = autor.books.all()
    
    context = {
        'autor':autor,
        'livros':livros,
    }
    return render(request, 'biblioteca/autor.html', context)

def adicionar(requeest):
    if requeest.method == 'POST':
        form = LivroForms(requeest.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('exibir'))
    
    else:
        form = LivroForms()
    
    context = {
        'form':form
    }
    return render(requeest, 'biblioteca/forms.html', context)