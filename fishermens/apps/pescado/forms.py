from django.forms import ModelForm
from .models import RankingWeight, RankingAmount


class CompeteWeightRank(ModelForm):
    class Meta:
        model = RankingWeight
        fields = ['fisherman', 'fish_species', 'fish_weight', 'fish_size', 'image']


class CompeteAmountRank(ModelForm):
    class Meta:
        model = RankingAmount
        fields = ['fisherman', 'fish_species', 'fish_amount', 'image']
