from django.db import models

# Create your models here.

class Autor(models.Model):
    nome = models.CharField(max_length=50, null=False)
    nacionalidade = models.CharField(max_length=50)
    
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
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="books")
    ano_publicado = models.IntegerField()
    disponivel = models.BooleanField(default=False)
    categoria = models.ManyToManyField(Categoria, blank=True)
    
    def __str__(self):
        return self.titulo