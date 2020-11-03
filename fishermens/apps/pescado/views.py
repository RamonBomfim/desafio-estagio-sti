from django.shortcuts import render, redirect, get_object_or_404
from .models import RankingWeight, RankingAmount
from .forms import CompeteWeightRank, CompeteAmountRank


def choose_rank(request):
    rank_weight = RankingWeight.objects.all()
    rank_amount = RankingAmount.objects.all()
    return render(request, 'pescado/choose_rank.html', {'rank_weight': rank_weight,
                                                        'rank_amount': rank_amount})


def register_rankweight(request):
    form = CompeteWeightRank(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('rankings')

    return render(request, 'pescado/registro_rankweight.html', {'form': form})


def register_rankamount(request):
    form = CompeteAmountRank(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('rankings')

    return render(request, 'pescado/registro_rankamount.html', {'form': form})


def update_rankweight(request, id):
    fisherman = get_object_or_404(RankingWeight, pk=id)
    form = CompeteWeightRank(request.POST or None, request.FILES or None, instance=fisherman)

    if form.is_valid():
        form.save()
        return redirect('rankings')

    return render(request, 'pescado/registro_rankweight.html', {'form': form})


def update_rankamount(request, id):
    fisherman = get_object_or_404(RankingAmount, pk=id)
    form = CompeteAmountRank(request.POST or None, request.FILES or None, instance=fisherman)

    if form.is_valid():
        form.save()
        return redirect('rankings')

    return render(request, 'pescado/registro_rankamount.html', {'form': form})


def delete_rankweight(request, id):
    fisherman = get_object_or_404(RankingWeight, pk=id)

    if request.method == 'POST':
        fisherman.delete()
        return redirect('rankings')

    return render(request, 'pescado/confirm_del_competidor_peso.html', {'fisherman': fisherman})


def delete_rankamount(request, id):
    fisherman = get_object_or_404(RankingAmount, pk=id)

    if request.method == 'POST':
        fisherman.delete()
        return redirect('rankings')

    return render(request, 'pescado/confirm_del_competidor_qnt.html', {'fisherman': fisherman})
