
from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_livros_view.as_view(), name='listar_livros'),
    path('autor/<int:autor_id>/detalhe/', views.autor_detalhe_view.as_view(), name='autor_detalhe'),
    path('criar/autor', views.criar_autor_view.as_view(), name='criar_autor'),
    path('livro/', views.criarlivroView.as_view(), name='criar_livro'),
    path('livro/<int:pk>/', views.editarlivroView.as_view(), name='editar_livro'),
    path('livro/<int:pk>/excluir/', views.ExcluirLivroView.as_view(), name='excluir_livro'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),
]
