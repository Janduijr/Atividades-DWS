from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100, null=False)
    nacionalidade = models.CharField(max_length=50)
    
    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Autores'
    
    def __str__(self):
        return self.nome
    
    
class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='books')
    ano = models.IntegerField()
    disponivel = models.BooleanField()
    categoria = models.ManyToManyField(Categoria)
    
    def __str__(self):
        return self.titulo
