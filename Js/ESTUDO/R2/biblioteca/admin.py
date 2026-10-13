from django.contrib import admin
from .models import Livro, Autor, Categoria
# Register your models here.

class EditLivro(admin.TabularInline):
    model = Livro
    extra = 0

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'ano', 'disponivel']
    search_fields = ['titulo', 'autor__nome']
    list_filter = ['categoria__nome', 'disponivel']
    filter_horizontal = ['categoria']
    
    
@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    inlines = [EditLivro]
    
admin.site.register(Categoria)