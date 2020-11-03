from django.shortcuts import render, redirect, get_object_or_404
from .models import Fishing
from .forms import Fisheries


def fishing_data(request):
    fishing_info = Fishing.objects.all()
    return render(request, 'pescaria/dados_pescaria.html', {'fishing_info': fishing_info})


def new_fishing(request):
    form = Fisheries(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('informacoes_pescaria')

    return render(request, 'pescaria/nova_pescaria.html', {'form': form})


def update_fishing(request, id):
    fishing = get_object_or_404(Fishing, pk=id)
    form = Fisheries(request.POST or None, request.FILES or None, instance=fishing)

    if form.is_valid():
        form.save()
        return redirect('informacoes_pescaria')

    return render(request, 'pescaria/nova_pescaria.html', {'form': form})


def delete_fishing(request, id):
    fishing = get_object_or_404(Fishing, pk=id)

    if request.method == 'POST':
        fishing.delete()
        return redirect('informacoes_pescaria')

    return render(request, 'pescaria/delete_pescaria.html', {'fishing': fishing})
