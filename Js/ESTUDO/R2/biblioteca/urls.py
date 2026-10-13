from django.urls import path
from .views import exibir

urlpatterns = [
    path('', exibir, name='exibir'),
]
