from django.db import models

# Create your models here.

class Local(models.Model):
    nome = models.CharField(max_length=200, unique=True)
    endereco = models.CharField(max_length=200)
    capacidade = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    criando = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, related_name='eventos')
    categoria = models.ManyToManyField(Categoria, null=True, blank=True)
    
    class Meta:
        ordering = ['inicio']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        
    def __str__(self):
        return self.titulo
    
    def vagas_restantes(self):
        return self.local.capacidade - self.relatorios.presentes


class Atividade(models.Model):
    titulo = models.CharField(max_length=100)
    palestrante = models.CharField(max_length=100)
    horario = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='atividades')
    
    class Meta:
        ordering = ['horario']
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        
    def __str__(self):
        return self.titulo

class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    inscrito = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
    
    class Meta:
        verbose_name = 'Inscricao'
        verbose_name_plural = 'Inscricoes'
        
    def __str__(self):
        return self.nome

class Relatorio(models.Model):
    presentes = models.PositiveIntegerField()
    observacoes = models.TextField(null=True, blank=True)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE, related_name='relatorios')
    
    class Meta:
        verbose_name = 'Relatorio'
        verbose_name_plural = 'Relatorios'

    def __str__(self):
        return f'Relatorio({self.id})'
