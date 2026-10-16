from django.urls import path
from .views import index, detalhe, local

urlpatterns = [
    path('', index, name='index'),
    path('eventos/<int:id>/', detalhe, name='detalhe'),
    path('local/<int:id>/', local, name='local'),
]
