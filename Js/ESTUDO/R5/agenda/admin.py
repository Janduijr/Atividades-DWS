from django.contrib import admin
from .models import Evento,Local,Categoria,Atividade,Inscricao,Relatorio
# Register your models here.

admin.site.register(Evento)
admin.site.register(Local)
admin.site.register(Categoria)
admin.site.register(Atividade)
admin.site.register(Inscricao)
admin.site.register(Relatorio)