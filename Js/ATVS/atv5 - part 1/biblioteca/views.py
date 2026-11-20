from django.shortcuts import render, redirect
from .models import Livro, Autor
from django.shortcuts import get_list_or_404, get_object_or_404
from .forms import AutorForms, LivroForms
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

class listar_livros_view(generic.ListView):
    template_name = 'biblioteca/listar_livros.html'
    context_object_name = 'livros'
    
    def get_queryset(self):
        return Livro.objects.all().order_by('titulo')


class criar_autor_view(generic.CreateView):
    model = Livro
    form_class = AutorForms
    template_name = 'biblioteca/criar_autor.html'
    success_url = reverse_lazy('listar_livros')


class criarlivroView(generic.CreateView):
    model = Livro
    form_class = LivroForms
    template_name = 'biblioteca/livro.html'
    success_url = reverse_lazy('listar_livros')

class editarlivroView(generic.UpdateView):
    model = Livro
    form_class = LivroForms
    template_name = 'biblioteca/livro.html'
    success_url = reverse_lazy('listar_livros')

class autor_detalhe_view(generic.DetailView):
    model = Autor
    template_name = 'biblioteca/autor_detalhe.html'
    pk_url_kwarg = 'autor_id'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['livros'] = Livro.objects.filter(autor=self.object)
        return context

class ExcluirLivroView(generic.DeleteView):
    model = Livro
    template_name = 'biblioteca/livro_deletar.html'
    context_object_name = 'livro'
    success_url = reverse_lazy('listar_livros')

class SobreView(generic.TemplateView):
    template_name = 'biblioteca/sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Livro.objects.count()
        context['disponiveis'] = Livro.objects.filter(disponivel=True).count()
        return context
