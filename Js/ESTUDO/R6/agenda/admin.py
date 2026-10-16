from django.contrib import admin
from .models import Local, Categoria, Atividade, Evento, Relatorio, Inscricao
# Register your models here.

class AtividadeEdit(admin.TabularInline):
    model = Atividade
    extra = 1

class RelatorioEdit(admin.TabularInline):
    model = Relatorio
    extra = 1

admin.site.register(Local)
admin.site.register(Categoria)
admin.site.register(Atividade)
admin.site.register(Relatorio)
admin.site.register(Inscricao)

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'inicio', 'local']
    list_filter = ['local', 'categoria']
    search_fields = ['titulo']
    inlines = [AtividadeEdit, RelatorioEdit]
