from django.db import models

# Create your models here.

class Local(models.Model):
    nome = models.CharField(max_length=150, unique=True)
    endereco = models.CharField(max_length=300)
    capacidade = models.PositiveIntegerField()
    
    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = 'Locais'
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    local = models.ForeignKey(Local, on_delete=models.PROTECT, related_name='locais')
    categoria = models.ManyToManyField(Categoria, related_name='categorias', null=True, blank=True)
    inicio = models.DateTimeField()
    fim = models.DateTimeField()
    criando = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['inicio']
    
    def __str__(self):
        return self.titulo
    
    def vagas_restantes(self):
        return self.local.capacidade - self.evento_inscricao.count()
         
        

class Atividade(models.Model):
    titulo = models.CharField(max_length=200)
    palestrante = models.CharField(max_length=200)
    horario = models.TimeField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='evento_atividade')
    
    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        ordering = ['horario']
    
    def __str__(self):
        return self.titulo
    
class Inscricao(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    inscrito = models.DateTimeField(auto_now_add=True)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='evento_inscricao')
    
    class Meta:
        verbose_name = 'Inscricao'
        verbose_name_plural = 'Inscricoes'
    
    def __str__(self):
        return self.nome

class Relatorio(models.Model):
    presentes = models.PositiveIntegerField()
    observacoes = models.TimeField(null=True, blank=True)
    evento = models.OneToOneField(Evento, on_delete=models.CASCADE, related_name='evento_relatorio')

    class Meta:
        verbose_name = 'Relatorio'
        verbose_name_plural = 'Relatorios'
    
    def __str__(self):
        return f'Relatorio({self.id})'
