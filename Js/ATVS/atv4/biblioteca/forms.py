from .models import Autor, Livro
from django import forms

class AutorForms(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroForms(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'