from django import forms
from .models import DadosFormulario

class FormularioContato(forms.ModelForm):
    class Meta:
        model = DadosFormulario
        fields = ['nome', 'email', 'mensagem']