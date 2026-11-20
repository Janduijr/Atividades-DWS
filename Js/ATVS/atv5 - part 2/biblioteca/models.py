from django.db import models
from django.core.validators import MinLengthValidator, FileExtensionValidator
from .validators import validate_ano, validade_paginas, validade_isbn, validade_tamanho

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=50, null=False)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.nome
        
    class Meta:
        verbose_name_plural = 'Autores'
        ordering = ['nome']
        
    
class Categoria(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.nome
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="books")
    ano_publicado = models.IntegerField(validators=[validate_ano])
    disponivel = models.BooleanField(default=False)
    categoria = models.ManyToManyField(Categoria, blank=True)
    paginas = models.PositiveIntegerField(null=True, blank=True, validators=[validade_paginas])
    isbn = models.CharField(null=True, blank=True, validators=[validade_isbn])
    capa = models.ImageField('imagem', upload_to='livros/', blank=True, validators=[FileExtensionValidator(['jpeg','png','jpg']), validade_tamanho])
    
    def __str__(self):
        return self.titulo