from django.contrib import admin
from .models import Local,Categoria,Evento,Atividade,Inscricao,Relatorio
# Register your models here.

admin.site.register(Local)
admin.site.register(Categoria)

class EditAtividade(admin.TabularInline):
    model = Atividade

class EditRelatorio(admin.TabularInline):
    model = Relatorio

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo','inicio','local']
    list_filter = ['local', 'categoria']
    search_fields = ['titulo']
    inlines = [EditAtividade,EditRelatorio]
    
admin.site.register(Atividade)
admin.site.register(Inscricao)
admin.site.register(Relatorio)