
from django.urls import path
from .views import listar_livros, autor_detalhe, criar_autor

urlpatterns = [
    path('', listar_livros, name='listar_livros'),
    path('autor/<int:autor_id>/detalhe/', autor_detalhe, name='autor_detalhe'),
    path('criar/autor', criar_autor, name='criar_autor'),
]
