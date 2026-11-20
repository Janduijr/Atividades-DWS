from django.contrib import admin
from .models import Livro, Categoria, Autor



class Editlivro(admin.TabularInline):
    model = Livro
    extra = 0

@admin.register(Livro)
class Livroadmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'ano_publicado', 'disponivel']
    search_fields = ['titulo', 'autor__nome']
    list_filter = ['disponivel', 'categoria__nome']
    filter_horizontal = ['categoria']
    
@admin.register(Categoria)
class Categoriaadmin(admin.ModelAdmin):
    ...
    
@admin.register(Autor)
class Autoradmin(admin.ModelAdmin):
    inlines = [Editlivro]

