from .models import Autor
from django import forms

class AutorForms(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'
