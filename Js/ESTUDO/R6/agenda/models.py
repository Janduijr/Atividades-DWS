from django.db import models

# Create your models here.

class Local(models.Model):
    nome = models.CharField(unique=True)
    endereco = models.CharField()
    capacidade = models.PositiveIntegerField()
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(unique=True)
    
    class Meta:
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField()
    descricao = models.TextField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    criado = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, related_name='eventos')
    categoria = models.ManyToManyField(Categoria, null=True, blank=True)

    class Meta:
        ordering = ['inicio']

    def __str__(self):
        return self.titulo
    
    def vagas_restantes(self):
        return self.local.capacidade - self.relatorios.presentes


class Atividade(models.Model):
    titulo = models.CharField()
    palestrante = models.CharField()
    horario = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='atividades')
    
    class Meta:
        ordering = ['horario']

    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    nome = models.CharField()
    email = models.EmailField()
    inscrito = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
    
    def __str__(self):
        return self.nome

class Relatorio(models.Model):
    presentes = models.PositiveIntegerField()
    observacoes = models.TextField(null=True, blank=True)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE, related_name='relatorios')

    def __str__(self):
        return f'Relatorio({self.id})'






