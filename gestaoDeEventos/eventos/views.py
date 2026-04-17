from django.shortcuts import render, redirect
from .forms import EventoForm

lista_eventos = []

def formulario_eventos(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            lista_eventos.append({'nome': form.cleaned_data['nome'], 'local': form.cleaned_data['local']})
            return redirect('home')
    else:
        form = EventoForm()

    return render(request, 'novo.html', {'form': form})


def home(request):
    return render(request, 'home.html', {'eventos': lista_eventos})
