from django.urls import path
from .views import exibir, autor, adicionar

urlpatterns = [
    path('', exibir, name='exibir'),
    path('autor/<int:id>', autor, name='autor'),
    path('adicionar', adicionar, name='adicionar'),
]
