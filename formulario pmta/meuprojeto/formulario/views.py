from django.shortcuts import render, redirect
from .forms import FormularioContato
from .models import DadosFormulario

def contato(request):
    if request.method == 'POST':
        form = FormularioContato(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = FormularioContato()
    return render(request, 'contato.html', {'form': form})

def sucesso(request):
    return render(request, 'sucesso.html')