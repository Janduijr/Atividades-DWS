from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=120)
    ano = models.IntegerField()
    disponivel = models.BooleanField()
    
    def __str__(self):
        return self.titulo
